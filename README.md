# NEXION - Kosmos-Technologie

*Nuclear & Antimatter Overhaul* für **Mindustry Build 160** (Serpulo und Erekir).

Eine reine Content-Mod aus JSON und PNG, ganz ohne JavaScript, Java oder JAR. Dadurch läuft sie auch auf iOS (`iosCompatible: true`).

![Icon](icon.png)

## Inhalt

- **Uran- und Fissionsindustrie:** Uran-Rückgewinnung, Zentrifuge, Brennstab-Presse, Fissions-Atomkraftwerk
- **Antimaterie:** Stabilisator-Mischer, Synthesekammer, Antimaterie-Reaktor, eigene Verteiler, Kreuzungen, Brücken und Impulswerfer
- **Quantenindustrie:** Quanten-Spalter und Quantenminer (Zufallsausbeute bis hin zur ultraseltenen Antimaterie-Ampulle), Quanten-Schild, Hyper-Knoten
- **Plasma-Kette:** Katalysator-Schmiede, Plasma-Reaktorkammer, Kristallplasma-Fusion, Plasma-Werfer, Kristallplasma-Kanone, Plasma-Turbine, Drucktank
- **Cosmic Expansion:** Neutronium, Dunkle Materie, Kryonit, Pyronium, Neutronenfluid, Sternenplasma, Naniten, Chrono-Essenz, jeweils mit Maschinen, Waffen und Reaktoren
- **Kosmos-Technologie (3.9):** Astralit, Solarit, Ionenkern, Graviplatte, Resonanzkristall, Ionenplasma, Gravitonfluid, Regenerat, dazu der Kosmos-Tiefenbohrer
- **Neue Erze:** Uran, Neutronit, Pyrodit, Astralit, Solarit (im Karteneditor platzierbar, Alternativrezepte für bestehende Welten vorhanden)
- **Verteidigung:** Kontaktminen, Bomben, Superwaffen wie Singularitätskanone und Orbitalkanone
- **Sandbox-Werkzeuge:** Endlosbatterie, Unendlichstrom, Omniknoten, Stabilspeicher

Alle Blöcke gibt es in einer Serpulo- und einer Erekir-Variante.
Umfang: 23 Items, 10 Flüssigkeiten, 243 Blockdateien.

Die empfohlene Forschungsreihenfolge steht in [docs/FORSCHUNGSREIHENFOLGE.md](docs/FORSCHUNGSREIHENFOLGE.md).

## Installation

**Direkt aus GitHub (empfohlen):**
Mindustry → *Mods* → *Mod importieren* → *Von GitHub importieren* → `jksxbW/Nexion` eingeben.

**Als ZIP:**
Die ZIP aus dem neuesten [Release](../../releases) herunterladen und in Mindustry über *Mods* → *Mod importieren* → *Datei* auswählen.

Vor dem Update alte NEXION-Versionen entfernen, Spielstände sichern und zuerst eine neue Sandbox-Welt testen.

## Bekannte Grenzen

- Neue Erzadern erscheinen nicht automatisch in bestehenden Karten. Sie lassen sich im Editor setzen, alternativ erzeugen Extraktoren die Roherze.
- Gravitationseffekte sind Schaden und Verlangsamung, kein echtes Ansaugen. Gegner-Umprogrammierung ist ohne Skriptlogik nicht möglich.
- Ob der Hauptmenü-Logo-Override (`sprites-override/ui/logo.png`) auf iOS greift, ist nicht bestätigt.

## Projektstruktur

```
mod.json              Mod-Metadaten (Version, Name, minGameVersion)
icon.png              Icon im Mod-Menü
content/blocks/       Blöcke (Serpulo + *-erekir)
content/items/        Items
content/liquids/      Flüssigkeiten
sprites/              Texturen, Dateiname = Content-Name
sprites-override/     Ersetzt Originaltexturen (Menü-Logo)
docs/                 Zusatzdokumentation
```

Jeder Push wird per GitHub Action geprüft (gültiges JSON, Sprite zu jedem Block). Ein Tag `vX.Y.Z` baut automatisch die Release-ZIP.

## Changelog

Siehe [CHANGELOG.md](CHANGELOG.md).

## Autor

witty-Gamer-Eli
