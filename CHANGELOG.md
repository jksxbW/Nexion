# Changelog

## 3.9.1 - Logo-Fix
- Hauptmenü-Logo durch kleinere, transparente Version ersetzt (`sprites-override/ui/logo.png`), schwarzer Hintergrund entfernt.

## 3.9.0 - Kosmos-Technologie
- 10 neue Stoffe: Astraliterz, Solariterz (Erze); Astralit, Solarit, Ionenkern, Graviplatte, Resonanzkristall (Items); Ionenplasma, Gravitonfluid, Regenerat (Flüssigkeiten).
- 22 neue Blockarten je Planet: Kosmos-Tiefenbohrer, Astralit-/Solarit-Extraktor, Astralit-/Solarit-Raffinerie, Ionenkern-Presse, Graviplatten-Presse, Resonanz-Kristallisator, Ionenplasma-Kammer, Graviton-Destillator, Regenerat-Labor, Astralit-Lanze, Solarit-Artillerie, Ionensturm-Turm, Graviton-Werfer, Resonanz-Railgun, Ionenkern-Kanone, Ionen-Fusionsreaktor, Solarit-Generator, Regenerat-Matrix, Graviplatten-Bollwerk, Resonanz-Schutzschild.
- Extraktoren erzeugen die neuen Roherze aus bestehenden Ressourcen, damit alte Welten nutzbar bleiben.
- Experimenteller Override des Hauptmenü-Logos.

## 3.8.0 - Erze und Materialverwendung
- Neue Erze Neutroniterz (Härte 7) und Pyroditerz (Härte 6), im Editor platzierbar.
- 14 neue Blockarten je Planet: Quantenbohrer (Stufe 9), Neutronit-Raffinerie, Pyrodit-Schmelzerei, Neutronium-Flak, Schattenpuls-Kanone, Pyronium-Mörser, Kryonit-Salvenwerfer, Chrononebel-Werfer, Sternenflut-Kanone, Neutronensturm, Naniten-Matrix, Neutronium-Bollwerk, Chrono-Schutzschild, Sternenstrom-Turbine.

## 3.7.1 - Plasma-Transportfix
- Plasma, Kristallplasma und Sternenplasma: Temperatur 0,68, nicht brennbar, nicht explosiv, keine Block-Flüssigkeitsreaktionen mehr. Verhindert Brände und Gebäudeschaden in Leitungen.

## 3.7.0 - Cosmic Expansion
- Neue Items: Neutronium, Dunkle Materie, Kryonit, Pyronium.
- Neue Flüssigkeiten: Neutronenfluid, Sternenplasma, Nanitenfluid, Chrono-Essenz.
- 27 neue Blockarten je Planet (Produktion, Waffen, Reaktoren, Superwaffen).
- Antimaterie-Reaktor kühlt jetzt mit Neutronenfluid statt Quanten-Stabilisator.

## 3.6.0 - Plasma-Kette
- Megadepots, Editor-Megadepots und Lagerausgänge entfernt (können in alten Spielständen fehlen).
- Neu: Plasma-Katalysator, Plasma, Kristallplasma sowie Katalysator-Schmiede, Plasma-Reaktorkammer, Kristallplasma-Fusion, Plasma-Werfer, Kristallplasma-Kanone, Plasma-Turbine, Plasma-Drucktank.

## 3.5.0 - Grafikfix
- Anschluss- und Kachelgrafiken von 104 Block-Basissprites überarbeitet.

## 3.3.0 - Editor-Energie
- Editor-Omniknoten (40 Kacheln, 128 Anschlüsse, nur Sandbox).
- Editor-Superstromquelle als `PowerSource` (vorher falscher Typ).
- Fehlende `-power`/`-top`-Layer der Editor-Giga-Batterie ergänzt (behebt "Oh no"-Grafik).
- Neu: Editor-Stabilspeicher mit 2 Mrd. Kapazität.
- Kurzer Mod-Name NEXION.

## 3.2.0 - Quantenminer-Mengenupdate
- Quanten-Spalter: 1 Uran-Brennstab → 10 Quantenladungen.
- Quantenminer: 1 Quantenladung → 1 zufälliges Material oder Quanten-Rückstand. Antimaterie-Ampulle mit Chance 1 : 1.000.000.

## 3.1.0 - iOS-Stabilitätsfix
- `scripts/` komplett entfernt, reine JSON-Mod.
- Kontaktminen nutzen natives ShockMine-Verhalten und verschwinden nach Auslösung.
- Neu: Quantenminer (4x4) für beide Planeten.

## 3.0.0-beta
- Erste zusammengeführte Version: Uran, Antimaterie, Reaktoren, Batterien, Quanten- und Chronomaschinen, Kontaktminen.
