# Working firmware image — evidence / Рабочая прошивка — результаты проверки

> **RU:** Предварительный отчёт по журналу локального Codex от 12 октября 2026. Бинарные файлы в GitHub не загружены. Перед релизом необходимы заключительный аудит лицензий, состава rootfs и способа восстановления.
>
> **EN:** Preliminary findings from local Codex logs dated 12 October 2026. No firmware binary has been uploaded to GitHub. A final review of licensing, rootfs contents, and recovery instructions is required before release.

## Источник / Source location

`D:\autel owerlord\Радио SDR\Материалы и анализ\ANTSDR_E310\firmware\v0.39\ant\build`

RU: Это локальный путь на компьютере разработчика, не адрес публичной загрузки.

EN: This is a developer-local filesystem path, not a public download location.

## Обнаруженные файлы / Identified files

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `ant.itb` | 12,392,479 | `7C9163BBCFC20AE44EDBE8C753F031C79298682C033FFFCBAE0C5D2093F55788` |
| `ant.dfu` | 12,392,495 | `E30A9371F8EDF1B1B5DFD9CC985895552E77F6EC3C66E962E0704A21E296B278` |
| `ant.frm` | 12,392,512 | `B0DD647776FD41F153EE0680847FA81B68BAA177520DA2B111CE3176CBEF69C6` |

## Подтверждения / Evidence

- **RU:** Согласно локальному анализу Codex, `ant.itb` побайтно совпадает с сохранённым payload и началом исторического readback flash. **EN:** Per the Codex audit, `ant.itb` matches the preserved payload and prefix of historical flash readback byte-for-byte.
- **RU:** Сообщается о корректных CRC оболочки DFU и MD5 оболочки FRM. **EN:** The audit reports valid DFU wrapper CRC and FRM wrapper MD5.
- **RU:** По журналу найден FPGA-target `7z020clg400` и совместимость AD9361 с режимом `2r2t`. **EN:** The logs report FPGA target `7z020clg400` and AD9361 `2r2t` configuration.
- **RU:** Настройки AD9361 в работавшей системе также зависели от U-Boot environment и не определяются одним образом. **EN:** The working AD9361 configuration also depended on U-Boot environment settings, which are not fully captured by the image alone.

## Что ещё требуется / Outstanding requirements

1. **RU:** Сверить полный отчёт аудита rootfs и право распространять каждый компонент. **EN:** Review the full rootfs audit and redistributability of each component.
2. **RU:** Задокументировать точную аппаратную ревизию и безопасную процедуру восстановления. **EN:** Document the precise hardware revision and safe recovery procedure.
3. **RU:** Убедиться в отсутствии пользовательских ключей, паролей и уникальных идентификаторов. **EN:** Ensure no user secrets, credentials or device-unique identifiers are included.
4. **RU:** Опубликовать образ с SHA-256 и честной пометкой Tested on one device, только после проверки. **EN:** Publish image, SHA-256 and qualified single-device test status only after review.

**RU:** Этот файл — информация об аудите, не инструкция к немедленной прошивке. **EN:** This document is an audit note, not a flashing instruction.
