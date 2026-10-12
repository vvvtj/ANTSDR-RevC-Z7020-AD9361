# Политика релизов прошивки / Firmware release policy

## Требования / Requirements

**RU:** Перед публикацией бинарного образа необходимо установить его происхождение и подтвердить, что он предназначен для нужной ревизии ANTSDR Rev.C. Данные одного успешно работающего экземпляра не являются гарантией совместимости всех плат.

**EN:** Before publishing a firmware binary, establish its provenance and confirm the target ANTSDR Rev.C hardware revision. A successful test on one board does not guarantee compatibility with all boards.

| Обязательно / Required | RU | EN |
|---|---|---|
| Filename / Имя | Точное имя исходного файла | Exact original filename |
| SHA-256 | Контрольная сумма файла | File checksum |
| Hardware / Плата | Маркировка PCB, Z7020, AD9361 | PCB marking, Z7020, AD9361 |
| Provenance / Источник | Ссылка на upstream, коммит или исходный архив; неизвестное пометить | Upstream link, commit, or source archive; label unknowns |
| Components / Компоненты | Указывать только подтверждённые компоненты | List only verified components |
| Tests / Тесты | Что проверено, на каком экземпляре, результаты | Tested functions, specific device and results |
| Recovery / Восстановление | Проверенный способ восстановления или явно обозначенные ограничения | Verified recovery procedure or clear limitations |
| Licensing / Лицензии | Права на распространение каждого компонента | Redistribution rights for each component |

## Статусы / Release statuses

- **Candidate / Кандидат** — файл найден, но его соответствие ранее использованному образу не доказано. / File found but not positively matched to the previously flashed image.
- **Tested on one device / Проверено на одной плате** — точный файл, SHA-256 и результаты теста задокументированы. / Exact file, SHA-256 and test results documented.
- **Reproducible build / Воспроизводимая сборка** — опубликованы соответствующие исходники, зависимости и команды сборки. / Matching sources, dependencies and build instructions are available.

## Размещение / Storage

**RU:** Исходники — `sources/`, текстовые манифесты — `prebuilt/`, история — `changelogs/`. Крупные образы после проверки — в GitHub Releases. Частные дампы flash и секреты не публикуются.

**EN:** Sources belong in `sources/`, text manifests in `prebuilt/`, changes in `changelogs/`. Verified large binaries belong in GitHub Releases. Private flash dumps and secrets must never be uploaded.

## Проверка SHA-256 в Windows / Verify SHA-256 on Windows

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath 'C:\path\to\firmware.bin'
```

**RU:** Сравните полную контрольную сумму с опубликованной. Не начинайте запись, если данные не совпадают.

**EN:** Compare the full hash with the published checksum. Do not flash the file if they differ.
