package ua.vvvtj.antsdr;

import android.app.Activity;
import android.os.Bundle;
import android.graphics.Color;
import android.graphics.Typeface;
import android.content.ClipData;
import android.content.ClipboardManager;
import android.content.Context;
import android.view.Gravity;
import android.view.View;
import android.widget.*;
import android.text.InputType;
import java.net.*;
import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.*;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.*;

public final class MainActivity extends Activity {
    private EditText host, port;
    private TextView status, report;
    private final ExecutorService worker = Executors.newSingleThreadExecutor();
    private volatile String lastReport = "";
    private final int bg = Color.rgb(7,10,15), surface = Color.rgb(24,31,40), fg=Color.rgb(227,237,245), accent=Color.rgb(79,205,182);

    @Override public void onCreate(Bundle b) {
        super.onCreate(b);
        ScrollView scroll = new ScrollView(this);
        scroll.setFillViewport(true);
        scroll.setBackgroundColor(bg);
        LinearLayout root = new LinearLayout(this);
        root.setOrientation(LinearLayout.VERTICAL);
        root.setPadding(28,40,28,36);
        scroll.addView(root);
        TextView title = text("ANTSDR MOBILE",28,accent,true);
        root.addView(title);
        root.addView(text("Rev.C • AD9361 • IIO / RX диагностика",14,fg,false));
        root.addView(text("\nIP-адрес SDR",15,fg,true));
        host = input("192.168.2.1", InputType.TYPE_CLASS_TEXT | InputType.TYPE_TEXT_VARIATION_URI);
        root.addView(host);
        root.addView(text("TCP-порт IIOD",15,fg,true));
        port = input("30431",InputType.TYPE_CLASS_NUMBER);
        root.addView(port);
        Button check = button("ПРОВЕРИТЬ ПОДКЛЮЧЕНИЕ");
        root.addView(check);
        status=text("Нет подключения. Телефон и SDR должны находиться в одной сети.",14,fg,false);
        status.setPadding(0,20,0,14);
        root.addView(status);
        report=text("Здесь появится ответ IIO-демона и список устройств.",13,fg,false);
        report.setTextIsSelectable(true);
        report.setPadding(18,20,18,20);
        report.setBackgroundColor(surface);
        root.addView(report);
        Button copy=button("КОПИРОВАТЬ ОТЧЁТ");
        root.addView(copy);
        copy.setOnClickListener(v -> {
            ((ClipboardManager)getSystemService(Context.CLIPBOARD_SERVICE)).setPrimaryClip(ClipData.newPlainText("ANTSDR report",lastReport));
            Toast.makeText(this,"Отчёт скопирован",Toast.LENGTH_SHORT).show();
        });
        root.addView(text("\nВерсия 0.1: только чтение IIO-конфигурации. Не передаёт RF, не меняет частоты или прошивку. IQ, спектр и водопад добавляются после проверки соединения.",12,fg,false));
        check.setOnClickListener(v -> {
            final String h = host.getText().toString().trim();
            final String p = port.getText().toString().trim();
            check.setEnabled(false);
            status.setText("Соединение...");
            worker.execute(() -> {
                String output;
                try {
                    int pn = Integer.parseInt(p);
                    if(pn<1 || pn>65535 || h.isEmpty()) throw new IllegalArgumentException("Проверь адрес и порт");
                    output = probe(h,pn);
                    final String display = output;
                    runOnUiThread(() -> {
                        status.setText("Опрос завершён");
                        report.setText(display);
                        lastReport=display;
                        check.setEnabled(true);
                    });
                } catch(Exception ex) {
                    final String err="Ошибка: "+ex.getClass().getSimpleName()+": "+ex.getMessage()+"\nПроверь питание, IP, маршрутизацию и доступность IIOD. USB-C телефона напрямую не создаёт Ethernet-сеть автоматически.";
                    runOnUiThread(() -> {
                        status.setText("Не удалось прочитать IIO");
                        report.setText(err);
                        lastReport=err;
                        check.setEnabled(true);
                    });
                }
            });
        });
        setContentView(scroll);
    }
    private TextView text(String s,int sp,int color,boolean bold){
        TextView t=new TextView(this);t.setText(s);t.setTextSize(sp);t.setTextColor(color);
        if(bold)t.setTypeface(Typeface.DEFAULT,Typeface.BOLD);
        t.setPadding(0,9,0,9);return t;
    }
    private EditText input(String def,int type){
        EditText e=new EditText(this);e.setText(def);e.setSingleLine(true);e.setTextColor(fg);
        e.setInputType(type);e.setSelectAllOnFocus(true);return e;
    }
    private Button button(String label){
        Button b=new Button(this);b.setText(label);b.setAllCaps(false);b.setTextColor(Color.BLACK);
        b.setBackgroundTintList(android.content.res.ColorStateList.valueOf(accent));return b;
    }
    private static String probe(String host,int port) throws Exception {
        try(Socket s=new Socket()) {
            s.connect(new InetSocketAddress(host,port),3500);
            s.setSoTimeout(7000);
            InputStream in=s.getInputStream();
            OutputStream out=s.getOutputStream();
            out.write("PRINT\r\n".getBytes(StandardCharsets.US_ASCII));
            out.flush();
            ByteArrayOutputStream line=new ByteArrayOutputStream();
            int v;
            while((v=in.read())!=-1 && v!='\n'){
                if(line.size()>30)throw new IOException("Некорректный ответ IIOD");
                if(v!='\r')line.write(v);
            }
            if(v==-1)throw new EOFException("IIOD закрыл соединение");
            int length=Integer.parseInt(line.toString("US-ASCII").trim());
            if(length<=0 || length>2_000_000)throw new IOException("PRINT вернул "+length);
            byte[] bytes=new byte[length];
            int off=0;
            while(off<length) {
                int n=in.read(bytes,off,length-off);
                if(n<0)throw new EOFException("Получено "+off+" из "+length+" байт XML");
                off+=n;
            }
            String xml=new String(bytes,StandardCharsets.UTF_8);
            DocumentBuilderFactory f=DocumentBuilderFactory.newInstance();
            f.setFeature("http://apache.org/xml/features/disallow-doctype-decl",true);
            f.setFeature("http://xml.org/sax/features/external-general-entities",false);
            f.setFeature("http://xml.org/sax/features/external-parameter-entities",false);
            f.setExpandEntityReferences(false);
            Document d=f.newDocumentBuilder().parse(new java.io.ByteArrayInputStream(bytes));
            StringBuilder sb=new StringBuilder();
            sb.append("IIOD ").append(host).append(":").append(port).append("\n");
            Element root=d.getDocumentElement();
            sb.append("Контекст: ").append(root.getTagName()).append("\n");
            NodeList devices=d.getElementsByTagName("device");
            sb.append("IIO-устройств: ").append(devices.getLength()).append("\n\n");
            for(int i=0;i<devices.getLength();i++){
                Element el=(Element)devices.item(i);
                sb.append(i+1).append(". ").append(el.getAttribute("id")).append("   ").append(el.getAttribute("name")).append("\n");
                NodeList chans=el.getElementsByTagName("channel");
                sb.append("   Каналов: ").append(chans.getLength()).append("\n");
                for(int j=0;j<Math.min(chans.getLength(),12);j++){
                    Element ch=(Element)chans.item(j);
                    sb.append("   • ").append(ch.getAttribute("id")).append(" ").append(ch.getAttribute("type")).append("\n");
                }
            }
            sb.append("\nXML получен: ").append(length).append(" байт.\n");
            if(devices.getLength()==0)sb.append("Предупреждение: XML не содержит IIO-устройств.\n");
            return sb.toString();
        }
    }
    @Override protected void onDestroy(){worker.shutdownNow();super.onDestroy();}
}
