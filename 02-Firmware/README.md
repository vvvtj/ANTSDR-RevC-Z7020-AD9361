# Firmware / Прошивка

**RU:** Прошивка ANTSDR Rev.C (Zynq-7020 + AD9361): происхождение файлов, исходники, готовые образы и процедуры безопасного восстановления.

**EN:** Firmware resources for ANTSDR Rev.C (Zynq-7020 + AD9361): file provenance, source code, prebuilt images, and safe recovery procedures.

## Структура / Directory structure

| Каталог / Directory | RU | EN |
|---|---|---|
| [sources/](sources/) | Исходники, патчи, сведения о лицензировании | Source code, patches, licensing information |
| [prebuilt/](prebuilt/) | Проверенные бинарные образы и манифесты | Verified binaries and manifests |
| [backups/](backups/) | Инструкции резервного копирования и восстановления | Backup and recovery instructions |
| [changelogs/](changelogs/) | История изменений и совместимость | Changelogs and compatibility notes |

## Состояние / Current status

**RU:** На одном экземпляре платы наблюдались Linux 6.1 и строка версии `v0.39-1-g7bcc-dirty`. Это **не подтверждает** точный состав и происхождение всего образа. Файл успешно использованной прошивки необходимо сопоставить с журналами записи и SHA-256 до публикации в Releases.

**EN:** Linux 6.1 and version string `v0.39-1-g7bcc-dirty` were observed on one board. This **does not establish** the precise contents or provenance of the entire firmware image. The previously flashed working image must be matched against flashing records and its SHA-256 before a GitHub Release is published.

**RU:** Не прошивайте неизвестные или несовместимые образы. Публичные резервные копии не должны содержать приватных ключей, идентификаторов устройства и пользовательских секретов.

**EN:** Do not flash unknown or incompatible images. Public backups must not contain private keys, device-unique identifiers, or user secrets.

[Правила публикации релизов / Release policy](RELEASE-POLICY.md) · [Шаблон релиза / Release template](RELEASE-TEMPLATE.md)
