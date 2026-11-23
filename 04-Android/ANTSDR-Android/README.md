# ANTSDR Mobile 0.1
Android 8+ diagnostic client for ANTSDR Rev.C / AD9361 with network IIOD.

## Scope
- TCP connection to configurable address (default 192.168.2.1:30431)
- Legacy IIOD PRINT command, XML context parsing, IIO device and channel listing
- Copyable diagnostic report, Russian dark UI
- Receive-only diagnostic: does not stream IQ, demodulate, transmit, or change SDR parameters

## Build
The parent repository workflow **.github/workflows/antsdr-android-apk.yml** builds the debug APK with Android SDK and Gradle 8.9; download it under Actions > Build Android APK > Artifacts. Android may require permission to install an APK from the browser/files app.

## Caveats
- The legacy ASCII PRINT command works with older IIOD; a newer binary-only server or incompatible firmware can reject it. A TCP connection alone is not proof that streaming works.
- Android needs routing to the SDR IP, via appropriate Ethernet or USB networking.
- No ANTSDR hardware has been used for a live verification of this APK yet.
- Future: native libiio for RX IQ streams, waterfall, tuning and gain.
