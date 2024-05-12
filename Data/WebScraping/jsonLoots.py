from bs4 import BeautifulSoup
import pandas as pd
from GenericsFunctions import linkName_textName as linkLoot_textLoot
from GenericsFunctions import dataframe_json

def jsonLoots():
    linksLoot = [
        ('https://minecraft.fandom.com/wiki/Ancient_City',                [0,3]),
        ('https://minecraft.fandom.com/wiki/Mineshaft',                   [0]),
        ('https://minecraft.fandom.com/wiki/Stronghold',                  [0,2,4]),
        ('https://minecraft.fandom.com/wiki/Buried_Treasure',             [0]),
        ('https://minecraft.fandom.com/wiki/Trail_Ruins',                 [0,2]),
        ('https://minecraft.fandom.com/wiki/Desert_pyramid',              [0,3]),
        ('https://minecraft.fandom.com/wiki/Igloo',                       [0]),
        ('https://minecraft.fandom.com/wiki/Jungle_pyramid',              [0,3]),
        ('https://minecraft.fandom.com/wiki/Pillager_Outpost',            [0]),
        ('https://minecraft.fandom.com/wiki/Swamp_hut',                   []),
        ('https://minecraft.fandom.com/wiki/Woodland_Mansion',            [0]),
        ('https://minecraft.fandom.com/wiki/Ruined_Portal',               [0]),
        ('https://minecraft.fandom.com/wiki/Ocean_Ruins',                 [0,2,4,6]),
        ('https://minecraft.fandom.com/wiki/Shipwreck',                   [0,2,4]),
        ('https://minecraft.fandom.com/wiki/Ocean_Monument',              []),
        ('https://minecraft.fandom.com/wiki/Nether_Fortress',             [0]),
        ('https://minecraft.fandom.com/wiki/Bastion_Remnant',             [0,2,4,6]),
        ('https://minecraft.fandom.com/wiki/Nether_Fossil',               []),
        ('https://minecraft.fandom.com/wiki/Ruined_Portal',               [0]),
        ('https://minecraft.fandom.com/wiki/End_City',                    [0]),
        ('https://minecraft.fandom.com/wiki/Dungeon',                     [0]),
        ('https://minecraft.fandom.com/wiki/Desert_Well',                 [0]),
        ('https://minecraft.fandom.com/wiki/Bonus_Chest',                 [0]),
        ('https://minecraft.fandom.com/wiki/Pile',                        []),
        ('https://minecraft.fandom.com/wiki/Forest_rock',                 []),
        ('https://minecraft.fandom.com/wiki/Geode',                       []),
        ('https://minecraft.fandom.com/wiki/Fossil',                      []),
        ('https://minecraft.fandom.com/wiki/Ice_spike',                   []),
        ('https://minecraft.fandom.com/wiki/Iceberg_(feature)',           []),
        ('https://minecraft.fandom.com/wiki/Exit_Portal',                 []),
        ('https://minecraft.fandom.com/wiki/End_gateway',                 []),
        ('https://minecraft.fandom.com/wiki/End_spike',                   []),
        ('https://minecraft.fandom.com/wiki/Obsidian_platform',           []),
        ('https://minecraft.fandom.com/wiki/Void_start_platform',         [])
        ]

    htmlsLoot = [
        ('https://minecraft.fandom.com/wiki/Village',           [0,2,4,5,6,8,9,11,13,15,17,19,21,23,25,27], """<div class="load-page pageloader-contentloaded" data-page="Village/Loot">
    <h3><span class="mw-headline" id="Loot">Loot</span><span class="mw-editsection-like load-page-button" style="min-width: 58px;">[<span class="jslink">hide</span>]</span><span class="mw-editsection-like" title="Edit: Village/Loot">[<a target="_self" class="text" href="https://minecraft.fandom.com/wiki/Village/Loot?action=edit">edit</a>]</span></h3>
    <div class="load-page-content" style=""><div class="mw-parser-output"><figure class="thumb tright show-info-icon" style="width: 180px"> 	<a href="https://static.wikia.nocookie.net/minecraft_gamepedia/images/2/2c/Villagechest.png/revision/latest?cb=20220728020643" class="image"><img alt="Villagechest" src="https://static.wikia.nocookie.net/minecraft_gamepedia/images/2/2c/Villagechest.png/revision/latest/scale-to-width-down/180?cb=20220728020643" decoding="async" loading="lazy" width="180" height="98" class="thumbimage" data-image-name="Villagechest.png" data-image-key="Villagechest.png" data-relevant="1"></a> 	 	<figcaption class="thumbcaption"> 		 			<a href="/wiki/File:Villagechest.png" class="info-icon"><svg><use xlink:href="#wds-icons-info-small"></use></svg></a> 		 		 		 			<p class="caption">Typical blacksmith loot from a village before 1.14.</p> 		 	</figcaption> </figure>
    <figure class="thumb tright show-info-icon" style="width: 180px"> 	<a href="https://static.wikia.nocookie.net/minecraft_gamepedia/images/a/ae/Loot_in_Village_Desert_Temple_1.png/revision/latest?cb=20210612173304" class="image"><img alt="Loot in Village Desert Temple 1" src="https://static.wikia.nocookie.net/minecraft_gamepedia/images/a/ae/Loot_in_Village_Desert_Temple_1.png/revision/latest/scale-to-width-down/180?cb=20210612173304" decoding="async" loading="lazy" width="180" height="93" class="thumbimage" data-image-name="Loot in Village Desert Temple 1.png" data-image-key="Loot_in_Village_Desert_Temple_1.png" data-relevant="1"></a> 	 	<figcaption class="thumbcaption"> 		 			<a href="/wiki/File:Loot_in_Village_Desert_Temple_1.png" class="info-icon"><svg><use xlink:href="#wds-icons-info-small"></use></svg></a> 		 		 		 			<p class="caption">A chest loot from a 1.14 village desert temple, the village desert temple has the rarest chance of generating in a desert village in Bedrock Edition.</p> 		 	</figcaption> </figure>
    <div id="toc" class="toc" role="navigation" aria-labelledby="mw-toc-heading"><input type="checkbox" role="button" id="toctogglecheckbox" class="toctogglecheckbox" style="display:none"><div class="toctitle" lang="en" dir="ltr"><h2 id="mw-toc-heading">Contents</h2><span class="toctogglespan"><label class="toctogglelabel" for="toctogglecheckbox"></label></span></div>
    <ul>
    <li class="toclevel-1"><a href="#Armorer_House"><span class="tocnumber">1</span> <span class="toctext">Armorer House</span></a></li>
    <li class="toclevel-1"><a href="#Butcher_Shop"><span class="tocnumber">2</span> <span class="toctext">Butcher Shop</span></a></li>
    <li class="toclevel-1"><a href="#Cartographer_House"><span class="tocnumber">3</span> <span class="toctext">Cartographer House</span></a></li>
    <li class="toclevel-1"><a href="#Fisher_Cottage"><span class="tocnumber">4</span> <span class="toctext">Fisher Cottage</span></a></li>
    <li class="toclevel-1"><a href="#Fletcher_House"><span class="tocnumber">5</span> <span class="toctext">Fletcher House</span></a></li>
    <li class="toclevel-1"><a href="#Mason_House"><span class="tocnumber">6</span> <span class="toctext">Mason House</span></a></li>
    <li class="toclevel-1"><a href="#Shepherd_House"><span class="tocnumber">7</span> <span class="toctext">Shepherd House</span></a></li>
    <li class="toclevel-1"><a href="#Tannery"><span class="tocnumber">8</span> <span class="toctext">Tannery</span></a></li>
    <li class="toclevel-1"><a href="#Temple"><span class="tocnumber">9</span> <span class="toctext">Temple</span></a></li>
    <li class="toclevel-1"><a href="#Toolsmith"><span class="tocnumber">10</span> <span class="toctext">Toolsmith</span></a></li>
    <li class="toclevel-1"><a href="#Weaponsmith"><span class="tocnumber">11</span> <span class="toctext">Weaponsmith</span></a></li>
    <li class="toclevel-1"><a href="#Desert_House"><span class="tocnumber">12</span> <span class="toctext">Desert House</span></a></li>
    <li class="toclevel-1"><a href="#Plain_House"><span class="tocnumber">13</span> <span class="toctext">Plain House</span></a></li>
    <li class="toclevel-1"><a href="#Savanna_House"><span class="tocnumber">14</span> <span class="toctext">Savanna House</span></a></li>
    <li class="toclevel-1"><a href="#Snowy_House"><span class="tocnumber">15</span> <span class="toctext">Snowy House</span></a></li>
    <li class="toclevel-1"><a href="#Taiga_House"><span class="tocnumber">16</span> <span class="toctext">Taiga House</span></a></li>
    </ul>
    </div>

    <h3><span class="mw-headline" id="Armorer_House">Armorer House</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><span class="mw-editsection-bracket">]</span></span></h3>
    <p>Only one of the armorer house variants in snowy villages contain chests.
    </p><p>In <i><a href="/wiki/Java_Edition" title="Java Edition">Java Edition</a></i>, each village armorer chest contains 1–5 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_1-0" class="reference"><a href="#cite_note-stacksize-1">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_2-0" class="reference"><a href="#cite_note-weight-2">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_3-0" class="reference"><a href="#cite_note-chance-3">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_4-0" class="reference"><a href="#cite_note-items-4">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_5-0" class="reference"><a href="#cite_note-chests-5">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="4"><sup>4</sup>⁄<sub>8</sub></td><td style="text-align:center;">80.6%</td><td style="text-align:center;">3.750</td><td style="text-align:center;">1.2</td></tr>
    <tr>
    <td><a href="/wiki/Iron_ingot" class="mw-redirect" title="Iron ingot"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-112px -560px"></span><span class="sprite-text">Iron Ingot</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>8</sub></td><td style="text-align:center;">54.2%</td><td style="text-align:center;">1.500</td><td style="text-align:center;">1.8</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>8</sub></td><td style="text-align:center;">31.8%</td><td style="text-align:center;">0.375</td><td style="text-align:center;">3.1</td></tr>
    <tr>
    <td><a href="/wiki/Armor" title="Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -416px"></span><span class="sprite-text">Iron Helmet</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>8</sub></td><td style="text-align:center;">31.8%</td><td style="text-align:center;">0.375</td><td style="text-align:center;">3.1</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <p>In <i><a href="/wiki/Bedrock_Edition" title="Bedrock Edition">Bedrock Edition</a></i>, each village armorer chest contains 1–5 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_1-1" class="reference"><a href="#cite_note-stacksize-1">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_2-1" class="reference"><a href="#cite_note-weight-2">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_3-1" class="reference"><a href="#cite_note-chance-3">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_4-1" class="reference"><a href="#cite_note-items-4">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_5-1" class="reference"><a href="#cite_note-chests-5">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="4"><sup>4</sup>⁄<sub>8</sub></td><td style="text-align:center;">80.6%</td><td style="text-align:center;">3.750</td><td style="text-align:center;">1.2</td></tr>
    <tr>
    <td><a href="/wiki/Iron_ingot" class="mw-redirect" title="Iron ingot"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-112px -560px"></span><span class="sprite-text">Iron Ingot</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>8</sub></td><td style="text-align:center;">54.2%</td><td style="text-align:center;">1.500</td><td style="text-align:center;">1.8</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>8</sub></td><td style="text-align:center;">31.8%</td><td style="text-align:center;">0.375</td><td style="text-align:center;">3.1</td></tr>
    <tr>
    <td><a href="/wiki/Armor" title="Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -416px"></span><span class="sprite-text">Iron Helmet</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>8</sub></td><td style="text-align:center;">31.8%</td><td style="text-align:center;">0.375</td><td style="text-align:center;">3.1</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <div class="mobileonly">
    <div class="reflist-upper-alpha"><div class="mw-references-wrap"><ol class="references">
    <li id="cite_note-stacksize-1"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-stacksize_1-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-stacksize_1-1">b</a></sup></span> <span class="reference-text">The size of stacks (or for unstackable items, number) of this item on any given roll.</span>
    </li>
    <li id="cite_note-weight-2"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-weight_2-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-weight_2-1">b</a></sup></span> <span class="reference-text">The weight of this item relative to other items in the pool.</span>
    </li>
    <li id="cite_note-chance-3"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chance_3-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chance_3-1">b</a></sup></span> <span class="reference-text">The odds of finding any of this item in a single chest.</span>
    </li>
    <li id="cite_note-items-4"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-items_4-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-items_4-1">b</a></sup></span> <span class="reference-text">The number of items expected per chest, averaged over a large number of chests.</span>
    </li>
    <li id="cite_note-chests-5"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chests_5-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chests_5-1">b</a></sup></span> <span class="reference-text">The average number of chests the player should expect to search to find any of this item.</span>
    </li>
    </ol></div></div>
    </div>
    <p><br>
    </p>
    <h3><span class="mw-headline" id="Butcher_Shop">Butcher Shop</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><span class="mw-editsection-bracket">]</span></span></h3>
    <p>Only butcher shops in savanna villages contain chests.
    </p><p>In <i><a href="/wiki/Java_Edition" title="Java Edition">Java Edition</a></i>, each village butcher chest contains 1–5 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_6-0" class="reference"><a href="#cite_note-stacksize-6">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_7-0" class="reference"><a href="#cite_note-weight-7">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_8-0" class="reference"><a href="#cite_note-chance-8">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_9-0" class="reference"><a href="#cite_note-items-9">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_10-0" class="reference"><a href="#cite_note-chests-10">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Raw_Beef" title="Raw Beef"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -480px"></span><span class="sprite-text">Raw Beef</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="6"><sup>6</sup>⁄<sub>28</sub></td><td style="text-align:center;">48.6%</td><td style="text-align:center;">1.286</td><td style="text-align:center;">2.1</td></tr>
    <tr>
    <td><a href="/wiki/Raw_Mutton" title="Raw Mutton"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-160px -496px"></span><span class="sprite-text">Raw Mutton</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="6"><sup>6</sup>⁄<sub>28</sub></td><td style="text-align:center;">48.6%</td><td style="text-align:center;">1.286</td><td style="text-align:center;">2.1</td></tr>
    <tr>
    <td><a href="/wiki/Raw_Porkchop" title="Raw Porkchop"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -496px"></span><span class="sprite-text">Raw Porkchop</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="6"><sup>6</sup>⁄<sub>28</sub></td><td style="text-align:center;">48.6%</td><td style="text-align:center;">1.286</td><td style="text-align:center;">2.1</td></tr>
    <tr>
    <td><a href="/wiki/Wheat" title="Wheat"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-192px -576px"></span><span class="sprite-text">Wheat</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="6"><sup>6</sup>⁄<sub>28</sub></td><td style="text-align:center;">48.6%</td><td style="text-align:center;">1.286</td><td style="text-align:center;">2.1</td></tr>
    <tr>
    <td><a href="/wiki/Coal" title="Coal"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-176px -544px"></span><span class="sprite-text">Coal</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="3"><sup>3</sup>⁄<sub>28</sub></td><td style="text-align:center;">27.9%</td><td style="text-align:center;">0.643</td><td style="text-align:center;">3.6</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>28</sub></td><td style="text-align:center;">10.2%</td><td style="text-align:center;">0.107</td><td style="text-align:center;">9.8</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <p>In <i><a href="/wiki/Bedrock_Edition" title="Bedrock Edition">Bedrock Edition</a></i>, each village butcher chest contains 1–5 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_6-1" class="reference"><a href="#cite_note-stacksize-6">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_7-1" class="reference"><a href="#cite_note-weight-7">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_8-1" class="reference"><a href="#cite_note-chance-8">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_9-1" class="reference"><a href="#cite_note-items-9">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_10-1" class="reference"><a href="#cite_note-chests-10">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Raw_Beef" title="Raw Beef"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -480px"></span><span class="sprite-text">Raw Beef</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="6"><sup>6</sup>⁄<sub>28</sub></td><td style="text-align:center;">48.6%</td><td style="text-align:center;">1.286</td><td style="text-align:center;">2.1</td></tr>
    <tr>
    <td><a href="/wiki/Raw_Mutton" title="Raw Mutton"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-160px -496px"></span><span class="sprite-text">Raw Mutton</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="6"><sup>6</sup>⁄<sub>28</sub></td><td style="text-align:center;">48.6%</td><td style="text-align:center;">1.286</td><td style="text-align:center;">2.1</td></tr>
    <tr>
    <td><a href="/wiki/Raw_Porkchop" title="Raw Porkchop"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -496px"></span><span class="sprite-text">Raw Porkchop</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="6"><sup>6</sup>⁄<sub>28</sub></td><td style="text-align:center;">48.6%</td><td style="text-align:center;">1.286</td><td style="text-align:center;">2.1</td></tr>
    <tr>
    <td><a href="/wiki/Wheat" title="Wheat"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-192px -576px"></span><span class="sprite-text">Wheat</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="6"><sup>6</sup>⁄<sub>28</sub></td><td style="text-align:center;">48.6%</td><td style="text-align:center;">1.286</td><td style="text-align:center;">2.1</td></tr>
    <tr>
    <td><a href="/wiki/Coal" title="Coal"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-176px -544px"></span><span class="sprite-text">Coal</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="3"><sup>3</sup>⁄<sub>28</sub></td><td style="text-align:center;">27.9%</td><td style="text-align:center;">0.643</td><td style="text-align:center;">3.6</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>28</sub></td><td style="text-align:center;">10.2%</td><td style="text-align:center;">0.107</td><td style="text-align:center;">9.8</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <div class="mobileonly">
    <div class="reflist-upper-alpha"><div class="mw-references-wrap"><ol class="references">
    <li id="cite_note-stacksize-6"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-stacksize_6-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-stacksize_6-1">b</a></sup></span> <span class="reference-text">The size of stacks (or for unstackable items, number) of this item on any given roll.</span>
    </li>
    <li id="cite_note-weight-7"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-weight_7-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-weight_7-1">b</a></sup></span> <span class="reference-text">The weight of this item relative to other items in the pool.</span>
    </li>
    <li id="cite_note-chance-8"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chance_8-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chance_8-1">b</a></sup></span> <span class="reference-text">The odds of finding any of this item in a single chest.</span>
    </li>
    <li id="cite_note-items-9"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-items_9-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-items_9-1">b</a></sup></span> <span class="reference-text">The number of items expected per chest, averaged over a large number of chests.</span>
    </li>
    <li id="cite_note-chests-10"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chests_10-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chests_10-1">b</a></sup></span> <span class="reference-text">The average number of chests the player should expect to search to find any of this item.</span>
    </li>
    </ol></div></div>
    </div>
    <p><br>
    </p>
    <h3><span class="mw-headline" id="Cartographer_House">Cartographer House</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><span class="mw-editsection-bracket">]</span></span></h3>
    <p>All cartographer houses except those in desert villages contain chests.
    </p><p>In <i><a href="/wiki/Java_Edition" title="Java Edition">Java Edition</a></i>, each village cartographer chest contains 1–5 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_11-0" class="reference"><a href="#cite_note-stacksize-11">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_12-0" class="reference"><a href="#cite_note-weight-12">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_13-0" class="reference"><a href="#cite_note-chance-13">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_14-0" class="reference"><a href="#cite_note-items-14">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_15-0" class="reference"><a href="#cite_note-chests-15">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Paper" title="Paper"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-96px -544px"></span><span class="sprite-text">Paper</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="15"><sup>15</sup>⁄<sub>50</sub></td><td style="text-align:center;">61.2%</td><td style="text-align:center;">2.700</td><td style="text-align:center;">1.6</td></tr>
    <tr>
    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="15"><sup>15</sup>⁄<sub>50</sub></td><td style="text-align:center;">61.2%</td><td style="text-align:center;">2.250</td><td style="text-align:center;">1.6</td></tr>
    <tr>
    <td><a href="/wiki/Map" title="Map"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -528px"></span><span class="sprite-text">Empty Map</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>50</sub></td><td style="text-align:center;">46.2%</td><td style="text-align:center;">1.200</td><td style="text-align:center;">2.2</td></tr>
    <tr>
    <td><a href="/wiki/Stick" title="Stick"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -48px"></span><span class="sprite-text">Stick</span></a></td>
    <td style="text-align:center;" data-sort-value="1.5">1–2</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>50</sub></td><td style="text-align:center;">26.3%</td><td style="text-align:center;">0.450</td><td style="text-align:center;">3.8</td></tr>
    <tr>
    <td><a href="/wiki/Compass" title="Compass"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-32px -880px"></span><span class="sprite-text">Compass</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>50</sub></td><td style="text-align:center;">26.3%</td><td style="text-align:center;">0.300</td><td style="text-align:center;">3.8</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <p>In <i><a href="/wiki/Bedrock_Edition" title="Bedrock Edition">Bedrock Edition</a></i>, each village cartographer chest contains 1–5 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_11-1" class="reference"><a href="#cite_note-stacksize-11">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_12-1" class="reference"><a href="#cite_note-weight-12">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_13-1" class="reference"><a href="#cite_note-chance-13">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_14-1" class="reference"><a href="#cite_note-items-14">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_15-1" class="reference"><a href="#cite_note-chests-15">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Paper" title="Paper"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-96px -544px"></span><span class="sprite-text">Paper</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="15"><sup>15</sup>⁄<sub>50</sub></td><td style="text-align:center;">61.2%</td><td style="text-align:center;">2.700</td><td style="text-align:center;">1.6</td></tr>
    <tr>
    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="15"><sup>15</sup>⁄<sub>50</sub></td><td style="text-align:center;">61.2%</td><td style="text-align:center;">2.250</td><td style="text-align:center;">1.6</td></tr>
    <tr>
    <td><a href="/wiki/Map" title="Map"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-112px -528px"></span><span class="sprite-text">Map</span></a><sup id="cite_ref-map_16-0" class="reference"><a href="#cite_note-map-16">[F]</a></sup></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>50</sub></td><td style="text-align:center;">46.2%</td><td style="text-align:center;">1.200</td><td style="text-align:center;">2.2</td></tr>
    <tr>
    <td><a href="/wiki/Sapling" title="Sapling"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-544px -464px"></span><span class="sprite-text">Oak Sapling</span></a></td>
    <td style="text-align:center;" data-sort-value="1.5">1–2</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>50</sub></td><td style="text-align:center;">26.3%</td><td style="text-align:center;">0.450</td><td style="text-align:center;">3.8</td></tr>
    <tr>
    <td><a href="/wiki/Compass" title="Compass"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-32px -880px"></span><span class="sprite-text">Compass</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>50</sub></td><td style="text-align:center;">26.3%</td><td style="text-align:center;">0.300</td><td style="text-align:center;">3.8</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <div class="mobileonly">
    <div class="reflist-upper-alpha"><div class="mw-references-wrap"><ol class="references">
    <li id="cite_note-stacksize-11"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-stacksize_11-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-stacksize_11-1">b</a></sup></span> <span class="reference-text">The size of stacks (or for unstackable items, number) of this item on any given roll.</span>
    </li>
    <li id="cite_note-weight-12"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-weight_12-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-weight_12-1">b</a></sup></span> <span class="reference-text">The weight of this item relative to other items in the pool.</span>
    </li>
    <li id="cite_note-chance-13"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chance_13-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chance_13-1">b</a></sup></span> <span class="reference-text">The odds of finding any of this item in a single chest.</span>
    </li>
    <li id="cite_note-items-14"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-items_14-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-items_14-1">b</a></sup></span> <span class="reference-text">The number of items expected per chest, averaged over a large number of chests.</span>
    </li>
    <li id="cite_note-chests-15"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chests_15-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chests_15-1">b</a></sup></span> <span class="reference-text">The average number of chests the player should expect to search to find any of this item.</span>
    </li>
    <li id="cite_note-map-16"><span class="mw-cite-backlink"><a href="#cite_ref-map_16-0" aria-label="Jump up" title="Jump up">↑</a></span> <span class="reference-text">Named unknown map, but changed to map 0, the scale level is 1:4, Maps from the same stack are stackable, but maps that are not stacked are unstackable despite looking identical.</span>
    </li>
    </ol></div></div>
    </div>
    <p><br>
    </p>
    <h3><span class="mw-headline" id="Fisher_Cottage">Fisher Cottage</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><span class="mw-editsection-bracket">]</span></span></h3>
    <p>Only fisher cottages in plains villages in <a href="/wiki/Java_Edition" title="Java Edition"><i>Java Edition</i></a> contain chests.
    </p><p>In <i><a href="/wiki/Java_Edition" title="Java Edition">Java Edition</a></i>, each village fisherman chest contains 1–5 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_17-0" class="reference"><a href="#cite_note-stacksize-17">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_18-0" class="reference"><a href="#cite_note-weight-18">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_19-0" class="reference"><a href="#cite_note-chance-19">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_20-0" class="reference"><a href="#cite_note-items-20">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_21-0" class="reference"><a href="#cite_note-chests-21">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Wheat_seeds" class="mw-redirect" title="Wheat seeds"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-144px -0px"></span><span class="sprite-text">Wheat Seeds</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="3"><sup>3</sup>⁄<sub>11</sub></td><td style="text-align:center;">57.5%</td><td style="text-align:center;">1.636</td><td style="text-align:center;">1.7</td></tr>
    <tr>
    <td><a href="/wiki/Coal" title="Coal"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-176px -544px"></span><span class="sprite-text">Coal</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>11</sub></td><td style="text-align:center;">43.0%</td><td style="text-align:center;">1.091</td><td style="text-align:center;">2.3</td></tr>
    <tr>
    <td><a href="/wiki/Raw_Cod" title="Raw Cod"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-240px -320px"></span><span class="sprite-text">Raw Cod</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>11</sub></td><td style="text-align:center;">43.0%</td><td style="text-align:center;">1.091</td><td style="text-align:center;">2.3</td></tr>
    <tr>
    <td><a href="/wiki/Barrel" title="Barrel"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-48px -336px"></span><span class="sprite-text">Barrel</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>11</sub></td><td style="text-align:center;">24.2%</td><td style="text-align:center;">0.545</td><td style="text-align:center;">4.1</td></tr>
    <tr>
    <td><a href="/wiki/Raw_Salmon" title="Raw Salmon"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-192px -336px"></span><span class="sprite-text">Raw Salmon</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>11</sub></td><td style="text-align:center;">24.2%</td><td style="text-align:center;">0.545</td><td style="text-align:center;">4.1</td></tr>
    <tr>
    <td><a href="/wiki/Water_bucket" class="mw-redirect" title="Water bucket"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-224px -464px"></span><span class="sprite-text">Water Bucket</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>11</sub></td><td style="text-align:center;">24.2%</td><td style="text-align:center;">0.545</td><td style="text-align:center;">4.1</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>11</sub></td><td style="text-align:center;">24.2%</td><td style="text-align:center;">0.273</td><td style="text-align:center;">4.1</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <div class="mobileonly">
    <div class="reflist-upper-alpha"><div class="mw-references-wrap"><ol class="references">
    <li id="cite_note-stacksize-17"><span class="mw-cite-backlink"><a href="#cite_ref-stacksize_17-0" aria-label="Jump up" title="Jump up">↑</a></span> <span class="reference-text">The size of stacks (or for unstackable items, number) of this item on any given roll.</span>
    </li>
    <li id="cite_note-weight-18"><span class="mw-cite-backlink"><a href="#cite_ref-weight_18-0" aria-label="Jump up" title="Jump up">↑</a></span> <span class="reference-text">The weight of this item relative to other items in the pool.</span>
    </li>
    <li id="cite_note-chance-19"><span class="mw-cite-backlink"><a href="#cite_ref-chance_19-0" aria-label="Jump up" title="Jump up">↑</a></span> <span class="reference-text">The odds of finding any of this item in a single chest.</span>
    </li>
    <li id="cite_note-items-20"><span class="mw-cite-backlink"><a href="#cite_ref-items_20-0" aria-label="Jump up" title="Jump up">↑</a></span> <span class="reference-text">The number of items expected per chest, averaged over a large number of chests.</span>
    </li>
    <li id="cite_note-chests-21"><span class="mw-cite-backlink"><a href="#cite_ref-chests_21-0" aria-label="Jump up" title="Jump up">↑</a></span> <span class="reference-text">The average number of chests the player should expect to search to find any of this item.</span>
    </li>
    </ol></div></div>
    </div>
    <p><br>
    </p>
    <h3><span class="mw-headline" id="Fletcher_House">Fletcher House</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><span class="mw-editsection-bracket">]</span></span></h3>
    <p>Only fletcher houses in taiga villages contain chests.
    </p><p>In <i><a href="/wiki/Java_Edition" title="Java Edition">Java Edition</a></i>, each village fletcher chest contains 1–5 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_22-0" class="reference"><a href="#cite_note-stacksize-22">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_23-0" class="reference"><a href="#cite_note-weight-23">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_24-0" class="reference"><a href="#cite_note-chance-24">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_25-0" class="reference"><a href="#cite_note-items-25">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_26-0" class="reference"><a href="#cite_note-chests-26">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Feather" title="Feather"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-240px -544px"></span><span class="sprite-text">Feather</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="6"><sup>6</sup>⁄<sub>23</sub></td><td style="text-align:center;">55.8%</td><td style="text-align:center;">1.565</td><td style="text-align:center;">1.8</td></tr>
    <tr>
    <td><a href="/wiki/Flint" title="Flint"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-0px -560px"></span><span class="sprite-text">Flint</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="6"><sup>6</sup>⁄<sub>23</sub></td><td style="text-align:center;">55.8%</td><td style="text-align:center;">1.565</td><td style="text-align:center;">1.8</td></tr>
    <tr>
    <td><a href="/wiki/Stick" title="Stick"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -48px"></span><span class="sprite-text">Stick</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="6"><sup>6</sup>⁄<sub>23</sub></td><td style="text-align:center;">55.8%</td><td style="text-align:center;">1.565</td><td style="text-align:center;">1.8</td></tr>
    <tr>
    <td><a href="/wiki/Arrow" title="Arrow"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -32px"></span><span class="sprite-text">Arrow</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>23</sub></td><td style="text-align:center;">23.3%</td><td style="text-align:center;">0.522</td><td style="text-align:center;">4.3</td></tr>
    <tr>
    <td><a href="/wiki/Egg" title="Egg"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-48px -496px"></span><span class="sprite-text">Egg</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>23</sub></td><td style="text-align:center;">23.3%</td><td style="text-align:center;">0.522</td><td style="text-align:center;">4.3</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>23</sub></td><td style="text-align:center;">12.3%</td><td style="text-align:center;">0.130</td><td style="text-align:center;">8.1</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <p>In <i><a href="/wiki/Bedrock_Edition" title="Bedrock Edition">Bedrock Edition</a></i>, each village fletcher chest contains 1–5 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_22-1" class="reference"><a href="#cite_note-stacksize-22">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_23-1" class="reference"><a href="#cite_note-weight-23">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_24-1" class="reference"><a href="#cite_note-chance-24">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_25-1" class="reference"><a href="#cite_note-items-25">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_26-1" class="reference"><a href="#cite_note-chests-26">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Feather" title="Feather"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-240px -544px"></span><span class="sprite-text">Feather</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="6"><sup>6</sup>⁄<sub>23</sub></td><td style="text-align:center;">55.8%</td><td style="text-align:center;">1.565</td><td style="text-align:center;">1.8</td></tr>
    <tr>
    <td><a href="/wiki/Flint" title="Flint"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-0px -560px"></span><span class="sprite-text">Flint</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="6"><sup>6</sup>⁄<sub>23</sub></td><td style="text-align:center;">55.8%</td><td style="text-align:center;">1.565</td><td style="text-align:center;">1.8</td></tr>
    <tr>
    <td><a href="/wiki/Stick" title="Stick"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -48px"></span><span class="sprite-text">Stick</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="6"><sup>6</sup>⁄<sub>23</sub></td><td style="text-align:center;">55.8%</td><td style="text-align:center;">1.565</td><td style="text-align:center;">1.8</td></tr>
    <tr>
    <td><a href="/wiki/Arrow" title="Arrow"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -32px"></span><span class="sprite-text">Arrow</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>23</sub></td><td style="text-align:center;">23.3%</td><td style="text-align:center;">0.522</td><td style="text-align:center;">4.3</td></tr>
    <tr>
    <td><a href="/wiki/Egg" title="Egg"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-48px -496px"></span><span class="sprite-text">Egg</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>23</sub></td><td style="text-align:center;">23.3%</td><td style="text-align:center;">0.522</td><td style="text-align:center;">4.3</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>23</sub></td><td style="text-align:center;">12.3%</td><td style="text-align:center;">0.130</td><td style="text-align:center;">8.1</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <div class="mobileonly">
    <div class="reflist-upper-alpha"><div class="mw-references-wrap"><ol class="references">
    <li id="cite_note-stacksize-22"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-stacksize_22-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-stacksize_22-1">b</a></sup></span> <span class="reference-text">The size of stacks (or for unstackable items, number) of this item on any given roll.</span>
    </li>
    <li id="cite_note-weight-23"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-weight_23-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-weight_23-1">b</a></sup></span> <span class="reference-text">The weight of this item relative to other items in the pool.</span>
    </li>
    <li id="cite_note-chance-24"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chance_24-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chance_24-1">b</a></sup></span> <span class="reference-text">The odds of finding any of this item in a single chest.</span>
    </li>
    <li id="cite_note-items-25"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-items_25-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-items_25-1">b</a></sup></span> <span class="reference-text">The number of items expected per chest, averaged over a large number of chests.</span>
    </li>
    <li id="cite_note-chests-26"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chests_26-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chests_26-1">b</a></sup></span> <span class="reference-text">The average number of chests the player should expect to search to find any of this item.</span>
    </li>
    </ol></div></div>
    </div>
    <p><br>
    </p>
    <h3><span class="mw-headline" id="Mason_House">Mason House</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><span class="mw-editsection-bracket">]</span></span></h3>
    <p>Only mason houses in savanna villages contain chests.
    </p><p>In <i><a href="/wiki/Java_Edition" title="Java Edition">Java Edition</a></i>, each village mason chest contains 1–5 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_27-0" class="reference"><a href="#cite_note-stacksize-27">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_28-0" class="reference"><a href="#cite_note-weight-28">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_29-0" class="reference"><a href="#cite_note-chance-29">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_30-0" class="reference"><a href="#cite_note-items-30">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_31-0" class="reference"><a href="#cite_note-chests-31">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="4"><sup>4</sup>⁄<sub>13</sub></td><td style="text-align:center;">62.2%</td><td style="text-align:center;">2.308</td><td style="text-align:center;">1.6</td></tr>
    <tr>
    <td><a href="/wiki/Stone" title="Stone"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-672px -400px"></span><span class="sprite-text">Stone</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>13</sub></td><td style="text-align:center;">37.7%</td><td style="text-align:center;">0.462</td><td style="text-align:center;">2.7</td></tr>
    <tr>
    <td><a href="/wiki/Stone_bricks" class="mw-redirect" title="Stone bricks"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-176px -480px"></span><span class="sprite-text">Stone Bricks</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>13</sub></td><td style="text-align:center;">37.7%</td><td style="text-align:center;">0.462</td><td style="text-align:center;">2.7</td></tr>
    <tr>
    <td><a href="/wiki/Clay_Ball" title="Clay Ball"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-160px -544px"></span><span class="sprite-text">Clay Ball</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>13</sub></td><td style="text-align:center;">20.8%</td><td style="text-align:center;">0.462</td><td style="text-align:center;">4.8</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>13</sub></td><td style="text-align:center;">20.8%</td><td style="text-align:center;">0.231</td><td style="text-align:center;">4.8</td></tr>
    <tr>
    <td><a href="/wiki/Flower_pot" class="mw-redirect" title="Flower pot"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-224px -512px"></span><span class="sprite-text">Flower Pot</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>13</sub></td><td style="text-align:center;">20.8%</td><td style="text-align:center;">0.231</td><td style="text-align:center;">4.8</td></tr>
    <tr>
    <td><a href="/wiki/Smooth_stone" class="mw-redirect" title="Smooth stone"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-672px -464px"></span><span class="sprite-text">Smooth Stone</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>13</sub></td><td style="text-align:center;">20.8%</td><td style="text-align:center;">0.231</td><td style="text-align:center;">4.8</td></tr>
    <tr>
    <td><a href="/wiki/Dye" title="Dye"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-64px -608px"></span><span class="sprite-text">Yellow Dye</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>13</sub></td><td style="text-align:center;">20.8%</td><td style="text-align:center;">0.231</td><td style="text-align:center;">4.8</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <p>In <i><a href="/wiki/Bedrock_Edition" title="Bedrock Edition">Bedrock Edition</a></i>, each village mason chest contains 1–5 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_27-1" class="reference"><a href="#cite_note-stacksize-27">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_28-1" class="reference"><a href="#cite_note-weight-28">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_29-1" class="reference"><a href="#cite_note-chance-29">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_30-1" class="reference"><a href="#cite_note-items-30">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_31-1" class="reference"><a href="#cite_note-chests-31">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="4"><sup>4</sup>⁄<sub>13</sub></td><td style="text-align:center;">62.2%</td><td style="text-align:center;">2.308</td><td style="text-align:center;">1.6</td></tr>
    <tr>
    <td><a href="/wiki/Stone" title="Stone"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-672px -400px"></span><span class="sprite-text">Stone</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>13</sub></td><td style="text-align:center;">37.7%</td><td style="text-align:center;">0.462</td><td style="text-align:center;">2.7</td></tr>
    <tr>
    <td><a href="/wiki/Stone_bricks" class="mw-redirect" title="Stone bricks"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-176px -480px"></span><span class="sprite-text">Stone Bricks</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>13</sub></td><td style="text-align:center;">37.7%</td><td style="text-align:center;">0.462</td><td style="text-align:center;">2.7</td></tr>
    <tr>
    <td><a href="/wiki/Clay_Ball" title="Clay Ball"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-160px -544px"></span><span class="sprite-text">Clay Ball</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>13</sub></td><td style="text-align:center;">20.8%</td><td style="text-align:center;">0.462</td><td style="text-align:center;">4.8</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>13</sub></td><td style="text-align:center;">20.8%</td><td style="text-align:center;">0.231</td><td style="text-align:center;">4.8</td></tr>
    <tr>
    <td><a href="/wiki/Flower_pot" class="mw-redirect" title="Flower pot"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-224px -512px"></span><span class="sprite-text">Flower Pot</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>13</sub></td><td style="text-align:center;">20.8%</td><td style="text-align:center;">0.231</td><td style="text-align:center;">4.8</td></tr>
    <tr>
    <td><a href="/wiki/Smooth_stone" class="mw-redirect" title="Smooth stone"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-672px -464px"></span><span class="sprite-text">Smooth Stone</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>13</sub></td><td style="text-align:center;">20.8%</td><td style="text-align:center;">0.231</td><td style="text-align:center;">4.8</td></tr>
    <tr>
    <td><a href="/wiki/Dye" title="Dye"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-64px -608px"></span><span class="sprite-text">Yellow Dye</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>13</sub></td><td style="text-align:center;">20.8%</td><td style="text-align:center;">0.231</td><td style="text-align:center;">4.8</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <div class="mobileonly">
    <div class="reflist-upper-alpha"><div class="mw-references-wrap"><ol class="references">
    <li id="cite_note-stacksize-27"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-stacksize_27-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-stacksize_27-1">b</a></sup></span> <span class="reference-text">The size of stacks (or for unstackable items, number) of this item on any given roll.</span>
    </li>
    <li id="cite_note-weight-28"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-weight_28-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-weight_28-1">b</a></sup></span> <span class="reference-text">The weight of this item relative to other items in the pool.</span>
    </li>
    <li id="cite_note-chance-29"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chance_29-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chance_29-1">b</a></sup></span> <span class="reference-text">The odds of finding any of this item in a single chest.</span>
    </li>
    <li id="cite_note-items-30"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-items_30-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-items_30-1">b</a></sup></span> <span class="reference-text">The number of items expected per chest, averaged over a large number of chests.</span>
    </li>
    <li id="cite_note-chests-31"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chests_31-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chests_31-1">b</a></sup></span> <span class="reference-text">The average number of chests the player should expect to search to find any of this item.</span>
    </li>
    </ol></div></div>
    </div>
    <p><br>
    </p>
    <h3><span class="mw-headline" id="Shepherd_House">Shepherd House</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><span class="mw-editsection-bracket">]</span></span></h3>
    <p>Only shepherd houses in snowy villages contain chests.
    </p><p>In <i><a href="/wiki/Java_Edition" title="Java Edition">Java Edition</a></i>, each village shepherd chest contains 1–5 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_32-0" class="reference"><a href="#cite_note-stacksize-32">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_33-0" class="reference"><a href="#cite_note-weight-33">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_34-0" class="reference"><a href="#cite_note-chance-34">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_35-0" class="reference"><a href="#cite_note-items-35">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_36-0" class="reference"><a href="#cite_note-chests-36">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Wool" title="Wool"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-0px -32px"></span><span class="sprite-text">White Wool</span></a></td>
    <td style="text-align:center;" data-sort-value="4.5">1–8</td><td style="text-align:center;" data-sort-value="6"><sup>6</sup>⁄<sub>23</sub></td><td style="text-align:center;">55.8%</td><td style="text-align:center;">3.522</td><td style="text-align:center;">1.8</td></tr>
    <tr>
    <td><a href="/wiki/Wheat" title="Wheat"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-192px -576px"></span><span class="sprite-text">Wheat</span></a></td>
    <td style="text-align:center;" data-sort-value="3.5">1–6</td><td style="text-align:center;" data-sort-value="6"><sup>6</sup>⁄<sub>23</sub></td><td style="text-align:center;">55.8%</td><td style="text-align:center;">2.739</td><td style="text-align:center;">1.8</td></tr>
    <tr>
    <td><a href="/wiki/Wool" title="Wool"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-400px -48px"></span><span class="sprite-text">Black Wool</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="3"><sup>3</sup>⁄<sub>23</sub></td><td style="text-align:center;">33.0%</td><td style="text-align:center;">0.783</td><td style="text-align:center;">3.0</td></tr>
    <tr>
    <td><a href="/wiki/Wool" title="Wool"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-16px -80px"></span><span class="sprite-text">Brown Wool</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>23</sub></td><td style="text-align:center;">23.3%</td><td style="text-align:center;">0.522</td><td style="text-align:center;">4.3</td></tr>
    <tr>
    <td><a href="/wiki/Wool" title="Wool"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-416px -48px"></span><span class="sprite-text">Gray Wool</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>23</sub></td><td style="text-align:center;">23.3%</td><td style="text-align:center;">0.522</td><td style="text-align:center;">4.3</td></tr>
    <tr>
    <td><a href="/wiki/Wool" title="Wool"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-16px -112px"></span><span class="sprite-text">Light Gray Wool</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>23</sub></td><td style="text-align:center;">23.3%</td><td style="text-align:center;">0.522</td><td style="text-align:center;">4.3</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>23</sub></td><td style="text-align:center;">12.3%</td><td style="text-align:center;">0.130</td><td style="text-align:center;">8.1</td></tr>
    <tr>
    <td><a href="/wiki/Shears" title="Shears"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-144px -464px"></span><span class="sprite-text">Shears</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>23</sub></td><td style="text-align:center;">12.3%</td><td style="text-align:center;">0.130</td><td style="text-align:center;">8.1</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <p>In <i><a href="/wiki/Bedrock_Edition" title="Bedrock Edition">Bedrock Edition</a></i>, each village shepherd chest contains 1–5 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_32-1" class="reference"><a href="#cite_note-stacksize-32">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_33-1" class="reference"><a href="#cite_note-weight-33">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_34-1" class="reference"><a href="#cite_note-chance-34">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_35-1" class="reference"><a href="#cite_note-items-35">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_36-1" class="reference"><a href="#cite_note-chests-36">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Wool" title="Wool"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-0px -32px"></span><span class="sprite-text">White Wool</span></a></td>
    <td style="text-align:center;" data-sort-value="4.5">1–8</td><td style="text-align:center;" data-sort-value="6"><sup>6</sup>⁄<sub>23</sub></td><td style="text-align:center;">55.8%</td><td style="text-align:center;">3.522</td><td style="text-align:center;">1.8</td></tr>
    <tr>
    <td><a href="/wiki/Wheat" title="Wheat"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-192px -576px"></span><span class="sprite-text">Wheat</span></a></td>
    <td style="text-align:center;" data-sort-value="3.5">1–6</td><td style="text-align:center;" data-sort-value="6"><sup>6</sup>⁄<sub>23</sub></td><td style="text-align:center;">55.8%</td><td style="text-align:center;">2.739</td><td style="text-align:center;">1.8</td></tr>
    <tr>
    <td><a href="/wiki/Wool" title="Wool"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-400px -48px"></span><span class="sprite-text">Black Wool</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="3"><sup>3</sup>⁄<sub>23</sub></td><td style="text-align:center;">33.0%</td><td style="text-align:center;">0.783</td><td style="text-align:center;">3.0</td></tr>
    <tr>
    <td><a href="/wiki/Wool" title="Wool"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-16px -80px"></span><span class="sprite-text">Brown Wool</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>23</sub></td><td style="text-align:center;">23.3%</td><td style="text-align:center;">0.522</td><td style="text-align:center;">4.3</td></tr>
    <tr>
    <td><a href="/wiki/Wool" title="Wool"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-416px -48px"></span><span class="sprite-text">Gray Wool</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>23</sub></td><td style="text-align:center;">23.3%</td><td style="text-align:center;">0.522</td><td style="text-align:center;">4.3</td></tr>
    <tr>
    <td><a href="/wiki/Wool" title="Wool"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-16px -112px"></span><span class="sprite-text">Light Gray Wool</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>23</sub></td><td style="text-align:center;">23.3%</td><td style="text-align:center;">0.522</td><td style="text-align:center;">4.3</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>23</sub></td><td style="text-align:center;">12.3%</td><td style="text-align:center;">0.130</td><td style="text-align:center;">8.1</td></tr>
    <tr>
    <td><a href="/wiki/Shears" title="Shears"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-144px -464px"></span><span class="sprite-text">Shears</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>23</sub></td><td style="text-align:center;">12.3%</td><td style="text-align:center;">0.130</td><td style="text-align:center;">8.1</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <div class="mobileonly">
    <div class="reflist-upper-alpha"><div class="mw-references-wrap"><ol class="references">
    <li id="cite_note-stacksize-32"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-stacksize_32-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-stacksize_32-1">b</a></sup></span> <span class="reference-text">The size of stacks (or for unstackable items, number) of this item on any given roll.</span>
    </li>
    <li id="cite_note-weight-33"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-weight_33-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-weight_33-1">b</a></sup></span> <span class="reference-text">The weight of this item relative to other items in the pool.</span>
    </li>
    <li id="cite_note-chance-34"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chance_34-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chance_34-1">b</a></sup></span> <span class="reference-text">The odds of finding any of this item in a single chest.</span>
    </li>
    <li id="cite_note-items-35"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-items_35-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-items_35-1">b</a></sup></span> <span class="reference-text">The number of items expected per chest, averaged over a large number of chests.</span>
    </li>
    <li id="cite_note-chests-36"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chests_36-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chests_36-1">b</a></sup></span> <span class="reference-text">The average number of chests the player should expect to search to find any of this item.</span>
    </li>
    </ol></div></div>
    </div>
    <p><br>
    </p>
    <h3><span class="mw-headline" id="Tannery">Tannery</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><span class="mw-editsection-bracket">]</span></span></h3>
    <p>All tanneries except those in desert villages contain chests.
    </p><p>In <i><a href="/wiki/Java_Edition" title="Java Edition">Java Edition</a></i>, each village tannery chest contains 1–5 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_37-0" class="reference"><a href="#cite_note-stacksize-37">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_38-0" class="reference"><a href="#cite_note-weight-38">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_39-0" class="reference"><a href="#cite_note-chance-39">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_40-0" class="reference"><a href="#cite_note-items-40">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_41-0" class="reference"><a href="#cite_note-chests-41">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>16</sub></td><td style="text-align:center;">62.8%</td><td style="text-align:center;">2.344</td><td style="text-align:center;">1.6</td></tr>
    <tr>
    <td><a href="/wiki/Armor" title="Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-144px -416px"></span><span class="sprite-text">Leather Cap</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>16</sub></td><td style="text-align:center;">31.8%</td><td style="text-align:center;">0.375</td><td style="text-align:center;">3.1</td></tr>
    <tr>
    <td><a href="/wiki/Armor" title="Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-160px -416px"></span><span class="sprite-text">Leather Tunic</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>16</sub></td><td style="text-align:center;">31.8%</td><td style="text-align:center;">0.375</td><td style="text-align:center;">3.1</td></tr>
    <tr>
    <td><a href="/wiki/Armor" title="Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-192px -416px"></span><span class="sprite-text">Leather Pants</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>16</sub></td><td style="text-align:center;">31.8%</td><td style="text-align:center;">0.375</td><td style="text-align:center;">3.1</td></tr>
    <tr>
    <td><a href="/wiki/Armor" title="Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -416px"></span><span class="sprite-text">Leather Boots</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>16</sub></td><td style="text-align:center;">31.8%</td><td style="text-align:center;">0.375</td><td style="text-align:center;">3.1</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>16</sub></td><td style="text-align:center;">17.3%</td><td style="text-align:center;">0.469</td><td style="text-align:center;">5.8</td></tr>
    <tr>
    <td><a href="/wiki/Leather" title="Leather"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-144px -560px"></span><span class="sprite-text">Leather</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>16</sub></td><td style="text-align:center;">17.3%</td><td style="text-align:center;">0.375</td><td style="text-align:center;">5.8</td></tr>
    <tr>
    <td><a href="/wiki/Saddle" title="Saddle"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -528px"></span><span class="sprite-text">Saddle</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>16</sub></td><td style="text-align:center;">17.3%</td><td style="text-align:center;">0.188</td><td style="text-align:center;">5.8</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <p>In <i><a href="/wiki/Bedrock_Edition" title="Bedrock Edition">Bedrock Edition</a></i>, each village tannery chest contains 1–5 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_37-1" class="reference"><a href="#cite_note-stacksize-37">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_38-1" class="reference"><a href="#cite_note-weight-38">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_39-1" class="reference"><a href="#cite_note-chance-39">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_40-1" class="reference"><a href="#cite_note-items-40">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_41-1" class="reference"><a href="#cite_note-chests-41">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>16</sub></td><td style="text-align:center;">62.8%</td><td style="text-align:center;">2.344</td><td style="text-align:center;">1.6</td></tr>
    <tr>
    <td><a href="/wiki/Armor" title="Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-144px -416px"></span><span class="sprite-text">Leather Cap</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>16</sub></td><td style="text-align:center;">31.8%</td><td style="text-align:center;">0.375</td><td style="text-align:center;">3.1</td></tr>
    <tr>
    <td><a href="/wiki/Armor" title="Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-160px -416px"></span><span class="sprite-text">Leather Tunic</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>16</sub></td><td style="text-align:center;">31.8%</td><td style="text-align:center;">0.375</td><td style="text-align:center;">3.1</td></tr>
    <tr>
    <td><a href="/wiki/Armor" title="Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-192px -416px"></span><span class="sprite-text">Leather Pants</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>16</sub></td><td style="text-align:center;">31.8%</td><td style="text-align:center;">0.375</td><td style="text-align:center;">3.1</td></tr>
    <tr>
    <td><a href="/wiki/Armor" title="Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -416px"></span><span class="sprite-text">Leather Boots</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>16</sub></td><td style="text-align:center;">31.8%</td><td style="text-align:center;">0.375</td><td style="text-align:center;">3.1</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>16</sub></td><td style="text-align:center;">17.3%</td><td style="text-align:center;">0.469</td><td style="text-align:center;">5.8</td></tr>
    <tr>
    <td><a href="/wiki/Leather" title="Leather"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-144px -560px"></span><span class="sprite-text">Leather</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>16</sub></td><td style="text-align:center;">17.3%</td><td style="text-align:center;">0.375</td><td style="text-align:center;">5.8</td></tr>
    <tr>
    <td><a href="/wiki/Saddle" title="Saddle"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -528px"></span><span class="sprite-text">Saddle</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>16</sub></td><td style="text-align:center;">17.3%</td><td style="text-align:center;">0.188</td><td style="text-align:center;">5.8</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <div class="mobileonly">
    <div class="reflist-upper-alpha"><div class="mw-references-wrap"><ol class="references">
    <li id="cite_note-stacksize-37"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-stacksize_37-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-stacksize_37-1">b</a></sup></span> <span class="reference-text">The size of stacks (or for unstackable items, number) of this item on any given roll.</span>
    </li>
    <li id="cite_note-weight-38"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-weight_38-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-weight_38-1">b</a></sup></span> <span class="reference-text">The weight of this item relative to other items in the pool.</span>
    </li>
    <li id="cite_note-chance-39"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chance_39-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chance_39-1">b</a></sup></span> <span class="reference-text">The odds of finding any of this item in a single chest.</span>
    </li>
    <li id="cite_note-items-40"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-items_40-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-items_40-1">b</a></sup></span> <span class="reference-text">The number of items expected per chest, averaged over a large number of chests.</span>
    </li>
    <li id="cite_note-chests-41"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chests_41-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chests_41-1">b</a></sup></span> <span class="reference-text">The average number of chests the player should expect to search to find any of this item.</span>
    </li>
    </ol></div></div>
    </div>
    <p><br>
    </p>
    <h3><span class="mw-headline" id="Temple">Temple</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><span class="mw-editsection-bracket">]</span></span></h3>
    <p>Only temples in desert villages contain chests.
    </p><p>In <i><a href="/wiki/Java_Edition" title="Java Edition">Java Edition</a></i>, each village temple chest contains 3–8 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_42-0" class="reference"><a href="#cite_note-stacksize-42">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_43-0" class="reference"><a href="#cite_note-weight-43">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_44-0" class="reference"><a href="#cite_note-chance-44">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_45-0" class="reference"><a href="#cite_note-items-45">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_46-0" class="reference"><a href="#cite_note-chests-46">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="7"><sup>7</sup>⁄<sub>19</sub></td><td style="text-align:center;">89.3%</td><td style="text-align:center;">5.066</td><td style="text-align:center;">1.1</td></tr>
    <tr>
    <td><a href="/wiki/Rotten_flesh" class="mw-redirect" title="Rotten flesh"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-32px -512px"></span><span class="sprite-text">Rotten Flesh</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="7"><sup>7</sup>⁄<sub>19</sub></td><td style="text-align:center;">89.3%</td><td style="text-align:center;">5.066</td><td style="text-align:center;">1.1</td></tr>
    <tr>
    <td><a href="/wiki/Redstone" class="mw-redirect" title="Redstone"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-16px -576px"></span><span class="sprite-text">Redstone Dust</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>19</sub></td><td style="text-align:center;">44.8%</td><td style="text-align:center;">1.447</td><td style="text-align:center;">2.2</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>19</sub></td><td style="text-align:center;">25.4%</td><td style="text-align:center;">0.724</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Lapis_lazuli" class="mw-redirect" title="Lapis lazuli"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -560px"></span><span class="sprite-text">Lapis Lazuli</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>19</sub></td><td style="text-align:center;">25.4%</td><td style="text-align:center;">0.724</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Gold_ingot" class="mw-redirect" title="Gold ingot"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-48px -560px"></span><span class="sprite-text">Gold Ingot</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>19</sub></td><td style="text-align:center;">25.4%</td><td style="text-align:center;">0.724</td><td style="text-align:center;">3.9</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <p>In <i><a href="/wiki/Bedrock_Edition" title="Bedrock Edition">Bedrock Edition</a></i>, each village temple chest contains 3–8 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_42-1" class="reference"><a href="#cite_note-stacksize-42">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_43-1" class="reference"><a href="#cite_note-weight-43">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_44-1" class="reference"><a href="#cite_note-chance-44">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_45-1" class="reference"><a href="#cite_note-items-45">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_46-1" class="reference"><a href="#cite_note-chests-46">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="7"><sup>7</sup>⁄<sub>19</sub></td><td style="text-align:center;">89.3%</td><td style="text-align:center;">5.066</td><td style="text-align:center;">1.1</td></tr>
    <tr>
    <td><a href="/wiki/Rotten_flesh" class="mw-redirect" title="Rotten flesh"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-32px -512px"></span><span class="sprite-text">Rotten Flesh</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="7"><sup>7</sup>⁄<sub>19</sub></td><td style="text-align:center;">89.3%</td><td style="text-align:center;">5.066</td><td style="text-align:center;">1.1</td></tr>
    <tr>
    <td><a href="/wiki/Redstone" class="mw-redirect" title="Redstone"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-16px -576px"></span><span class="sprite-text">Redstone Dust</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>19</sub></td><td style="text-align:center;">44.8%</td><td style="text-align:center;">1.447</td><td style="text-align:center;">2.2</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>19</sub></td><td style="text-align:center;">25.4%</td><td style="text-align:center;">0.724</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Lapis_lazuli" class="mw-redirect" title="Lapis lazuli"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -560px"></span><span class="sprite-text">Lapis Lazuli</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>19</sub></td><td style="text-align:center;">25.4%</td><td style="text-align:center;">0.724</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Gold_ingot" class="mw-redirect" title="Gold ingot"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-48px -560px"></span><span class="sprite-text">Gold Ingot</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>19</sub></td><td style="text-align:center;">25.4%</td><td style="text-align:center;">0.724</td><td style="text-align:center;">3.9</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <div class="mobileonly">
    <div class="reflist-upper-alpha"><div class="mw-references-wrap"><ol class="references">
    <li id="cite_note-stacksize-42"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-stacksize_42-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-stacksize_42-1">b</a></sup></span> <span class="reference-text">The size of stacks (or for unstackable items, number) of this item on any given roll.</span>
    </li>
    <li id="cite_note-weight-43"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-weight_43-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-weight_43-1">b</a></sup></span> <span class="reference-text">The weight of this item relative to other items in the pool.</span>
    </li>
    <li id="cite_note-chance-44"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chance_44-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chance_44-1">b</a></sup></span> <span class="reference-text">The odds of finding any of this item in a single chest.</span>
    </li>
    <li id="cite_note-items-45"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-items_45-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-items_45-1">b</a></sup></span> <span class="reference-text">The number of items expected per chest, averaged over a large number of chests.</span>
    </li>
    <li id="cite_note-chests-46"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chests_46-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chests_46-1">b</a></sup></span> <span class="reference-text">The average number of chests the player should expect to search to find any of this item.</span>
    </li>
    </ol></div></div>
    </div>
    <p><br>
    </p>
    <h3><span class="mw-headline" id="Toolsmith">Toolsmith</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><span class="mw-editsection-bracket">]</span></span></h3>
    <p>Only toolsmiths in desert and taiga villages contain chests.
    </p><p>In <i><a href="/wiki/Java_Edition" title="Java Edition">Java Edition</a></i>, each village toolsmith chest contains 3–8 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_47-0" class="reference"><a href="#cite_note-stacksize-47">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_48-0" class="reference"><a href="#cite_note-weight-48">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_49-0" class="reference"><a href="#cite_note-chance-49">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_50-0" class="reference"><a href="#cite_note-items-50">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_51-0" class="reference"><a href="#cite_note-chests-51">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Stick" title="Stick"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -48px"></span><span class="sprite-text">Stick</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="20"><sup>20</sup>⁄<sub>53</sub></td><td style="text-align:center;">90.0%</td><td style="text-align:center;">4.151</td><td style="text-align:center;">1.1</td></tr>
    <tr>
    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="15"><sup>15</sup>⁄<sub>53</sub></td><td style="text-align:center;">81.2%</td><td style="text-align:center;">3.113</td><td style="text-align:center;">1.2</td></tr>
    <tr>
    <td><a href="/wiki/Iron_ingot" class="mw-redirect" title="Iron ingot"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-112px -560px"></span><span class="sprite-text">Iron Ingot</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>53</sub></td><td style="text-align:center;">41.2%</td><td style="text-align:center;">1.557</td><td style="text-align:center;">2.4</td></tr>
    <tr>
    <td><a href="/wiki/Pickaxe" title="Pickaxe"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-96px -464px"></span><span class="sprite-text">Iron Pickaxe</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>53</sub></td><td style="text-align:center;">41.2%</td><td style="text-align:center;">0.519</td><td style="text-align:center;">2.4</td></tr>
    <tr>
    <td><a href="/wiki/Shovel" title="Shovel"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-112px -464px"></span><span class="sprite-text">Iron Shovel</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>53</sub></td><td style="text-align:center;">41.2%</td><td style="text-align:center;">0.519</td><td style="text-align:center;">2.4</td></tr>
    <tr>
    <td><a href="/wiki/Coal" title="Coal"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-176px -544px"></span><span class="sprite-text">Coal</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>53</sub></td><td style="text-align:center;">9.9%</td><td style="text-align:center;">0.208</td><td style="text-align:center;">10.1</td></tr>
    <tr>
    <td><a href="/wiki/Gold_ingot" class="mw-redirect" title="Gold ingot"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-48px -560px"></span><span class="sprite-text">Gold Ingot</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>53</sub></td><td style="text-align:center;">9.9%</td><td style="text-align:center;">0.208</td><td style="text-align:center;">10.1</td></tr>
    <tr>
    <td><a href="/wiki/Diamond" title="Diamond"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-192px -544px"></span><span class="sprite-text">Diamond</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>53</sub></td><td style="text-align:center;">9.9%</td><td style="text-align:center;">0.208</td><td style="text-align:center;">10.1</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <p>In <i><a href="/wiki/Bedrock_Edition" title="Bedrock Edition">Bedrock Edition</a></i>, each village toolsmith chest contains 3–8 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_47-1" class="reference"><a href="#cite_note-stacksize-47">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_48-1" class="reference"><a href="#cite_note-weight-48">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_49-1" class="reference"><a href="#cite_note-chance-49">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_50-1" class="reference"><a href="#cite_note-items-50">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_51-1" class="reference"><a href="#cite_note-chests-51">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Stick" title="Stick"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -48px"></span><span class="sprite-text">Stick</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="20"><sup>20</sup>⁄<sub>53</sub></td><td style="text-align:center;">90.0%</td><td style="text-align:center;">4.151</td><td style="text-align:center;">1.1</td></tr>
    <tr>
    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="15"><sup>15</sup>⁄<sub>53</sub></td><td style="text-align:center;">81.2%</td><td style="text-align:center;">3.113</td><td style="text-align:center;">1.2</td></tr>
    <tr>
    <td><a href="/wiki/Iron_ingot" class="mw-redirect" title="Iron ingot"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-112px -560px"></span><span class="sprite-text">Iron Ingot</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>53</sub></td><td style="text-align:center;">41.2%</td><td style="text-align:center;">1.557</td><td style="text-align:center;">2.4</td></tr>
    <tr>
    <td><a href="/wiki/Pickaxe" title="Pickaxe"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-96px -464px"></span><span class="sprite-text">Iron Pickaxe</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>53</sub></td><td style="text-align:center;">41.2%</td><td style="text-align:center;">0.519</td><td style="text-align:center;">2.4</td></tr>
    <tr>
    <td><a href="/wiki/Shovel" title="Shovel"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-112px -464px"></span><span class="sprite-text">Iron Shovel</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>53</sub></td><td style="text-align:center;">41.2%</td><td style="text-align:center;">0.519</td><td style="text-align:center;">2.4</td></tr>
    <tr>
    <td><a href="/wiki/Coal" title="Coal"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-176px -544px"></span><span class="sprite-text">Coal</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>53</sub></td><td style="text-align:center;">9.9%</td><td style="text-align:center;">0.208</td><td style="text-align:center;">10.1</td></tr>
    <tr>
    <td><a href="/wiki/Gold_ingot" class="mw-redirect" title="Gold ingot"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-48px -560px"></span><span class="sprite-text">Gold Ingot</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>53</sub></td><td style="text-align:center;">9.9%</td><td style="text-align:center;">0.208</td><td style="text-align:center;">10.1</td></tr>
    <tr>
    <td><a href="/wiki/Diamond" title="Diamond"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-192px -544px"></span><span class="sprite-text">Diamond</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>53</sub></td><td style="text-align:center;">9.9%</td><td style="text-align:center;">0.208</td><td style="text-align:center;">10.1</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <div class="mobileonly">
    <div class="reflist-upper-alpha"><div class="mw-references-wrap"><ol class="references">
    <li id="cite_note-stacksize-47"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-stacksize_47-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-stacksize_47-1">b</a></sup></span> <span class="reference-text">The size of stacks (or for unstackable items, number) of this item on any given roll.</span>
    </li>
    <li id="cite_note-weight-48"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-weight_48-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-weight_48-1">b</a></sup></span> <span class="reference-text">The weight of this item relative to other items in the pool.</span>
    </li>
    <li id="cite_note-chance-49"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chance_49-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chance_49-1">b</a></sup></span> <span class="reference-text">The odds of finding any of this item in a single chest.</span>
    </li>
    <li id="cite_note-items-50"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-items_50-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-items_50-1">b</a></sup></span> <span class="reference-text">The number of items expected per chest, averaged over a large number of chests.</span>
    </li>
    <li id="cite_note-chests-51"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chests_51-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chests_51-1">b</a></sup></span> <span class="reference-text">The average number of chests the player should expect to search to find any of this item.</span>
    </li>
    </ol></div></div>
    </div>
    <p><br>
    </p>
    <h3><span class="mw-headline" id="Weaponsmith">Weaponsmith</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><span class="mw-editsection-bracket">]</span></span></h3>
    <p>All weaponsmiths contain chests.
    </p><p>In <i><a href="/wiki/Java_Edition" title="Java Edition">Java Edition</a></i>, each village weaponsmith chest contains 3–8 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_52-0" class="reference"><a href="#cite_note-stacksize-52">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_53-0" class="reference"><a href="#cite_note-weight-53">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_54-0" class="reference"><a href="#cite_note-chance-54">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_55-0" class="reference"><a href="#cite_note-items-55">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_56-0" class="reference"><a href="#cite_note-chests-56">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Apple" title="Apple"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-48px -480px"></span><span class="sprite-text">Apple</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="15"><sup>15</sup>⁄<sub>94</sub></td><td style="text-align:center;">59.8%</td><td style="text-align:center;">1.755</td><td style="text-align:center;">1.7</td></tr>
    <tr>
    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="15"><sup>15</sup>⁄<sub>94</sub></td><td style="text-align:center;">59.8%</td><td style="text-align:center;">1.755</td><td style="text-align:center;">1.7</td></tr>
    <tr>
    <td><a href="/wiki/Iron_ingot" class="mw-redirect" title="Iron ingot"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-112px -560px"></span><span class="sprite-text">Iron Ingot</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>94</sub></td><td style="text-align:center;">45.1%</td><td style="text-align:center;">1.755</td><td style="text-align:center;">2.2</td></tr>
    <tr>
    <td><a href="/wiki/Sapling" title="Sapling"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-544px -464px"></span><span class="sprite-text">Oak Sapling</span></a></td>
    <td style="text-align:center;" data-sort-value="5">3–7</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>94</sub></td><td style="text-align:center;">25.6%</td><td style="text-align:center;">1.463</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Obsidian" title="Obsidian"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-320px -416px"></span><span class="sprite-text">Obsidian</span></a></td>
    <td style="text-align:center;" data-sort-value="5">3–7</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>94</sub></td><td style="text-align:center;">25.6%</td><td style="text-align:center;">1.463</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Gold_ingot" class="mw-redirect" title="Gold ingot"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-48px -560px"></span><span class="sprite-text">Gold Ingot</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>94</sub></td><td style="text-align:center;">25.6%</td><td style="text-align:center;">0.585</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Pickaxe" title="Pickaxe"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-96px -464px"></span><span class="sprite-text">Iron Pickaxe</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>94</sub></td><td style="text-align:center;">25.6%</td><td style="text-align:center;">0.293</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Sword" title="Sword"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-0px -448px"></span><span class="sprite-text">Iron Sword</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>94</sub></td><td style="text-align:center;">25.6%</td><td style="text-align:center;">0.293</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Armor" title="Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -416px"></span><span class="sprite-text">Iron Helmet</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>94</sub></td><td style="text-align:center;">25.6%</td><td style="text-align:center;">0.293</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Armor" title="Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-64px -416px"></span><span class="sprite-text">Iron Chestplate</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>94</sub></td><td style="text-align:center;">25.6%</td><td style="text-align:center;">0.293</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Armor" title="Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-112px -416px"></span><span class="sprite-text">Iron Leggings</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>94</sub></td><td style="text-align:center;">25.6%</td><td style="text-align:center;">0.293</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Armor" title="Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-48px -416px"></span><span class="sprite-text">Iron Boots</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>94</sub></td><td style="text-align:center;">25.6%</td><td style="text-align:center;">0.293</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Diamond" title="Diamond"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-192px -544px"></span><span class="sprite-text">Diamond</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="3"><sup>3</sup>⁄<sub>94</sub></td><td style="text-align:center;">16.2%</td><td style="text-align:center;">0.351</td><td style="text-align:center;">6.2</td></tr>
    <tr>
    <td><a href="/wiki/Saddle" title="Saddle"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -528px"></span><span class="sprite-text">Saddle</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="3"><sup>3</sup>⁄<sub>94</sub></td><td style="text-align:center;">16.2%</td><td style="text-align:center;">0.176</td><td style="text-align:center;">6.2</td></tr>
    <tr>
    <td><a href="/wiki/Horse_Armor" title="Horse Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-96px -416px"></span><span class="sprite-text">Iron Horse Armor</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>94</sub></td><td style="text-align:center;">5.7%</td><td style="text-align:center;">0.059</td><td style="text-align:center;">17.6</td></tr>
    <tr>
    <td><a href="/wiki/Horse_Armor" title="Horse Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-16px -416px"></span><span class="sprite-text">Golden Horse Armor</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>94</sub></td><td style="text-align:center;">5.7%</td><td style="text-align:center;">0.059</td><td style="text-align:center;">17.6</td></tr>
    <tr>
    <td><a href="/wiki/Horse_Armor" title="Horse Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-176px -400px"></span><span class="sprite-text">Diamond Horse Armor</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>94</sub></td><td style="text-align:center;">5.7%</td><td style="text-align:center;">0.059</td><td style="text-align:center;">17.6</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <p>In <i><a href="/wiki/Bedrock_Edition" title="Bedrock Edition">Bedrock Edition</a></i>, each village weaponsmith chest contains 3–8 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_52-1" class="reference"><a href="#cite_note-stacksize-52">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_53-1" class="reference"><a href="#cite_note-weight-53">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_54-1" class="reference"><a href="#cite_note-chance-54">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_55-1" class="reference"><a href="#cite_note-items-55">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_56-1" class="reference"><a href="#cite_note-chests-56">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Apple" title="Apple"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-48px -480px"></span><span class="sprite-text">Apple</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="15"><sup>15</sup>⁄<sub>94</sub></td><td style="text-align:center;">59.8%</td><td style="text-align:center;">1.755</td><td style="text-align:center;">1.7</td></tr>
    <tr>
    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="15"><sup>15</sup>⁄<sub>94</sub></td><td style="text-align:center;">59.8%</td><td style="text-align:center;">1.755</td><td style="text-align:center;">1.7</td></tr>
    <tr>
    <td><a href="/wiki/Iron_ingot" class="mw-redirect" title="Iron ingot"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-112px -560px"></span><span class="sprite-text">Iron Ingot</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>94</sub></td><td style="text-align:center;">45.1%</td><td style="text-align:center;">1.755</td><td style="text-align:center;">2.2</td></tr>
    <tr>
    <td><a href="/wiki/Sapling" title="Sapling"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-544px -464px"></span><span class="sprite-text">Oak Sapling</span></a></td>
    <td style="text-align:center;" data-sort-value="5">3–7</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>94</sub></td><td style="text-align:center;">25.6%</td><td style="text-align:center;">1.463</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Obsidian" title="Obsidian"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-320px -416px"></span><span class="sprite-text">Obsidian</span></a></td>
    <td style="text-align:center;" data-sort-value="5">3–7</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>94</sub></td><td style="text-align:center;">25.6%</td><td style="text-align:center;">1.463</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Gold_ingot" class="mw-redirect" title="Gold ingot"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-48px -560px"></span><span class="sprite-text">Gold Ingot</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>94</sub></td><td style="text-align:center;">25.6%</td><td style="text-align:center;">0.585</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Pickaxe" title="Pickaxe"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-96px -464px"></span><span class="sprite-text">Iron Pickaxe</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>94</sub></td><td style="text-align:center;">25.6%</td><td style="text-align:center;">0.293</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Sword" title="Sword"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-0px -448px"></span><span class="sprite-text">Iron Sword</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>94</sub></td><td style="text-align:center;">25.6%</td><td style="text-align:center;">0.293</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Armor" title="Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -416px"></span><span class="sprite-text">Iron Helmet</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>94</sub></td><td style="text-align:center;">25.6%</td><td style="text-align:center;">0.293</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Armor" title="Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-64px -416px"></span><span class="sprite-text">Iron Chestplate</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>94</sub></td><td style="text-align:center;">25.6%</td><td style="text-align:center;">0.293</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Armor" title="Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-112px -416px"></span><span class="sprite-text">Iron Leggings</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>94</sub></td><td style="text-align:center;">25.6%</td><td style="text-align:center;">0.293</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Armor" title="Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-48px -416px"></span><span class="sprite-text">Iron Boots</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>94</sub></td><td style="text-align:center;">25.6%</td><td style="text-align:center;">0.293</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Diamond" title="Diamond"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-192px -544px"></span><span class="sprite-text">Diamond</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="3"><sup>3</sup>⁄<sub>94</sub></td><td style="text-align:center;">16.2%</td><td style="text-align:center;">0.351</td><td style="text-align:center;">6.2</td></tr>
    <tr>
    <td><a href="/wiki/Saddle" title="Saddle"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -528px"></span><span class="sprite-text">Saddle</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="3"><sup>3</sup>⁄<sub>94</sub></td><td style="text-align:center;">16.2%</td><td style="text-align:center;">0.176</td><td style="text-align:center;">6.2</td></tr>
    <tr>
    <td><a href="/wiki/Horse_Armor" title="Horse Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-96px -416px"></span><span class="sprite-text">Iron Horse Armor</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>94</sub></td><td style="text-align:center;">5.7%</td><td style="text-align:center;">0.059</td><td style="text-align:center;">17.6</td></tr>
    <tr>
    <td><a href="/wiki/Horse_Armor" title="Horse Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-16px -416px"></span><span class="sprite-text">Golden Horse Armor</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>94</sub></td><td style="text-align:center;">5.7%</td><td style="text-align:center;">0.059</td><td style="text-align:center;">17.6</td></tr>
    <tr>
    <td><a href="/wiki/Horse_Armor" title="Horse Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-176px -400px"></span><span class="sprite-text">Diamond Horse Armor</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>94</sub></td><td style="text-align:center;">5.7%</td><td style="text-align:center;">0.059</td><td style="text-align:center;">17.6</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <div class="mobileonly">
    <div class="reflist-upper-alpha"><div class="mw-references-wrap"><ol class="references">
    <li id="cite_note-stacksize-52"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-stacksize_52-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-stacksize_52-1">b</a></sup></span> <span class="reference-text">The size of stacks (or for unstackable items, number) of this item on any given roll.</span>
    </li>
    <li id="cite_note-weight-53"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-weight_53-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-weight_53-1">b</a></sup></span> <span class="reference-text">The weight of this item relative to other items in the pool.</span>
    </li>
    <li id="cite_note-chance-54"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chance_54-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chance_54-1">b</a></sup></span> <span class="reference-text">The odds of finding any of this item in a single chest.</span>
    </li>
    <li id="cite_note-items-55"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-items_55-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-items_55-1">b</a></sup></span> <span class="reference-text">The number of items expected per chest, averaged over a large number of chests.</span>
    </li>
    <li id="cite_note-chests-56"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chests_56-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chests_56-1">b</a></sup></span> <span class="reference-text">The average number of chests the player should expect to search to find any of this item.</span>
    </li>
    </ol></div></div>
    </div>
    <p><br>
    </p>
    <h3><span class="mw-headline" id="Desert_House">Desert House</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><span class="mw-editsection-bracket">]</span></span></h3>
    <p>In <i><a href="/wiki/Java_Edition" title="Java Edition">Java Edition</a></i>, each village desert house chest contains 3–8 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_57-0" class="reference"><a href="#cite_note-stacksize-57">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_58-0" class="reference"><a href="#cite_note-weight-58">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_59-0" class="reference"><a href="#cite_note-chance-59">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_60-0" class="reference"><a href="#cite_note-items-60">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_61-0" class="reference"><a href="#cite_note-chests-61">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Wheat" title="Wheat"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-192px -576px"></span><span class="sprite-text">Wheat</span></a></td>
    <td style="text-align:center;" data-sort-value="4">1–7</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>36</sub></td><td style="text-align:center;">80.6%</td><td style="text-align:center;">6.111</td><td style="text-align:center;">1.2</td></tr>
    <tr>
    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>36</sub></td><td style="text-align:center;">80.6%</td><td style="text-align:center;">3.819</td><td style="text-align:center;">1.2</td></tr>
    <tr>
    <td><a href="/wiki/Cactus" title="Cactus"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-432px -464px"></span><span class="sprite-text">Cactus</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>36</sub></td><td style="text-align:center;">80.6%</td><td style="text-align:center;">3.819</td><td style="text-align:center;">1.2</td></tr>
    <tr>
    <td><a href="/wiki/Dead_Bush" title="Dead Bush"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-16px -560px"></span><span class="sprite-text">Dead Bush</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>36</sub></td><td style="text-align:center;">26.6%</td><td style="text-align:center;">0.611</td><td style="text-align:center;">3.8</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>36</sub></td><td style="text-align:center;">14.3%</td><td style="text-align:center;">0.306</td><td style="text-align:center;">7.0</td></tr>
    <tr>
    <td><a href="/wiki/Book" title="Book"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-192px -528px"></span><span class="sprite-text">Book</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>36</sub></td><td style="text-align:center;">14.3%</td><td style="text-align:center;">0.153</td><td style="text-align:center;">7.0</td></tr>
    <tr>
    <td><a href="/wiki/Clay_Ball" title="Clay Ball"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-160px -544px"></span><span class="sprite-text">Clay Ball</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>36</sub></td><td style="text-align:center;">14.3%</td><td style="text-align:center;">0.153</td><td style="text-align:center;">7.0</td></tr>
    <tr>
    <td><a href="/wiki/Dye" title="Dye"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-176px -592px"></span><span class="sprite-text">Green Dye</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>36</sub></td><td style="text-align:center;">14.3%</td><td style="text-align:center;">0.153</td><td style="text-align:center;">7.0</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <p>In <i><a href="/wiki/Bedrock_Edition" title="Bedrock Edition">Bedrock Edition</a></i>, each village desert house chest contains 3–8 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_57-1" class="reference"><a href="#cite_note-stacksize-57">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_58-1" class="reference"><a href="#cite_note-weight-58">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_59-1" class="reference"><a href="#cite_note-chance-59">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_60-1" class="reference"><a href="#cite_note-items-60">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_61-1" class="reference"><a href="#cite_note-chests-61">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Wheat" title="Wheat"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-192px -576px"></span><span class="sprite-text">Wheat</span></a></td>
    <td style="text-align:center;" data-sort-value="4">1–7</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>36</sub></td><td style="text-align:center;">80.6%</td><td style="text-align:center;">6.111</td><td style="text-align:center;">1.2</td></tr>
    <tr>
    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>36</sub></td><td style="text-align:center;">80.6%</td><td style="text-align:center;">3.819</td><td style="text-align:center;">1.2</td></tr>
    <tr>
    <td><a href="/wiki/Cactus" title="Cactus"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-432px -464px"></span><span class="sprite-text">Cactus</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>36</sub></td><td style="text-align:center;">80.6%</td><td style="text-align:center;">3.819</td><td style="text-align:center;">1.2</td></tr>
    <tr>
    <td><a href="/wiki/Dead_Bush" title="Dead Bush"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-16px -560px"></span><span class="sprite-text">Dead Bush</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>36</sub></td><td style="text-align:center;">26.6%</td><td style="text-align:center;">0.611</td><td style="text-align:center;">3.8</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>36</sub></td><td style="text-align:center;">14.3%</td><td style="text-align:center;">0.306</td><td style="text-align:center;">7.0</td></tr>
    <tr>
    <td><a href="/wiki/Book" title="Book"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-192px -528px"></span><span class="sprite-text">Book</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>36</sub></td><td style="text-align:center;">14.3%</td><td style="text-align:center;">0.153</td><td style="text-align:center;">7.0</td></tr>
    <tr>
    <td><a href="/wiki/Clay_Ball" title="Clay Ball"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-160px -544px"></span><span class="sprite-text">Clay Ball</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>36</sub></td><td style="text-align:center;">14.3%</td><td style="text-align:center;">0.153</td><td style="text-align:center;">7.0</td></tr>
    <tr>
    <td><a href="/wiki/Dye" title="Dye"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-176px -592px"></span><span class="sprite-text">Green Dye</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>36</sub></td><td style="text-align:center;">14.3%</td><td style="text-align:center;">0.153</td><td style="text-align:center;">7.0</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <div class="mobileonly">
    <div class="reflist-upper-alpha"><div class="mw-references-wrap"><ol class="references">
    <li id="cite_note-stacksize-57"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-stacksize_57-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-stacksize_57-1">b</a></sup></span> <span class="reference-text">The size of stacks (or for unstackable items, number) of this item on any given roll.</span>
    </li>
    <li id="cite_note-weight-58"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-weight_58-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-weight_58-1">b</a></sup></span> <span class="reference-text">The weight of this item relative to other items in the pool.</span>
    </li>
    <li id="cite_note-chance-59"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chance_59-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chance_59-1">b</a></sup></span> <span class="reference-text">The odds of finding any of this item in a single chest.</span>
    </li>
    <li id="cite_note-items-60"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-items_60-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-items_60-1">b</a></sup></span> <span class="reference-text">The number of items expected per chest, averaged over a large number of chests.</span>
    </li>
    <li id="cite_note-chests-61"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chests_61-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chests_61-1">b</a></sup></span> <span class="reference-text">The average number of chests the player should expect to search to find any of this item.</span>
    </li>
    </ol></div></div>
    </div>
    <p><br>
    </p>
    <h3><span class="mw-headline" id="Plain_House">Plain House</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><span class="mw-editsection-bracket">]</span></span></h3>
    <p>In <i><a href="/wiki/Java_Edition" title="Java Edition">Java Edition</a></i>, each village plains house chest contains 3–8 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_62-0" class="reference"><a href="#cite_note-stacksize-62">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_63-0" class="reference"><a href="#cite_note-weight-63">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_64-0" class="reference"><a href="#cite_note-chance-64">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_65-0" class="reference"><a href="#cite_note-items-65">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_66-0" class="reference"><a href="#cite_note-chests-66">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Potato" title="Potato"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-224px -496px"></span><span class="sprite-text">Potato</span></a></td>
    <td style="text-align:center;" data-sort-value="4">1–7</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>43</sub></td><td style="text-align:center;">74.2%</td><td style="text-align:center;">5.116</td><td style="text-align:center;">1.3</td></tr>
    <tr>
    <td><a href="/wiki/Apple" title="Apple"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-48px -480px"></span><span class="sprite-text">Apple</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>43</sub></td><td style="text-align:center;">74.2%</td><td style="text-align:center;">3.837</td><td style="text-align:center;">1.3</td></tr>
    <tr>
    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>43</sub></td><td style="text-align:center;">74.2%</td><td style="text-align:center;">3.198</td><td style="text-align:center;">1.3</td></tr>
    <tr>
    <td><a href="/wiki/Sapling" title="Sapling"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-544px -464px"></span><span class="sprite-text">Oak Sapling</span></a></td>
    <td style="text-align:center;" data-sort-value="1.5">1–2</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>43</sub></td><td style="text-align:center;">48.2%</td><td style="text-align:center;">0.959</td><td style="text-align:center;">2.1</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>43</sub></td><td style="text-align:center;">22.8%</td><td style="text-align:center;">0.640</td><td style="text-align:center;">4.4</td></tr>
    <tr>
    <td><a href="/wiki/Flower" title="Flower"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-192px -560px"></span><span class="sprite-text">Dandelion</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>43</sub></td><td style="text-align:center;">22.8%</td><td style="text-align:center;">0.256</td><td style="text-align:center;">4.4</td></tr>
    <tr>
    <td><a href="/wiki/Gold_nugget" class="mw-redirect" title="Gold nugget"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-64px -560px"></span><span class="sprite-text">Gold Nugget</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>43</sub></td><td style="text-align:center;">12.1%</td><td style="text-align:center;">0.256</td><td style="text-align:center;">8.3</td></tr>
    <tr>
    <td><a href="/wiki/Book" title="Book"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-192px -528px"></span><span class="sprite-text">Book</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>43</sub></td><td style="text-align:center;">12.1%</td><td style="text-align:center;">0.128</td><td style="text-align:center;">8.3</td></tr>
    <tr>
    <td><a href="/wiki/Feather" title="Feather"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-240px -544px"></span><span class="sprite-text">Feather</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>43</sub></td><td style="text-align:center;">12.1%</td><td style="text-align:center;">0.128</td><td style="text-align:center;">8.3</td></tr>
    <tr>
    <td><a href="/wiki/Flower" title="Flower"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-304px -560px"></span><span class="sprite-text">Poppy</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>43</sub></td><td style="text-align:center;">12.1%</td><td style="text-align:center;">0.128</td><td style="text-align:center;">8.3</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <p>In <i><a href="/wiki/Bedrock_Edition" title="Bedrock Edition">Bedrock Edition</a></i>, each village plains house chest contains 3–8 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_62-1" class="reference"><a href="#cite_note-stacksize-62">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_63-1" class="reference"><a href="#cite_note-weight-63">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_64-1" class="reference"><a href="#cite_note-chance-64">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_65-1" class="reference"><a href="#cite_note-items-65">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_66-1" class="reference"><a href="#cite_note-chests-66">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Potato" title="Potato"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-224px -496px"></span><span class="sprite-text">Potato</span></a></td>
    <td style="text-align:center;" data-sort-value="4">1–7</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>43</sub></td><td style="text-align:center;">74.2%</td><td style="text-align:center;">5.116</td><td style="text-align:center;">1.3</td></tr>
    <tr>
    <td><a href="/wiki/Apple" title="Apple"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-48px -480px"></span><span class="sprite-text">Apple</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>43</sub></td><td style="text-align:center;">74.2%</td><td style="text-align:center;">3.837</td><td style="text-align:center;">1.3</td></tr>
    <tr>
    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>43</sub></td><td style="text-align:center;">74.2%</td><td style="text-align:center;">3.198</td><td style="text-align:center;">1.3</td></tr>
    <tr>
    <td><a href="/wiki/Sapling" title="Sapling"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-544px -464px"></span><span class="sprite-text">Oak Sapling</span></a></td>
    <td style="text-align:center;" data-sort-value="1.5">1–2</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>43</sub></td><td style="text-align:center;">48.2%</td><td style="text-align:center;">0.959</td><td style="text-align:center;">2.1</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>43</sub></td><td style="text-align:center;">22.8%</td><td style="text-align:center;">0.640</td><td style="text-align:center;">4.4</td></tr>
    <tr>
    <td><a href="/wiki/Flower" title="Flower"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-192px -560px"></span><span class="sprite-text">Dandelion</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>43</sub></td><td style="text-align:center;">22.8%</td><td style="text-align:center;">0.256</td><td style="text-align:center;">4.4</td></tr>
    <tr>
    <td><a href="/wiki/Gold_nugget" class="mw-redirect" title="Gold nugget"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-64px -560px"></span><span class="sprite-text">Gold Nugget</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>43</sub></td><td style="text-align:center;">12.1%</td><td style="text-align:center;">0.256</td><td style="text-align:center;">8.3</td></tr>
    <tr>
    <td><a href="/wiki/Book" title="Book"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-192px -528px"></span><span class="sprite-text">Book</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>43</sub></td><td style="text-align:center;">12.1%</td><td style="text-align:center;">0.128</td><td style="text-align:center;">8.3</td></tr>
    <tr>
    <td><a href="/wiki/Feather" title="Feather"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-240px -544px"></span><span class="sprite-text">Feather</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>43</sub></td><td style="text-align:center;">12.1%</td><td style="text-align:center;">0.128</td><td style="text-align:center;">8.3</td></tr>
    <tr>
    <td><a href="/wiki/Flower" title="Flower"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-304px -560px"></span><span class="sprite-text">Poppy</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>43</sub></td><td style="text-align:center;">12.1%</td><td style="text-align:center;">0.128</td><td style="text-align:center;">8.3</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <div class="mobileonly">
    <div class="reflist-upper-alpha"><div class="mw-references-wrap"><ol class="references">
    <li id="cite_note-stacksize-62"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-stacksize_62-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-stacksize_62-1">b</a></sup></span> <span class="reference-text">The size of stacks (or for unstackable items, number) of this item on any given roll.</span>
    </li>
    <li id="cite_note-weight-63"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-weight_63-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-weight_63-1">b</a></sup></span> <span class="reference-text">The weight of this item relative to other items in the pool.</span>
    </li>
    <li id="cite_note-chance-64"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chance_64-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chance_64-1">b</a></sup></span> <span class="reference-text">The odds of finding any of this item in a single chest.</span>
    </li>
    <li id="cite_note-items-65"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-items_65-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-items_65-1">b</a></sup></span> <span class="reference-text">The number of items expected per chest, averaged over a large number of chests.</span>
    </li>
    <li id="cite_note-chests-66"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chests_66-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chests_66-1">b</a></sup></span> <span class="reference-text">The average number of chests the player should expect to search to find any of this item.</span>
    </li>
    </ol></div></div>
    </div>
    <p><br>
    </p>
    <h3><span class="mw-headline" id="Savanna_House">Savanna House</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><span class="mw-editsection-bracket">]</span></span></h3>
    <p>In <i><a href="/wiki/Java_Edition" title="Java Edition">Java Edition</a></i>, each village savanna house chest contains 3–8 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_67-0" class="reference"><a href="#cite_note-stacksize-67">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_68-0" class="reference"><a href="#cite_note-weight-68">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_69-0" class="reference"><a href="#cite_note-chance-69">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_70-0" class="reference"><a href="#cite_note-items-70">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_71-0" class="reference"><a href="#cite_note-chests-71">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Wheat_seeds" class="mw-redirect" title="Wheat seeds"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-144px -0px"></span><span class="sprite-text">Wheat Seeds</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>46</sub></td><td style="text-align:center;">71.7%</td><td style="text-align:center;">3.587</td><td style="text-align:center;">1.4</td></tr>
    <tr>
    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>46</sub></td><td style="text-align:center;">71.7%</td><td style="text-align:center;">2.989</td><td style="text-align:center;">1.4</td></tr>
    <tr>
    <td><a href="/wiki/Sapling" title="Sapling"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-480px -464px"></span><span class="sprite-text">Acacia Sapling</span></a></td>
    <td style="text-align:center;" data-sort-value="1.5">1–2</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>46</sub></td><td style="text-align:center;">71.7%</td><td style="text-align:center;">1.793</td><td style="text-align:center;">1.4</td></tr>
    <tr>
    <td><a href="/wiki/Grass" title="Grass"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-48px -560px"></span><span class="sprite-text">Grass</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>46</sub></td><td style="text-align:center;">45.9%</td><td style="text-align:center;">0.598</td><td style="text-align:center;">2.2</td></tr>
    <tr>
    <td><a href="/wiki/Grass" title="Grass"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-112px -560px"></span><span class="sprite-text">Tall Grass</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>46</sub></td><td style="text-align:center;">45.9%</td><td style="text-align:center;">0.598</td><td style="text-align:center;">2.2</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>46</sub></td><td style="text-align:center;">21.5%</td><td style="text-align:center;">0.598</td><td style="text-align:center;">4.7</td></tr>
    <tr>
    <td><a href="/wiki/Gold_nugget" class="mw-redirect" title="Gold nugget"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-64px -560px"></span><span class="sprite-text">Gold Nugget</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>46</sub></td><td style="text-align:center;">11.3%</td><td style="text-align:center;">0.239</td><td style="text-align:center;">8.8</td></tr>
    <tr>
    <td><a href="/wiki/Torch" title="Torch"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-480px -512px"></span><span class="sprite-text">Torch</span></a></td>
    <td style="text-align:center;" data-sort-value="1.5">1–2</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>46</sub></td><td style="text-align:center;">11.3%</td><td style="text-align:center;">0.179</td><td style="text-align:center;">8.8</td></tr>
    <tr>
    <td><a href="/wiki/Bucket" title="Bucket"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-112px -448px"></span><span class="sprite-text">Bucket</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>46</sub></td><td style="text-align:center;">11.3%</td><td style="text-align:center;">0.120</td><td style="text-align:center;">8.8</td></tr>
    <tr>
    <td><a href="/wiki/Saddle" title="Saddle"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -528px"></span><span class="sprite-text">Saddle</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>46</sub></td><td style="text-align:center;">11.3%</td><td style="text-align:center;">0.120</td><td style="text-align:center;">8.8</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <p>In <i><a href="/wiki/Bedrock_Edition" title="Bedrock Edition">Bedrock Edition</a></i>, each village savanna house chest contains 3–8 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_67-1" class="reference"><a href="#cite_note-stacksize-67">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_68-1" class="reference"><a href="#cite_note-weight-68">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_69-1" class="reference"><a href="#cite_note-chance-69">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_70-1" class="reference"><a href="#cite_note-items-70">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_71-1" class="reference"><a href="#cite_note-chests-71">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Wheat_seeds" class="mw-redirect" title="Wheat seeds"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-144px -0px"></span><span class="sprite-text">Wheat Seeds</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>46</sub></td><td style="text-align:center;">71.7%</td><td style="text-align:center;">3.587</td><td style="text-align:center;">1.4</td></tr>
    <tr>
    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>46</sub></td><td style="text-align:center;">71.7%</td><td style="text-align:center;">2.989</td><td style="text-align:center;">1.4</td></tr>
    <tr>
    <td><a href="/wiki/Sapling" title="Sapling"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-480px -464px"></span><span class="sprite-text">Acacia Sapling</span></a></td>
    <td style="text-align:center;" data-sort-value="1.5">1–2</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>46</sub></td><td style="text-align:center;">71.7%</td><td style="text-align:center;">1.793</td><td style="text-align:center;">1.4</td></tr>
    <tr>
    <td><a href="/wiki/Grass" title="Grass"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-48px -560px"></span><span class="sprite-text">Grass</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>46</sub></td><td style="text-align:center;">45.9%</td><td style="text-align:center;">0.598</td><td style="text-align:center;">2.2</td></tr>
    <tr>
    <td><a href="/wiki/Grass" title="Grass"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-112px -560px"></span><span class="sprite-text">Tall Grass</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>46</sub></td><td style="text-align:center;">45.9%</td><td style="text-align:center;">0.598</td><td style="text-align:center;">2.2</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>46</sub></td><td style="text-align:center;">21.5%</td><td style="text-align:center;">0.598</td><td style="text-align:center;">4.7</td></tr>
    <tr>
    <td><a href="/wiki/Gold_nugget" class="mw-redirect" title="Gold nugget"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-64px -560px"></span><span class="sprite-text">Gold Nugget</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>46</sub></td><td style="text-align:center;">11.3%</td><td style="text-align:center;">0.239</td><td style="text-align:center;">8.8</td></tr>
    <tr>
    <td><a href="/wiki/Torch" title="Torch"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-480px -512px"></span><span class="sprite-text">Torch</span></a></td>
    <td style="text-align:center;" data-sort-value="1.5">1–2</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>46</sub></td><td style="text-align:center;">11.3%</td><td style="text-align:center;">0.179</td><td style="text-align:center;">8.8</td></tr>
    <tr>
    <td><a href="/wiki/Bucket" title="Bucket"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-112px -448px"></span><span class="sprite-text">Bucket</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>46</sub></td><td style="text-align:center;">11.3%</td><td style="text-align:center;">0.120</td><td style="text-align:center;">8.8</td></tr>
    <tr>
    <td><a href="/wiki/Saddle" title="Saddle"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -528px"></span><span class="sprite-text">Saddle</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>46</sub></td><td style="text-align:center;">11.3%</td><td style="text-align:center;">0.120</td><td style="text-align:center;">8.8</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <div class="mobileonly">
    <div class="reflist-upper-alpha"><div class="mw-references-wrap"><ol class="references">
    <li id="cite_note-stacksize-67"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-stacksize_67-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-stacksize_67-1">b</a></sup></span> <span class="reference-text">The size of stacks (or for unstackable items, number) of this item on any given roll.</span>
    </li>
    <li id="cite_note-weight-68"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-weight_68-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-weight_68-1">b</a></sup></span> <span class="reference-text">The weight of this item relative to other items in the pool.</span>
    </li>
    <li id="cite_note-chance-69"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chance_69-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chance_69-1">b</a></sup></span> <span class="reference-text">The odds of finding any of this item in a single chest.</span>
    </li>
    <li id="cite_note-items-70"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-items_70-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-items_70-1">b</a></sup></span> <span class="reference-text">The number of items expected per chest, averaged over a large number of chests.</span>
    </li>
    <li id="cite_note-chests-71"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chests_71-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chests_71-1">b</a></sup></span> <span class="reference-text">The average number of chests the player should expect to search to find any of this item.</span>
    </li>
    </ol></div></div>
    </div>
    <p><br>
    </p>
    <h3><span class="mw-headline" id="Snowy_House">Snowy House</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><span class="mw-editsection-bracket">]</span></span></h3>
    <p>In <i><a href="/wiki/Java_Edition" title="Java Edition">Java Edition</a></i>, each village snowy house chest contains 3–8 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_72-0" class="reference"><a href="#cite_note-stacksize-72">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_73-0" class="reference"><a href="#cite_note-weight-73">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_74-0" class="reference"><a href="#cite_note-chance-74">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_75-0" class="reference"><a href="#cite_note-items-75">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_76-0" class="reference"><a href="#cite_note-chests-76">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Potato" title="Potato"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-224px -496px"></span><span class="sprite-text">Potato</span></a></td>
    <td style="text-align:center;" data-sort-value="4">1–7</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>53</sub></td><td style="text-align:center;">66.3%</td><td style="text-align:center;">4.151</td><td style="text-align:center;">1.5</td></tr>
    <tr>
    <td><a href="/wiki/Snowball" title="Snowball"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-32px -448px"></span><span class="sprite-text">Snowball</span></a></td>
    <td style="text-align:center;" data-sort-value="4">1–7</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>53</sub></td><td style="text-align:center;">66.3%</td><td style="text-align:center;">4.151</td><td style="text-align:center;">1.5</td></tr>
    <tr>
    <td><a href="/wiki/Beetroot_seeds" class="mw-redirect" title="Beetroot seeds"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-144px -576px"></span><span class="sprite-text">Beetroot Seeds</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>53</sub></td><td style="text-align:center;">66.3%</td><td style="text-align:center;">3.113</td><td style="text-align:center;">1.5</td></tr>
    <tr>
    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>53</sub></td><td style="text-align:center;">66.3%</td><td style="text-align:center;">2.594</td><td style="text-align:center;">1.5</td></tr>
    <tr>
    <td><a href="/wiki/Coal" title="Coal"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-176px -544px"></span><span class="sprite-text">Coal</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>53</sub></td><td style="text-align:center;">41.2%</td><td style="text-align:center;">1.297</td><td style="text-align:center;">2.4</td></tr>
    <tr>
    <td><a href="/wiki/Snow_Block" title="Snow Block"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-544px -416px"></span><span class="sprite-text">Snow Block</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="4"><sup>4</sup>⁄<sub>53</sub></td><td style="text-align:center;">34.5%</td><td style="text-align:center;">0.415</td><td style="text-align:center;">2.9</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>53</sub></td><td style="text-align:center;">9.9%</td><td style="text-align:center;">0.259</td><td style="text-align:center;">10.1</td></tr>
    <tr>
    <td><a href="/wiki/Beetroot_soup" class="mw-redirect" title="Beetroot soup"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-112px -480px"></span><span class="sprite-text">Beetroot Soup</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>53</sub></td><td style="text-align:center;">9.9%</td><td style="text-align:center;">0.104</td><td style="text-align:center;">10.1</td></tr>
    <tr>
    <td><a href="/wiki/Blue_ice" class="mw-redirect" title="Blue ice"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-384px -256px"></span><span class="sprite-text">Blue Ice</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>53</sub></td><td style="text-align:center;">9.9%</td><td style="text-align:center;">0.104</td><td style="text-align:center;">10.1</td></tr>
    <tr>
    <td><a href="/wiki/Furnace" title="Furnace"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-400px -464px"></span><span class="sprite-text">Furnace</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>53</sub></td><td style="text-align:center;">9.9%</td><td style="text-align:center;">0.104</td><td style="text-align:center;">10.1</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <p>In <i><a href="/wiki/Bedrock_Edition" title="Bedrock Edition">Bedrock Edition</a></i>, each village snowy house chest contains 3–8 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_72-1" class="reference"><a href="#cite_note-stacksize-72">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_73-1" class="reference"><a href="#cite_note-weight-73">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_74-1" class="reference"><a href="#cite_note-chance-74">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_75-1" class="reference"><a href="#cite_note-items-75">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_76-1" class="reference"><a href="#cite_note-chests-76">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Potato" title="Potato"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-224px -496px"></span><span class="sprite-text">Potato</span></a></td>
    <td style="text-align:center;" data-sort-value="4">1–7</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>53</sub></td><td style="text-align:center;">66.3%</td><td style="text-align:center;">4.151</td><td style="text-align:center;">1.5</td></tr>
    <tr>
    <td><a href="/wiki/Snowball" title="Snowball"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-32px -448px"></span><span class="sprite-text">Snowball</span></a></td>
    <td style="text-align:center;" data-sort-value="4">1–7</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>53</sub></td><td style="text-align:center;">66.3%</td><td style="text-align:center;">4.151</td><td style="text-align:center;">1.5</td></tr>
    <tr>
    <td><a href="/wiki/Beetroot_seeds" class="mw-redirect" title="Beetroot seeds"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-144px -576px"></span><span class="sprite-text">Beetroot Seeds</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>53</sub></td><td style="text-align:center;">66.3%</td><td style="text-align:center;">3.113</td><td style="text-align:center;">1.5</td></tr>
    <tr>
    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>53</sub></td><td style="text-align:center;">66.3%</td><td style="text-align:center;">2.594</td><td style="text-align:center;">1.5</td></tr>
    <tr>
    <td><a href="/wiki/Coal" title="Coal"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-176px -544px"></span><span class="sprite-text">Coal</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>53</sub></td><td style="text-align:center;">41.2%</td><td style="text-align:center;">1.297</td><td style="text-align:center;">2.4</td></tr>
    <tr>
    <td><a href="/wiki/Snow_Block" title="Snow Block"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-544px -416px"></span><span class="sprite-text">Snow Block</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="4"><sup>4</sup>⁄<sub>53</sub></td><td style="text-align:center;">34.5%</td><td style="text-align:center;">0.415</td><td style="text-align:center;">2.9</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>53</sub></td><td style="text-align:center;">9.9%</td><td style="text-align:center;">0.259</td><td style="text-align:center;">10.1</td></tr>
    <tr>
    <td><a href="/wiki/Beetroot_soup" class="mw-redirect" title="Beetroot soup"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-112px -480px"></span><span class="sprite-text">Beetroot Soup</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>53</sub></td><td style="text-align:center;">9.9%</td><td style="text-align:center;">0.104</td><td style="text-align:center;">10.1</td></tr>
    <tr>
    <td><a href="/wiki/Blue_ice" class="mw-redirect" title="Blue ice"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-384px -256px"></span><span class="sprite-text">Blue Ice</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>53</sub></td><td style="text-align:center;">9.9%</td><td style="text-align:center;">0.104</td><td style="text-align:center;">10.1</td></tr>
    <tr>
    <td><a href="/wiki/Furnace" title="Furnace"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-400px -464px"></span><span class="sprite-text">Furnace</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>53</sub></td><td style="text-align:center;">9.9%</td><td style="text-align:center;">0.104</td><td style="text-align:center;">10.1</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <div class="mobileonly">
    <div class="reflist-upper-alpha"><div class="mw-references-wrap"><ol class="references">
    <li id="cite_note-stacksize-72"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-stacksize_72-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-stacksize_72-1">b</a></sup></span> <span class="reference-text">The size of stacks (or for unstackable items, number) of this item on any given roll.</span>
    </li>
    <li id="cite_note-weight-73"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-weight_73-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-weight_73-1">b</a></sup></span> <span class="reference-text">The weight of this item relative to other items in the pool.</span>
    </li>
    <li id="cite_note-chance-74"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chance_74-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chance_74-1">b</a></sup></span> <span class="reference-text">The odds of finding any of this item in a single chest.</span>
    </li>
    <li id="cite_note-items-75"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-items_75-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-items_75-1">b</a></sup></span> <span class="reference-text">The number of items expected per chest, averaged over a large number of chests.</span>
    </li>
    <li id="cite_note-chests-76"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chests_76-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chests_76-1">b</a></sup></span> <span class="reference-text">The average number of chests the player should expect to search to find any of this item.</span>
    </li>
    </ol></div></div>
    </div>
    <p><br>
    </p>
    <h3><span class="mw-headline" id="Taiga_House">Taiga House</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><span class="mw-editsection-bracket">]</span></span></h3>
    <p>In <i><a href="/wiki/Java_Edition" title="Java Edition">Java Edition</a></i>, each village taiga house chest contains 3–8 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_77-0" class="reference"><a href="#cite_note-stacksize-77">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_78-0" class="reference"><a href="#cite_note-weight-78">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_79-0" class="reference"><a href="#cite_note-chance-79">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_80-0" class="reference"><a href="#cite_note-items-80">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_81-0" class="reference"><a href="#cite_note-chests-81">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Potato" title="Potato"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-224px -496px"></span><span class="sprite-text">Potato</span></a></td>
    <td style="text-align:center;" data-sort-value="4">1–7</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>54</sub></td><td style="text-align:center;">65.6%</td><td style="text-align:center;">4.074</td><td style="text-align:center;">1.5</td></tr>
    <tr>
    <td><a href="/wiki/Log" title="Log"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-160px -432px"></span><span class="sprite-text">Spruce Log</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>54</sub></td><td style="text-align:center;">65.6%</td><td style="text-align:center;">3.056</td><td style="text-align:center;">1.5</td></tr>
    <tr>
    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>54</sub></td><td style="text-align:center;">65.6%</td><td style="text-align:center;">2.546</td><td style="text-align:center;">1.5</td></tr>
    <tr>
    <td><a href="/wiki/Sweet_berries" class="mw-redirect" title="Sweet berries"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-96px -384px"></span><span class="sprite-text">Sweet Berries</span></a></td>
    <td style="text-align:center;" data-sort-value="4">1–7</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>54</sub></td><td style="text-align:center;">40.6%</td><td style="text-align:center;">2.037</td><td style="text-align:center;">2.5</td></tr>
    <tr>
    <td><a href="/wiki/Pumpkin_seeds" class="mw-redirect" title="Pumpkin seeds"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -48px"></span><span class="sprite-text">Pumpkin Seeds</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>54</sub></td><td style="text-align:center;">40.6%</td><td style="text-align:center;">1.528</td><td style="text-align:center;">2.5</td></tr>
    <tr>
    <td><a href="/wiki/Sapling" title="Sapling"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-560px -464px"></span><span class="sprite-text">Spruce Sapling</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>54</sub></td><td style="text-align:center;">40.6%</td><td style="text-align:center;">1.528</td><td style="text-align:center;">2.5</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>54</sub></td><td style="text-align:center;">18.6%</td><td style="text-align:center;">0.509</td><td style="text-align:center;">5.4</td></tr>
    <tr>
    <td><a href="/wiki/Grass" title="Grass"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-32px -560px"></span><span class="sprite-text">Fern</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>54</sub></td><td style="text-align:center;">18.6%</td><td style="text-align:center;">0.204</td><td style="text-align:center;">5.4</td></tr>
    <tr>
    <td><a href="/wiki/Grass" title="Grass"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-64px -560px"></span><span class="sprite-text">Large Fern</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>54</sub></td><td style="text-align:center;">18.6%</td><td style="text-align:center;">0.204</td><td style="text-align:center;">5.4</td></tr>
    <tr>
    <td><a href="/wiki/Iron_nugget" class="mw-redirect" title="Iron nugget"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-240px -272px"></span><span class="sprite-text">Iron Nugget</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>54</sub></td><td style="text-align:center;">9.7%</td><td style="text-align:center;">0.306</td><td style="text-align:center;">10.3</td></tr>
    <tr>
    <td><a href="/wiki/Pumpkin_pie" class="mw-redirect" title="Pumpkin pie"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-240px -496px"></span><span class="sprite-text">Pumpkin Pie</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>54</sub></td><td style="text-align:center;">9.7%</td><td style="text-align:center;">0.102</td><td style="text-align:center;">10.3</td></tr>
    <tr>
    <td><a href="/wiki/Sign" title="Sign"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-16px -896px"></span><span class="sprite-text">Spruce Sign</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>54</sub></td><td style="text-align:center;">9.7%</td><td style="text-align:center;">0.102</td><td style="text-align:center;">10.3</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <p>In <i><a href="/wiki/Bedrock_Edition" title="Bedrock Edition">Bedrock Edition</a></i>, each village taiga house chest contains 3–8 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_77-1" class="reference"><a href="#cite_note-stacksize-77">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_78-1" class="reference"><a href="#cite_note-weight-78">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_79-1" class="reference"><a href="#cite_note-chance-79">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_80-1" class="reference"><a href="#cite_note-items-80">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_81-1" class="reference"><a href="#cite_note-chests-81">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Potato" title="Potato"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-224px -496px"></span><span class="sprite-text">Potato</span></a></td>
    <td style="text-align:center;" data-sort-value="4">1–7</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>49</sub></td><td style="text-align:center;">69.3%</td><td style="text-align:center;">4.490</td><td style="text-align:center;">1.4</td></tr>
    <tr>
    <td><a href="/wiki/Log" title="Log"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-160px -432px"></span><span class="sprite-text">Spruce Log</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>49</sub></td><td style="text-align:center;">69.3%</td><td style="text-align:center;">3.367</td><td style="text-align:center;">1.4</td></tr>
    <tr>
    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>49</sub></td><td style="text-align:center;">69.3%</td><td style="text-align:center;">2.806</td><td style="text-align:center;">1.4</td></tr>
    <tr>
    <td><a href="/wiki/Pumpkin_seeds" class="mw-redirect" title="Pumpkin seeds"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -48px"></span><span class="sprite-text">Pumpkin Seeds</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>49</sub></td><td style="text-align:center;">43.7%</td><td style="text-align:center;">1.684</td><td style="text-align:center;">2.3</td></tr>
    <tr>
    <td><a href="/wiki/Sapling" title="Sapling"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-560px -464px"></span><span class="sprite-text">Spruce Sapling</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>49</sub></td><td style="text-align:center;">43.7%</td><td style="text-align:center;">1.684</td><td style="text-align:center;">2.3</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>49</sub></td><td style="text-align:center;">20.3%</td><td style="text-align:center;">0.561</td><td style="text-align:center;">4.9</td></tr>
    <tr>
    <td><a href="/wiki/Grass" title="Grass"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-32px -560px"></span><span class="sprite-text">Fern</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>49</sub></td><td style="text-align:center;">20.3%</td><td style="text-align:center;">0.224</td><td style="text-align:center;">4.9</td></tr>
    <tr>
    <td><a href="/wiki/Grass" title="Grass"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-64px -560px"></span><span class="sprite-text">Large Fern</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>49</sub></td><td style="text-align:center;">20.3%</td><td style="text-align:center;">0.224</td><td style="text-align:center;">4.9</td></tr>
    <tr>
    <td><a href="/wiki/Iron_nugget" class="mw-redirect" title="Iron nugget"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-240px -272px"></span><span class="sprite-text">Iron Nugget</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>49</sub></td><td style="text-align:center;">10.7%</td><td style="text-align:center;">0.337</td><td style="text-align:center;">9.4</td></tr>
    <tr>
    <td><a href="/wiki/Sign" title="Sign"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-240px -880px"></span><span class="sprite-text">Oak Sign</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>49</sub></td><td style="text-align:center;">10.7%</td><td style="text-align:center;">0.112</td><td style="text-align:center;">9.4</td></tr>
    <tr>
    <td><a href="/wiki/Pumpkin_pie" class="mw-redirect" title="Pumpkin pie"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-240px -496px"></span><span class="sprite-text">Pumpkin Pie</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>49</sub></td><td style="text-align:center;">10.7%</td><td style="text-align:center;">0.112</td><td style="text-align:center;">9.4</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <div class="mobileonly">
    <div class="reflist-upper-alpha"><div class="mw-references-wrap"><ol class="references">
    <li id="cite_note-stacksize-77"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-stacksize_77-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-stacksize_77-1">b</a></sup></span> <span class="reference-text">The size of stacks (or for unstackable items, number) of this item on any given roll.</span>
    </li>
    <li id="cite_note-weight-78"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-weight_78-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-weight_78-1">b</a></sup></span> <span class="reference-text">The weight of this item relative to other items in the pool.</span>
    </li>
    <li id="cite_note-chance-79"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chance_79-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chance_79-1">b</a></sup></span> <span class="reference-text">The odds of finding any of this item in a single chest.</span>
    </li>
    <li id="cite_note-items-80"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-items_80-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-items_80-1">b</a></sup></span> <span class="reference-text">The number of items expected per chest, averaged over a large number of chests.</span>
    </li>
    <li id="cite_note-chests-81"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chests_81-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chests_81-1">b</a></sup></span> <span class="reference-text">The average number of chests the player should expect to search to find any of this item.</span>
    </li>
    </ol></div></div>
    </div>
    <p><br>
    </p>
    <!--
    NewPP limit report
    Cached time: 20240413133705
    Cache expiry: 1209600
    Reduced expiry: false
    Complications: [show‐toc]
    CPU time usage: 0.508 seconds
    Real time usage: 0.539 seconds
    Preprocessor visited node count: 4858/1000000
    Post‐expand include size: 708776/2097152 bytes
    Template argument size: 756/2097152 bytes
    Highest expansion depth: 13/100
    Expensive parser function count: 2/100
    Unstrip recursion depth: 0/20
    Unstrip post‐expand size: 39836/5000000 bytes
    Lua time usage: 0.252/7.000 seconds
    Lua memory usage: 6332780/104857600 bytes
    ExtLoops count: 0/200
    -->
    <!--
    Transclusion expansion time report (%,ms,calls,template)
    100.00%  295.562      1 Village/Loot
    100.00%  295.562      1 -total
    96.33%  284.715     16 Template:LootChest
    1.93%    5.702      1 Template:In
    1.44%    4.266      1 Template:Editions
    -->
    </div></div>
    </div>"""),
        ('https://minecraft.fandom.com/wiki/Village#Abandoned_villages', [0,2,4,5,6,8,9,11,13,15,17,19,21,23,25,27], """<div class="load-page pageloader-contentloaded" data-page="Village/Loot">
    <h3><span class="mw-headline" id="Loot">Loot</span><span class="mw-editsection-like load-page-button" style="min-width: 58px;">[<span class="jslink">hide</span>]</span><span class="mw-editsection-like" title="Edit: Village/Loot">[<a target="_self" class="text" href="https://minecraft.fandom.com/wiki/Village/Loot?action=edit">edit</a>]</span></h3>
    <div class="load-page-content" style=""><div class="mw-parser-output"><figure class="thumb tright show-info-icon" style="width: 180px"> 	<a href="https://static.wikia.nocookie.net/minecraft_gamepedia/images/2/2c/Villagechest.png/revision/latest?cb=20220728020643" class="image"><img alt="Villagechest" src="https://static.wikia.nocookie.net/minecraft_gamepedia/images/2/2c/Villagechest.png/revision/latest/scale-to-width-down/180?cb=20220728020643" decoding="async" loading="lazy" width="180" height="98" class="thumbimage" data-image-name="Villagechest.png" data-image-key="Villagechest.png" data-relevant="1"></a> 	 	<figcaption class="thumbcaption"> 		 			<a href="/wiki/File:Villagechest.png" class="info-icon"><svg><use xlink:href="#wds-icons-info-small"></use></svg></a> 		 		 		 			<p class="caption">Typical blacksmith loot from a village before 1.14.</p> 		 	</figcaption> </figure>
    <figure class="thumb tright show-info-icon" style="width: 180px"> 	<a href="https://static.wikia.nocookie.net/minecraft_gamepedia/images/a/ae/Loot_in_Village_Desert_Temple_1.png/revision/latest?cb=20210612173304" class="image"><img alt="Loot in Village Desert Temple 1" src="https://static.wikia.nocookie.net/minecraft_gamepedia/images/a/ae/Loot_in_Village_Desert_Temple_1.png/revision/latest/scale-to-width-down/180?cb=20210612173304" decoding="async" loading="lazy" width="180" height="93" class="thumbimage" data-image-name="Loot in Village Desert Temple 1.png" data-image-key="Loot_in_Village_Desert_Temple_1.png" data-relevant="1"></a> 	 	<figcaption class="thumbcaption"> 		 			<a href="/wiki/File:Loot_in_Village_Desert_Temple_1.png" class="info-icon"><svg><use xlink:href="#wds-icons-info-small"></use></svg></a> 		 		 		 			<p class="caption">A chest loot from a 1.14 village desert temple, the village desert temple has the rarest chance of generating in a desert village in Bedrock Edition.</p> 		 	</figcaption> </figure>
    <div id="toc" class="toc" role="navigation" aria-labelledby="mw-toc-heading"><input type="checkbox" role="button" id="toctogglecheckbox" class="toctogglecheckbox" style="display:none"><div class="toctitle" lang="en" dir="ltr"><h2 id="mw-toc-heading">Contents</h2><span class="toctogglespan"><label class="toctogglelabel" for="toctogglecheckbox"></label></span></div>
    <ul>
    <li class="toclevel-1"><a href="#Armorer_House"><span class="tocnumber">1</span> <span class="toctext">Armorer House</span></a></li>
    <li class="toclevel-1"><a href="#Butcher_Shop"><span class="tocnumber">2</span> <span class="toctext">Butcher Shop</span></a></li>
    <li class="toclevel-1"><a href="#Cartographer_House"><span class="tocnumber">3</span> <span class="toctext">Cartographer House</span></a></li>
    <li class="toclevel-1"><a href="#Fisher_Cottage"><span class="tocnumber">4</span> <span class="toctext">Fisher Cottage</span></a></li>
    <li class="toclevel-1"><a href="#Fletcher_House"><span class="tocnumber">5</span> <span class="toctext">Fletcher House</span></a></li>
    <li class="toclevel-1"><a href="#Mason_House"><span class="tocnumber">6</span> <span class="toctext">Mason House</span></a></li>
    <li class="toclevel-1"><a href="#Shepherd_House"><span class="tocnumber">7</span> <span class="toctext">Shepherd House</span></a></li>
    <li class="toclevel-1"><a href="#Tannery"><span class="tocnumber">8</span> <span class="toctext">Tannery</span></a></li>
    <li class="toclevel-1"><a href="#Temple"><span class="tocnumber">9</span> <span class="toctext">Temple</span></a></li>
    <li class="toclevel-1"><a href="#Toolsmith"><span class="tocnumber">10</span> <span class="toctext">Toolsmith</span></a></li>
    <li class="toclevel-1"><a href="#Weaponsmith"><span class="tocnumber">11</span> <span class="toctext">Weaponsmith</span></a></li>
    <li class="toclevel-1"><a href="#Desert_House"><span class="tocnumber">12</span> <span class="toctext">Desert House</span></a></li>
    <li class="toclevel-1"><a href="#Plain_House"><span class="tocnumber">13</span> <span class="toctext">Plain House</span></a></li>
    <li class="toclevel-1"><a href="#Savanna_House"><span class="tocnumber">14</span> <span class="toctext">Savanna House</span></a></li>
    <li class="toclevel-1"><a href="#Snowy_House"><span class="tocnumber">15</span> <span class="toctext">Snowy House</span></a></li>
    <li class="toclevel-1"><a href="#Taiga_House"><span class="tocnumber">16</span> <span class="toctext">Taiga House</span></a></li>
    </ul>
    </div>

    <h3><span class="mw-headline" id="Armorer_House">Armorer House</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><span class="mw-editsection-bracket">]</span></span></h3>
    <p>Only one of the armorer house variants in snowy villages contain chests.
    </p><p>In <i><a href="/wiki/Java_Edition" title="Java Edition">Java Edition</a></i>, each village armorer chest contains 1–5 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_1-0" class="reference"><a href="#cite_note-stacksize-1">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_2-0" class="reference"><a href="#cite_note-weight-2">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_3-0" class="reference"><a href="#cite_note-chance-3">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_4-0" class="reference"><a href="#cite_note-items-4">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_5-0" class="reference"><a href="#cite_note-chests-5">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="4"><sup>4</sup>⁄<sub>8</sub></td><td style="text-align:center;">80.6%</td><td style="text-align:center;">3.750</td><td style="text-align:center;">1.2</td></tr>
    <tr>
    <td><a href="/wiki/Iron_ingot" class="mw-redirect" title="Iron ingot"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-112px -560px"></span><span class="sprite-text">Iron Ingot</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>8</sub></td><td style="text-align:center;">54.2%</td><td style="text-align:center;">1.500</td><td style="text-align:center;">1.8</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>8</sub></td><td style="text-align:center;">31.8%</td><td style="text-align:center;">0.375</td><td style="text-align:center;">3.1</td></tr>
    <tr>
    <td><a href="/wiki/Armor" title="Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -416px"></span><span class="sprite-text">Iron Helmet</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>8</sub></td><td style="text-align:center;">31.8%</td><td style="text-align:center;">0.375</td><td style="text-align:center;">3.1</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <p>In <i><a href="/wiki/Bedrock_Edition" title="Bedrock Edition">Bedrock Edition</a></i>, each village armorer chest contains 1–5 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_1-1" class="reference"><a href="#cite_note-stacksize-1">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_2-1" class="reference"><a href="#cite_note-weight-2">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_3-1" class="reference"><a href="#cite_note-chance-3">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_4-1" class="reference"><a href="#cite_note-items-4">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_5-1" class="reference"><a href="#cite_note-chests-5">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="4"><sup>4</sup>⁄<sub>8</sub></td><td style="text-align:center;">80.6%</td><td style="text-align:center;">3.750</td><td style="text-align:center;">1.2</td></tr>
    <tr>
    <td><a href="/wiki/Iron_ingot" class="mw-redirect" title="Iron ingot"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-112px -560px"></span><span class="sprite-text">Iron Ingot</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>8</sub></td><td style="text-align:center;">54.2%</td><td style="text-align:center;">1.500</td><td style="text-align:center;">1.8</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>8</sub></td><td style="text-align:center;">31.8%</td><td style="text-align:center;">0.375</td><td style="text-align:center;">3.1</td></tr>
    <tr>
    <td><a href="/wiki/Armor" title="Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -416px"></span><span class="sprite-text">Iron Helmet</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>8</sub></td><td style="text-align:center;">31.8%</td><td style="text-align:center;">0.375</td><td style="text-align:center;">3.1</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <div class="mobileonly">
    <div class="reflist-upper-alpha"><div class="mw-references-wrap"><ol class="references">
    <li id="cite_note-stacksize-1"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-stacksize_1-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-stacksize_1-1">b</a></sup></span> <span class="reference-text">The size of stacks (or for unstackable items, number) of this item on any given roll.</span>
    </li>
    <li id="cite_note-weight-2"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-weight_2-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-weight_2-1">b</a></sup></span> <span class="reference-text">The weight of this item relative to other items in the pool.</span>
    </li>
    <li id="cite_note-chance-3"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chance_3-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chance_3-1">b</a></sup></span> <span class="reference-text">The odds of finding any of this item in a single chest.</span>
    </li>
    <li id="cite_note-items-4"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-items_4-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-items_4-1">b</a></sup></span> <span class="reference-text">The number of items expected per chest, averaged over a large number of chests.</span>
    </li>
    <li id="cite_note-chests-5"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chests_5-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chests_5-1">b</a></sup></span> <span class="reference-text">The average number of chests the player should expect to search to find any of this item.</span>
    </li>
    </ol></div></div>
    </div>
    <p><br>
    </p>
    <h3><span class="mw-headline" id="Butcher_Shop">Butcher Shop</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><span class="mw-editsection-bracket">]</span></span></h3>
    <p>Only butcher shops in savanna villages contain chests.
    </p><p>In <i><a href="/wiki/Java_Edition" title="Java Edition">Java Edition</a></i>, each village butcher chest contains 1–5 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_6-0" class="reference"><a href="#cite_note-stacksize-6">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_7-0" class="reference"><a href="#cite_note-weight-7">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_8-0" class="reference"><a href="#cite_note-chance-8">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_9-0" class="reference"><a href="#cite_note-items-9">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_10-0" class="reference"><a href="#cite_note-chests-10">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Raw_Beef" title="Raw Beef"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -480px"></span><span class="sprite-text">Raw Beef</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="6"><sup>6</sup>⁄<sub>28</sub></td><td style="text-align:center;">48.6%</td><td style="text-align:center;">1.286</td><td style="text-align:center;">2.1</td></tr>
    <tr>
    <td><a href="/wiki/Raw_Mutton" title="Raw Mutton"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-160px -496px"></span><span class="sprite-text">Raw Mutton</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="6"><sup>6</sup>⁄<sub>28</sub></td><td style="text-align:center;">48.6%</td><td style="text-align:center;">1.286</td><td style="text-align:center;">2.1</td></tr>
    <tr>
    <td><a href="/wiki/Raw_Porkchop" title="Raw Porkchop"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -496px"></span><span class="sprite-text">Raw Porkchop</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="6"><sup>6</sup>⁄<sub>28</sub></td><td style="text-align:center;">48.6%</td><td style="text-align:center;">1.286</td><td style="text-align:center;">2.1</td></tr>
    <tr>
    <td><a href="/wiki/Wheat" title="Wheat"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-192px -576px"></span><span class="sprite-text">Wheat</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="6"><sup>6</sup>⁄<sub>28</sub></td><td style="text-align:center;">48.6%</td><td style="text-align:center;">1.286</td><td style="text-align:center;">2.1</td></tr>
    <tr>
    <td><a href="/wiki/Coal" title="Coal"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-176px -544px"></span><span class="sprite-text">Coal</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="3"><sup>3</sup>⁄<sub>28</sub></td><td style="text-align:center;">27.9%</td><td style="text-align:center;">0.643</td><td style="text-align:center;">3.6</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>28</sub></td><td style="text-align:center;">10.2%</td><td style="text-align:center;">0.107</td><td style="text-align:center;">9.8</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <p>In <i><a href="/wiki/Bedrock_Edition" title="Bedrock Edition">Bedrock Edition</a></i>, each village butcher chest contains 1–5 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_6-1" class="reference"><a href="#cite_note-stacksize-6">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_7-1" class="reference"><a href="#cite_note-weight-7">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_8-1" class="reference"><a href="#cite_note-chance-8">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_9-1" class="reference"><a href="#cite_note-items-9">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_10-1" class="reference"><a href="#cite_note-chests-10">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Raw_Beef" title="Raw Beef"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -480px"></span><span class="sprite-text">Raw Beef</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="6"><sup>6</sup>⁄<sub>28</sub></td><td style="text-align:center;">48.6%</td><td style="text-align:center;">1.286</td><td style="text-align:center;">2.1</td></tr>
    <tr>
    <td><a href="/wiki/Raw_Mutton" title="Raw Mutton"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-160px -496px"></span><span class="sprite-text">Raw Mutton</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="6"><sup>6</sup>⁄<sub>28</sub></td><td style="text-align:center;">48.6%</td><td style="text-align:center;">1.286</td><td style="text-align:center;">2.1</td></tr>
    <tr>
    <td><a href="/wiki/Raw_Porkchop" title="Raw Porkchop"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -496px"></span><span class="sprite-text">Raw Porkchop</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="6"><sup>6</sup>⁄<sub>28</sub></td><td style="text-align:center;">48.6%</td><td style="text-align:center;">1.286</td><td style="text-align:center;">2.1</td></tr>
    <tr>
    <td><a href="/wiki/Wheat" title="Wheat"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-192px -576px"></span><span class="sprite-text">Wheat</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="6"><sup>6</sup>⁄<sub>28</sub></td><td style="text-align:center;">48.6%</td><td style="text-align:center;">1.286</td><td style="text-align:center;">2.1</td></tr>
    <tr>
    <td><a href="/wiki/Coal" title="Coal"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-176px -544px"></span><span class="sprite-text">Coal</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="3"><sup>3</sup>⁄<sub>28</sub></td><td style="text-align:center;">27.9%</td><td style="text-align:center;">0.643</td><td style="text-align:center;">3.6</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>28</sub></td><td style="text-align:center;">10.2%</td><td style="text-align:center;">0.107</td><td style="text-align:center;">9.8</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <div class="mobileonly">
    <div class="reflist-upper-alpha"><div class="mw-references-wrap"><ol class="references">
    <li id="cite_note-stacksize-6"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-stacksize_6-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-stacksize_6-1">b</a></sup></span> <span class="reference-text">The size of stacks (or for unstackable items, number) of this item on any given roll.</span>
    </li>
    <li id="cite_note-weight-7"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-weight_7-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-weight_7-1">b</a></sup></span> <span class="reference-text">The weight of this item relative to other items in the pool.</span>
    </li>
    <li id="cite_note-chance-8"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chance_8-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chance_8-1">b</a></sup></span> <span class="reference-text">The odds of finding any of this item in a single chest.</span>
    </li>
    <li id="cite_note-items-9"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-items_9-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-items_9-1">b</a></sup></span> <span class="reference-text">The number of items expected per chest, averaged over a large number of chests.</span>
    </li>
    <li id="cite_note-chests-10"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chests_10-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chests_10-1">b</a></sup></span> <span class="reference-text">The average number of chests the player should expect to search to find any of this item.</span>
    </li>
    </ol></div></div>
    </div>
    <p><br>
    </p>
    <h3><span class="mw-headline" id="Cartographer_House">Cartographer House</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><span class="mw-editsection-bracket">]</span></span></h3>
    <p>All cartographer houses except those in desert villages contain chests.
    </p><p>In <i><a href="/wiki/Java_Edition" title="Java Edition">Java Edition</a></i>, each village cartographer chest contains 1–5 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_11-0" class="reference"><a href="#cite_note-stacksize-11">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_12-0" class="reference"><a href="#cite_note-weight-12">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_13-0" class="reference"><a href="#cite_note-chance-13">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_14-0" class="reference"><a href="#cite_note-items-14">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_15-0" class="reference"><a href="#cite_note-chests-15">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Paper" title="Paper"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-96px -544px"></span><span class="sprite-text">Paper</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="15"><sup>15</sup>⁄<sub>50</sub></td><td style="text-align:center;">61.2%</td><td style="text-align:center;">2.700</td><td style="text-align:center;">1.6</td></tr>
    <tr>
    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="15"><sup>15</sup>⁄<sub>50</sub></td><td style="text-align:center;">61.2%</td><td style="text-align:center;">2.250</td><td style="text-align:center;">1.6</td></tr>
    <tr>
    <td><a href="/wiki/Map" title="Map"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -528px"></span><span class="sprite-text">Empty Map</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>50</sub></td><td style="text-align:center;">46.2%</td><td style="text-align:center;">1.200</td><td style="text-align:center;">2.2</td></tr>
    <tr>
    <td><a href="/wiki/Stick" title="Stick"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -48px"></span><span class="sprite-text">Stick</span></a></td>
    <td style="text-align:center;" data-sort-value="1.5">1–2</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>50</sub></td><td style="text-align:center;">26.3%</td><td style="text-align:center;">0.450</td><td style="text-align:center;">3.8</td></tr>
    <tr>
    <td><a href="/wiki/Compass" title="Compass"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-32px -880px"></span><span class="sprite-text">Compass</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>50</sub></td><td style="text-align:center;">26.3%</td><td style="text-align:center;">0.300</td><td style="text-align:center;">3.8</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <p>In <i><a href="/wiki/Bedrock_Edition" title="Bedrock Edition">Bedrock Edition</a></i>, each village cartographer chest contains 1–5 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_11-1" class="reference"><a href="#cite_note-stacksize-11">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_12-1" class="reference"><a href="#cite_note-weight-12">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_13-1" class="reference"><a href="#cite_note-chance-13">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_14-1" class="reference"><a href="#cite_note-items-14">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_15-1" class="reference"><a href="#cite_note-chests-15">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Paper" title="Paper"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-96px -544px"></span><span class="sprite-text">Paper</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="15"><sup>15</sup>⁄<sub>50</sub></td><td style="text-align:center;">61.2%</td><td style="text-align:center;">2.700</td><td style="text-align:center;">1.6</td></tr>
    <tr>
    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="15"><sup>15</sup>⁄<sub>50</sub></td><td style="text-align:center;">61.2%</td><td style="text-align:center;">2.250</td><td style="text-align:center;">1.6</td></tr>
    <tr>
    <td><a href="/wiki/Map" title="Map"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-112px -528px"></span><span class="sprite-text">Map</span></a><sup id="cite_ref-map_16-0" class="reference"><a href="#cite_note-map-16">[F]</a></sup></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>50</sub></td><td style="text-align:center;">46.2%</td><td style="text-align:center;">1.200</td><td style="text-align:center;">2.2</td></tr>
    <tr>
    <td><a href="/wiki/Sapling" title="Sapling"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-544px -464px"></span><span class="sprite-text">Oak Sapling</span></a></td>
    <td style="text-align:center;" data-sort-value="1.5">1–2</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>50</sub></td><td style="text-align:center;">26.3%</td><td style="text-align:center;">0.450</td><td style="text-align:center;">3.8</td></tr>
    <tr>
    <td><a href="/wiki/Compass" title="Compass"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-32px -880px"></span><span class="sprite-text">Compass</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>50</sub></td><td style="text-align:center;">26.3%</td><td style="text-align:center;">0.300</td><td style="text-align:center;">3.8</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <div class="mobileonly">
    <div class="reflist-upper-alpha"><div class="mw-references-wrap"><ol class="references">
    <li id="cite_note-stacksize-11"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-stacksize_11-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-stacksize_11-1">b</a></sup></span> <span class="reference-text">The size of stacks (or for unstackable items, number) of this item on any given roll.</span>
    </li>
    <li id="cite_note-weight-12"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-weight_12-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-weight_12-1">b</a></sup></span> <span class="reference-text">The weight of this item relative to other items in the pool.</span>
    </li>
    <li id="cite_note-chance-13"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chance_13-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chance_13-1">b</a></sup></span> <span class="reference-text">The odds of finding any of this item in a single chest.</span>
    </li>
    <li id="cite_note-items-14"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-items_14-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-items_14-1">b</a></sup></span> <span class="reference-text">The number of items expected per chest, averaged over a large number of chests.</span>
    </li>
    <li id="cite_note-chests-15"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chests_15-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chests_15-1">b</a></sup></span> <span class="reference-text">The average number of chests the player should expect to search to find any of this item.</span>
    </li>
    <li id="cite_note-map-16"><span class="mw-cite-backlink"><a href="#cite_ref-map_16-0" aria-label="Jump up" title="Jump up">↑</a></span> <span class="reference-text">Named unknown map, but changed to map 0, the scale level is 1:4, Maps from the same stack are stackable, but maps that are not stacked are unstackable despite looking identical.</span>
    </li>
    </ol></div></div>
    </div>
    <p><br>
    </p>
    <h3><span class="mw-headline" id="Fisher_Cottage">Fisher Cottage</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><span class="mw-editsection-bracket">]</span></span></h3>
    <p>Only fisher cottages in plains villages in <a href="/wiki/Java_Edition" title="Java Edition"><i>Java Edition</i></a> contain chests.
    </p><p>In <i><a href="/wiki/Java_Edition" title="Java Edition">Java Edition</a></i>, each village fisherman chest contains 1–5 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_17-0" class="reference"><a href="#cite_note-stacksize-17">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_18-0" class="reference"><a href="#cite_note-weight-18">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_19-0" class="reference"><a href="#cite_note-chance-19">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_20-0" class="reference"><a href="#cite_note-items-20">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_21-0" class="reference"><a href="#cite_note-chests-21">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Wheat_seeds" class="mw-redirect" title="Wheat seeds"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-144px -0px"></span><span class="sprite-text">Wheat Seeds</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="3"><sup>3</sup>⁄<sub>11</sub></td><td style="text-align:center;">57.5%</td><td style="text-align:center;">1.636</td><td style="text-align:center;">1.7</td></tr>
    <tr>
    <td><a href="/wiki/Coal" title="Coal"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-176px -544px"></span><span class="sprite-text">Coal</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>11</sub></td><td style="text-align:center;">43.0%</td><td style="text-align:center;">1.091</td><td style="text-align:center;">2.3</td></tr>
    <tr>
    <td><a href="/wiki/Raw_Cod" title="Raw Cod"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-240px -320px"></span><span class="sprite-text">Raw Cod</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>11</sub></td><td style="text-align:center;">43.0%</td><td style="text-align:center;">1.091</td><td style="text-align:center;">2.3</td></tr>
    <tr>
    <td><a href="/wiki/Barrel" title="Barrel"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-48px -336px"></span><span class="sprite-text">Barrel</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>11</sub></td><td style="text-align:center;">24.2%</td><td style="text-align:center;">0.545</td><td style="text-align:center;">4.1</td></tr>
    <tr>
    <td><a href="/wiki/Raw_Salmon" title="Raw Salmon"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-192px -336px"></span><span class="sprite-text">Raw Salmon</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>11</sub></td><td style="text-align:center;">24.2%</td><td style="text-align:center;">0.545</td><td style="text-align:center;">4.1</td></tr>
    <tr>
    <td><a href="/wiki/Water_bucket" class="mw-redirect" title="Water bucket"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-224px -464px"></span><span class="sprite-text">Water Bucket</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>11</sub></td><td style="text-align:center;">24.2%</td><td style="text-align:center;">0.545</td><td style="text-align:center;">4.1</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>11</sub></td><td style="text-align:center;">24.2%</td><td style="text-align:center;">0.273</td><td style="text-align:center;">4.1</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <div class="mobileonly">
    <div class="reflist-upper-alpha"><div class="mw-references-wrap"><ol class="references">
    <li id="cite_note-stacksize-17"><span class="mw-cite-backlink"><a href="#cite_ref-stacksize_17-0" aria-label="Jump up" title="Jump up">↑</a></span> <span class="reference-text">The size of stacks (or for unstackable items, number) of this item on any given roll.</span>
    </li>
    <li id="cite_note-weight-18"><span class="mw-cite-backlink"><a href="#cite_ref-weight_18-0" aria-label="Jump up" title="Jump up">↑</a></span> <span class="reference-text">The weight of this item relative to other items in the pool.</span>
    </li>
    <li id="cite_note-chance-19"><span class="mw-cite-backlink"><a href="#cite_ref-chance_19-0" aria-label="Jump up" title="Jump up">↑</a></span> <span class="reference-text">The odds of finding any of this item in a single chest.</span>
    </li>
    <li id="cite_note-items-20"><span class="mw-cite-backlink"><a href="#cite_ref-items_20-0" aria-label="Jump up" title="Jump up">↑</a></span> <span class="reference-text">The number of items expected per chest, averaged over a large number of chests.</span>
    </li>
    <li id="cite_note-chests-21"><span class="mw-cite-backlink"><a href="#cite_ref-chests_21-0" aria-label="Jump up" title="Jump up">↑</a></span> <span class="reference-text">The average number of chests the player should expect to search to find any of this item.</span>
    </li>
    </ol></div></div>
    </div>
    <p><br>
    </p>
    <h3><span class="mw-headline" id="Fletcher_House">Fletcher House</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><span class="mw-editsection-bracket">]</span></span></h3>
    <p>Only fletcher houses in taiga villages contain chests.
    </p><p>In <i><a href="/wiki/Java_Edition" title="Java Edition">Java Edition</a></i>, each village fletcher chest contains 1–5 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_22-0" class="reference"><a href="#cite_note-stacksize-22">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_23-0" class="reference"><a href="#cite_note-weight-23">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_24-0" class="reference"><a href="#cite_note-chance-24">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_25-0" class="reference"><a href="#cite_note-items-25">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_26-0" class="reference"><a href="#cite_note-chests-26">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Feather" title="Feather"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-240px -544px"></span><span class="sprite-text">Feather</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="6"><sup>6</sup>⁄<sub>23</sub></td><td style="text-align:center;">55.8%</td><td style="text-align:center;">1.565</td><td style="text-align:center;">1.8</td></tr>
    <tr>
    <td><a href="/wiki/Flint" title="Flint"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-0px -560px"></span><span class="sprite-text">Flint</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="6"><sup>6</sup>⁄<sub>23</sub></td><td style="text-align:center;">55.8%</td><td style="text-align:center;">1.565</td><td style="text-align:center;">1.8</td></tr>
    <tr>
    <td><a href="/wiki/Stick" title="Stick"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -48px"></span><span class="sprite-text">Stick</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="6"><sup>6</sup>⁄<sub>23</sub></td><td style="text-align:center;">55.8%</td><td style="text-align:center;">1.565</td><td style="text-align:center;">1.8</td></tr>
    <tr>
    <td><a href="/wiki/Arrow" title="Arrow"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -32px"></span><span class="sprite-text">Arrow</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>23</sub></td><td style="text-align:center;">23.3%</td><td style="text-align:center;">0.522</td><td style="text-align:center;">4.3</td></tr>
    <tr>
    <td><a href="/wiki/Egg" title="Egg"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-48px -496px"></span><span class="sprite-text">Egg</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>23</sub></td><td style="text-align:center;">23.3%</td><td style="text-align:center;">0.522</td><td style="text-align:center;">4.3</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>23</sub></td><td style="text-align:center;">12.3%</td><td style="text-align:center;">0.130</td><td style="text-align:center;">8.1</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <p>In <i><a href="/wiki/Bedrock_Edition" title="Bedrock Edition">Bedrock Edition</a></i>, each village fletcher chest contains 1–5 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_22-1" class="reference"><a href="#cite_note-stacksize-22">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_23-1" class="reference"><a href="#cite_note-weight-23">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_24-1" class="reference"><a href="#cite_note-chance-24">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_25-1" class="reference"><a href="#cite_note-items-25">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_26-1" class="reference"><a href="#cite_note-chests-26">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Feather" title="Feather"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-240px -544px"></span><span class="sprite-text">Feather</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="6"><sup>6</sup>⁄<sub>23</sub></td><td style="text-align:center;">55.8%</td><td style="text-align:center;">1.565</td><td style="text-align:center;">1.8</td></tr>
    <tr>
    <td><a href="/wiki/Flint" title="Flint"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-0px -560px"></span><span class="sprite-text">Flint</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="6"><sup>6</sup>⁄<sub>23</sub></td><td style="text-align:center;">55.8%</td><td style="text-align:center;">1.565</td><td style="text-align:center;">1.8</td></tr>
    <tr>
    <td><a href="/wiki/Stick" title="Stick"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -48px"></span><span class="sprite-text">Stick</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="6"><sup>6</sup>⁄<sub>23</sub></td><td style="text-align:center;">55.8%</td><td style="text-align:center;">1.565</td><td style="text-align:center;">1.8</td></tr>
    <tr>
    <td><a href="/wiki/Arrow" title="Arrow"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -32px"></span><span class="sprite-text">Arrow</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>23</sub></td><td style="text-align:center;">23.3%</td><td style="text-align:center;">0.522</td><td style="text-align:center;">4.3</td></tr>
    <tr>
    <td><a href="/wiki/Egg" title="Egg"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-48px -496px"></span><span class="sprite-text">Egg</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>23</sub></td><td style="text-align:center;">23.3%</td><td style="text-align:center;">0.522</td><td style="text-align:center;">4.3</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>23</sub></td><td style="text-align:center;">12.3%</td><td style="text-align:center;">0.130</td><td style="text-align:center;">8.1</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <div class="mobileonly">
    <div class="reflist-upper-alpha"><div class="mw-references-wrap"><ol class="references">
    <li id="cite_note-stacksize-22"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-stacksize_22-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-stacksize_22-1">b</a></sup></span> <span class="reference-text">The size of stacks (or for unstackable items, number) of this item on any given roll.</span>
    </li>
    <li id="cite_note-weight-23"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-weight_23-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-weight_23-1">b</a></sup></span> <span class="reference-text">The weight of this item relative to other items in the pool.</span>
    </li>
    <li id="cite_note-chance-24"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chance_24-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chance_24-1">b</a></sup></span> <span class="reference-text">The odds of finding any of this item in a single chest.</span>
    </li>
    <li id="cite_note-items-25"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-items_25-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-items_25-1">b</a></sup></span> <span class="reference-text">The number of items expected per chest, averaged over a large number of chests.</span>
    </li>
    <li id="cite_note-chests-26"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chests_26-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chests_26-1">b</a></sup></span> <span class="reference-text">The average number of chests the player should expect to search to find any of this item.</span>
    </li>
    </ol></div></div>
    </div>
    <p><br>
    </p>
    <h3><span class="mw-headline" id="Mason_House">Mason House</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><span class="mw-editsection-bracket">]</span></span></h3>
    <p>Only mason houses in savanna villages contain chests.
    </p><p>In <i><a href="/wiki/Java_Edition" title="Java Edition">Java Edition</a></i>, each village mason chest contains 1–5 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_27-0" class="reference"><a href="#cite_note-stacksize-27">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_28-0" class="reference"><a href="#cite_note-weight-28">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_29-0" class="reference"><a href="#cite_note-chance-29">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_30-0" class="reference"><a href="#cite_note-items-30">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_31-0" class="reference"><a href="#cite_note-chests-31">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="4"><sup>4</sup>⁄<sub>13</sub></td><td style="text-align:center;">62.2%</td><td style="text-align:center;">2.308</td><td style="text-align:center;">1.6</td></tr>
    <tr>
    <td><a href="/wiki/Stone" title="Stone"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-672px -400px"></span><span class="sprite-text">Stone</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>13</sub></td><td style="text-align:center;">37.7%</td><td style="text-align:center;">0.462</td><td style="text-align:center;">2.7</td></tr>
    <tr>
    <td><a href="/wiki/Stone_bricks" class="mw-redirect" title="Stone bricks"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-176px -480px"></span><span class="sprite-text">Stone Bricks</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>13</sub></td><td style="text-align:center;">37.7%</td><td style="text-align:center;">0.462</td><td style="text-align:center;">2.7</td></tr>
    <tr>
    <td><a href="/wiki/Clay_Ball" title="Clay Ball"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-160px -544px"></span><span class="sprite-text">Clay Ball</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>13</sub></td><td style="text-align:center;">20.8%</td><td style="text-align:center;">0.462</td><td style="text-align:center;">4.8</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>13</sub></td><td style="text-align:center;">20.8%</td><td style="text-align:center;">0.231</td><td style="text-align:center;">4.8</td></tr>
    <tr>
    <td><a href="/wiki/Flower_pot" class="mw-redirect" title="Flower pot"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-224px -512px"></span><span class="sprite-text">Flower Pot</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>13</sub></td><td style="text-align:center;">20.8%</td><td style="text-align:center;">0.231</td><td style="text-align:center;">4.8</td></tr>
    <tr>
    <td><a href="/wiki/Smooth_stone" class="mw-redirect" title="Smooth stone"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-672px -464px"></span><span class="sprite-text">Smooth Stone</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>13</sub></td><td style="text-align:center;">20.8%</td><td style="text-align:center;">0.231</td><td style="text-align:center;">4.8</td></tr>
    <tr>
    <td><a href="/wiki/Dye" title="Dye"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-64px -608px"></span><span class="sprite-text">Yellow Dye</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>13</sub></td><td style="text-align:center;">20.8%</td><td style="text-align:center;">0.231</td><td style="text-align:center;">4.8</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <p>In <i><a href="/wiki/Bedrock_Edition" title="Bedrock Edition">Bedrock Edition</a></i>, each village mason chest contains 1–5 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_27-1" class="reference"><a href="#cite_note-stacksize-27">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_28-1" class="reference"><a href="#cite_note-weight-28">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_29-1" class="reference"><a href="#cite_note-chance-29">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_30-1" class="reference"><a href="#cite_note-items-30">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_31-1" class="reference"><a href="#cite_note-chests-31">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="4"><sup>4</sup>⁄<sub>13</sub></td><td style="text-align:center;">62.2%</td><td style="text-align:center;">2.308</td><td style="text-align:center;">1.6</td></tr>
    <tr>
    <td><a href="/wiki/Stone" title="Stone"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-672px -400px"></span><span class="sprite-text">Stone</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>13</sub></td><td style="text-align:center;">37.7%</td><td style="text-align:center;">0.462</td><td style="text-align:center;">2.7</td></tr>
    <tr>
    <td><a href="/wiki/Stone_bricks" class="mw-redirect" title="Stone bricks"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-176px -480px"></span><span class="sprite-text">Stone Bricks</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>13</sub></td><td style="text-align:center;">37.7%</td><td style="text-align:center;">0.462</td><td style="text-align:center;">2.7</td></tr>
    <tr>
    <td><a href="/wiki/Clay_Ball" title="Clay Ball"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-160px -544px"></span><span class="sprite-text">Clay Ball</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>13</sub></td><td style="text-align:center;">20.8%</td><td style="text-align:center;">0.462</td><td style="text-align:center;">4.8</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>13</sub></td><td style="text-align:center;">20.8%</td><td style="text-align:center;">0.231</td><td style="text-align:center;">4.8</td></tr>
    <tr>
    <td><a href="/wiki/Flower_pot" class="mw-redirect" title="Flower pot"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-224px -512px"></span><span class="sprite-text">Flower Pot</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>13</sub></td><td style="text-align:center;">20.8%</td><td style="text-align:center;">0.231</td><td style="text-align:center;">4.8</td></tr>
    <tr>
    <td><a href="/wiki/Smooth_stone" class="mw-redirect" title="Smooth stone"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-672px -464px"></span><span class="sprite-text">Smooth Stone</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>13</sub></td><td style="text-align:center;">20.8%</td><td style="text-align:center;">0.231</td><td style="text-align:center;">4.8</td></tr>
    <tr>
    <td><a href="/wiki/Dye" title="Dye"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-64px -608px"></span><span class="sprite-text">Yellow Dye</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>13</sub></td><td style="text-align:center;">20.8%</td><td style="text-align:center;">0.231</td><td style="text-align:center;">4.8</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <div class="mobileonly">
    <div class="reflist-upper-alpha"><div class="mw-references-wrap"><ol class="references">
    <li id="cite_note-stacksize-27"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-stacksize_27-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-stacksize_27-1">b</a></sup></span> <span class="reference-text">The size of stacks (or for unstackable items, number) of this item on any given roll.</span>
    </li>
    <li id="cite_note-weight-28"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-weight_28-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-weight_28-1">b</a></sup></span> <span class="reference-text">The weight of this item relative to other items in the pool.</span>
    </li>
    <li id="cite_note-chance-29"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chance_29-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chance_29-1">b</a></sup></span> <span class="reference-text">The odds of finding any of this item in a single chest.</span>
    </li>
    <li id="cite_note-items-30"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-items_30-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-items_30-1">b</a></sup></span> <span class="reference-text">The number of items expected per chest, averaged over a large number of chests.</span>
    </li>
    <li id="cite_note-chests-31"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chests_31-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chests_31-1">b</a></sup></span> <span class="reference-text">The average number of chests the player should expect to search to find any of this item.</span>
    </li>
    </ol></div></div>
    </div>
    <p><br>
    </p>
    <h3><span class="mw-headline" id="Shepherd_House">Shepherd House</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><span class="mw-editsection-bracket">]</span></span></h3>
    <p>Only shepherd houses in snowy villages contain chests.
    </p><p>In <i><a href="/wiki/Java_Edition" title="Java Edition">Java Edition</a></i>, each village shepherd chest contains 1–5 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_32-0" class="reference"><a href="#cite_note-stacksize-32">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_33-0" class="reference"><a href="#cite_note-weight-33">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_34-0" class="reference"><a href="#cite_note-chance-34">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_35-0" class="reference"><a href="#cite_note-items-35">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_36-0" class="reference"><a href="#cite_note-chests-36">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Wool" title="Wool"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-0px -32px"></span><span class="sprite-text">White Wool</span></a></td>
    <td style="text-align:center;" data-sort-value="4.5">1–8</td><td style="text-align:center;" data-sort-value="6"><sup>6</sup>⁄<sub>23</sub></td><td style="text-align:center;">55.8%</td><td style="text-align:center;">3.522</td><td style="text-align:center;">1.8</td></tr>
    <tr>
    <td><a href="/wiki/Wheat" title="Wheat"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-192px -576px"></span><span class="sprite-text">Wheat</span></a></td>
    <td style="text-align:center;" data-sort-value="3.5">1–6</td><td style="text-align:center;" data-sort-value="6"><sup>6</sup>⁄<sub>23</sub></td><td style="text-align:center;">55.8%</td><td style="text-align:center;">2.739</td><td style="text-align:center;">1.8</td></tr>
    <tr>
    <td><a href="/wiki/Wool" title="Wool"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-400px -48px"></span><span class="sprite-text">Black Wool</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="3"><sup>3</sup>⁄<sub>23</sub></td><td style="text-align:center;">33.0%</td><td style="text-align:center;">0.783</td><td style="text-align:center;">3.0</td></tr>
    <tr>
    <td><a href="/wiki/Wool" title="Wool"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-16px -80px"></span><span class="sprite-text">Brown Wool</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>23</sub></td><td style="text-align:center;">23.3%</td><td style="text-align:center;">0.522</td><td style="text-align:center;">4.3</td></tr>
    <tr>
    <td><a href="/wiki/Wool" title="Wool"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-416px -48px"></span><span class="sprite-text">Gray Wool</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>23</sub></td><td style="text-align:center;">23.3%</td><td style="text-align:center;">0.522</td><td style="text-align:center;">4.3</td></tr>
    <tr>
    <td><a href="/wiki/Wool" title="Wool"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-16px -112px"></span><span class="sprite-text">Light Gray Wool</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>23</sub></td><td style="text-align:center;">23.3%</td><td style="text-align:center;">0.522</td><td style="text-align:center;">4.3</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>23</sub></td><td style="text-align:center;">12.3%</td><td style="text-align:center;">0.130</td><td style="text-align:center;">8.1</td></tr>
    <tr>
    <td><a href="/wiki/Shears" title="Shears"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-144px -464px"></span><span class="sprite-text">Shears</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>23</sub></td><td style="text-align:center;">12.3%</td><td style="text-align:center;">0.130</td><td style="text-align:center;">8.1</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <p>In <i><a href="/wiki/Bedrock_Edition" title="Bedrock Edition">Bedrock Edition</a></i>, each village shepherd chest contains 1–5 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_32-1" class="reference"><a href="#cite_note-stacksize-32">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_33-1" class="reference"><a href="#cite_note-weight-33">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_34-1" class="reference"><a href="#cite_note-chance-34">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_35-1" class="reference"><a href="#cite_note-items-35">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_36-1" class="reference"><a href="#cite_note-chests-36">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Wool" title="Wool"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-0px -32px"></span><span class="sprite-text">White Wool</span></a></td>
    <td style="text-align:center;" data-sort-value="4.5">1–8</td><td style="text-align:center;" data-sort-value="6"><sup>6</sup>⁄<sub>23</sub></td><td style="text-align:center;">55.8%</td><td style="text-align:center;">3.522</td><td style="text-align:center;">1.8</td></tr>
    <tr>
    <td><a href="/wiki/Wheat" title="Wheat"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-192px -576px"></span><span class="sprite-text">Wheat</span></a></td>
    <td style="text-align:center;" data-sort-value="3.5">1–6</td><td style="text-align:center;" data-sort-value="6"><sup>6</sup>⁄<sub>23</sub></td><td style="text-align:center;">55.8%</td><td style="text-align:center;">2.739</td><td style="text-align:center;">1.8</td></tr>
    <tr>
    <td><a href="/wiki/Wool" title="Wool"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-400px -48px"></span><span class="sprite-text">Black Wool</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="3"><sup>3</sup>⁄<sub>23</sub></td><td style="text-align:center;">33.0%</td><td style="text-align:center;">0.783</td><td style="text-align:center;">3.0</td></tr>
    <tr>
    <td><a href="/wiki/Wool" title="Wool"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-16px -80px"></span><span class="sprite-text">Brown Wool</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>23</sub></td><td style="text-align:center;">23.3%</td><td style="text-align:center;">0.522</td><td style="text-align:center;">4.3</td></tr>
    <tr>
    <td><a href="/wiki/Wool" title="Wool"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-416px -48px"></span><span class="sprite-text">Gray Wool</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>23</sub></td><td style="text-align:center;">23.3%</td><td style="text-align:center;">0.522</td><td style="text-align:center;">4.3</td></tr>
    <tr>
    <td><a href="/wiki/Wool" title="Wool"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-16px -112px"></span><span class="sprite-text">Light Gray Wool</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>23</sub></td><td style="text-align:center;">23.3%</td><td style="text-align:center;">0.522</td><td style="text-align:center;">4.3</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>23</sub></td><td style="text-align:center;">12.3%</td><td style="text-align:center;">0.130</td><td style="text-align:center;">8.1</td></tr>
    <tr>
    <td><a href="/wiki/Shears" title="Shears"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-144px -464px"></span><span class="sprite-text">Shears</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>23</sub></td><td style="text-align:center;">12.3%</td><td style="text-align:center;">0.130</td><td style="text-align:center;">8.1</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <div class="mobileonly">
    <div class="reflist-upper-alpha"><div class="mw-references-wrap"><ol class="references">
    <li id="cite_note-stacksize-32"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-stacksize_32-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-stacksize_32-1">b</a></sup></span> <span class="reference-text">The size of stacks (or for unstackable items, number) of this item on any given roll.</span>
    </li>
    <li id="cite_note-weight-33"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-weight_33-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-weight_33-1">b</a></sup></span> <span class="reference-text">The weight of this item relative to other items in the pool.</span>
    </li>
    <li id="cite_note-chance-34"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chance_34-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chance_34-1">b</a></sup></span> <span class="reference-text">The odds of finding any of this item in a single chest.</span>
    </li>
    <li id="cite_note-items-35"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-items_35-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-items_35-1">b</a></sup></span> <span class="reference-text">The number of items expected per chest, averaged over a large number of chests.</span>
    </li>
    <li id="cite_note-chests-36"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chests_36-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chests_36-1">b</a></sup></span> <span class="reference-text">The average number of chests the player should expect to search to find any of this item.</span>
    </li>
    </ol></div></div>
    </div>
    <p><br>
    </p>
    <h3><span class="mw-headline" id="Tannery">Tannery</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><span class="mw-editsection-bracket">]</span></span></h3>
    <p>All tanneries except those in desert villages contain chests.
    </p><p>In <i><a href="/wiki/Java_Edition" title="Java Edition">Java Edition</a></i>, each village tannery chest contains 1–5 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_37-0" class="reference"><a href="#cite_note-stacksize-37">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_38-0" class="reference"><a href="#cite_note-weight-38">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_39-0" class="reference"><a href="#cite_note-chance-39">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_40-0" class="reference"><a href="#cite_note-items-40">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_41-0" class="reference"><a href="#cite_note-chests-41">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>16</sub></td><td style="text-align:center;">62.8%</td><td style="text-align:center;">2.344</td><td style="text-align:center;">1.6</td></tr>
    <tr>
    <td><a href="/wiki/Armor" title="Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-144px -416px"></span><span class="sprite-text">Leather Cap</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>16</sub></td><td style="text-align:center;">31.8%</td><td style="text-align:center;">0.375</td><td style="text-align:center;">3.1</td></tr>
    <tr>
    <td><a href="/wiki/Armor" title="Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-160px -416px"></span><span class="sprite-text">Leather Tunic</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>16</sub></td><td style="text-align:center;">31.8%</td><td style="text-align:center;">0.375</td><td style="text-align:center;">3.1</td></tr>
    <tr>
    <td><a href="/wiki/Armor" title="Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-192px -416px"></span><span class="sprite-text">Leather Pants</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>16</sub></td><td style="text-align:center;">31.8%</td><td style="text-align:center;">0.375</td><td style="text-align:center;">3.1</td></tr>
    <tr>
    <td><a href="/wiki/Armor" title="Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -416px"></span><span class="sprite-text">Leather Boots</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>16</sub></td><td style="text-align:center;">31.8%</td><td style="text-align:center;">0.375</td><td style="text-align:center;">3.1</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>16</sub></td><td style="text-align:center;">17.3%</td><td style="text-align:center;">0.469</td><td style="text-align:center;">5.8</td></tr>
    <tr>
    <td><a href="/wiki/Leather" title="Leather"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-144px -560px"></span><span class="sprite-text">Leather</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>16</sub></td><td style="text-align:center;">17.3%</td><td style="text-align:center;">0.375</td><td style="text-align:center;">5.8</td></tr>
    <tr>
    <td><a href="/wiki/Saddle" title="Saddle"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -528px"></span><span class="sprite-text">Saddle</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>16</sub></td><td style="text-align:center;">17.3%</td><td style="text-align:center;">0.188</td><td style="text-align:center;">5.8</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <p>In <i><a href="/wiki/Bedrock_Edition" title="Bedrock Edition">Bedrock Edition</a></i>, each village tannery chest contains 1–5 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_37-1" class="reference"><a href="#cite_note-stacksize-37">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_38-1" class="reference"><a href="#cite_note-weight-38">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_39-1" class="reference"><a href="#cite_note-chance-39">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_40-1" class="reference"><a href="#cite_note-items-40">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_41-1" class="reference"><a href="#cite_note-chests-41">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>16</sub></td><td style="text-align:center;">62.8%</td><td style="text-align:center;">2.344</td><td style="text-align:center;">1.6</td></tr>
    <tr>
    <td><a href="/wiki/Armor" title="Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-144px -416px"></span><span class="sprite-text">Leather Cap</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>16</sub></td><td style="text-align:center;">31.8%</td><td style="text-align:center;">0.375</td><td style="text-align:center;">3.1</td></tr>
    <tr>
    <td><a href="/wiki/Armor" title="Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-160px -416px"></span><span class="sprite-text">Leather Tunic</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>16</sub></td><td style="text-align:center;">31.8%</td><td style="text-align:center;">0.375</td><td style="text-align:center;">3.1</td></tr>
    <tr>
    <td><a href="/wiki/Armor" title="Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-192px -416px"></span><span class="sprite-text">Leather Pants</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>16</sub></td><td style="text-align:center;">31.8%</td><td style="text-align:center;">0.375</td><td style="text-align:center;">3.1</td></tr>
    <tr>
    <td><a href="/wiki/Armor" title="Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -416px"></span><span class="sprite-text">Leather Boots</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>16</sub></td><td style="text-align:center;">31.8%</td><td style="text-align:center;">0.375</td><td style="text-align:center;">3.1</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>16</sub></td><td style="text-align:center;">17.3%</td><td style="text-align:center;">0.469</td><td style="text-align:center;">5.8</td></tr>
    <tr>
    <td><a href="/wiki/Leather" title="Leather"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-144px -560px"></span><span class="sprite-text">Leather</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>16</sub></td><td style="text-align:center;">17.3%</td><td style="text-align:center;">0.375</td><td style="text-align:center;">5.8</td></tr>
    <tr>
    <td><a href="/wiki/Saddle" title="Saddle"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -528px"></span><span class="sprite-text">Saddle</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>16</sub></td><td style="text-align:center;">17.3%</td><td style="text-align:center;">0.188</td><td style="text-align:center;">5.8</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <div class="mobileonly">
    <div class="reflist-upper-alpha"><div class="mw-references-wrap"><ol class="references">
    <li id="cite_note-stacksize-37"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-stacksize_37-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-stacksize_37-1">b</a></sup></span> <span class="reference-text">The size of stacks (or for unstackable items, number) of this item on any given roll.</span>
    </li>
    <li id="cite_note-weight-38"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-weight_38-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-weight_38-1">b</a></sup></span> <span class="reference-text">The weight of this item relative to other items in the pool.</span>
    </li>
    <li id="cite_note-chance-39"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chance_39-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chance_39-1">b</a></sup></span> <span class="reference-text">The odds of finding any of this item in a single chest.</span>
    </li>
    <li id="cite_note-items-40"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-items_40-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-items_40-1">b</a></sup></span> <span class="reference-text">The number of items expected per chest, averaged over a large number of chests.</span>
    </li>
    <li id="cite_note-chests-41"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chests_41-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chests_41-1">b</a></sup></span> <span class="reference-text">The average number of chests the player should expect to search to find any of this item.</span>
    </li>
    </ol></div></div>
    </div>
    <p><br>
    </p>
    <h3><span class="mw-headline" id="Temple">Temple</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><span class="mw-editsection-bracket">]</span></span></h3>
    <p>Only temples in desert villages contain chests.
    </p><p>In <i><a href="/wiki/Java_Edition" title="Java Edition">Java Edition</a></i>, each village temple chest contains 3–8 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_42-0" class="reference"><a href="#cite_note-stacksize-42">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_43-0" class="reference"><a href="#cite_note-weight-43">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_44-0" class="reference"><a href="#cite_note-chance-44">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_45-0" class="reference"><a href="#cite_note-items-45">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_46-0" class="reference"><a href="#cite_note-chests-46">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="7"><sup>7</sup>⁄<sub>19</sub></td><td style="text-align:center;">89.3%</td><td style="text-align:center;">5.066</td><td style="text-align:center;">1.1</td></tr>
    <tr>
    <td><a href="/wiki/Rotten_flesh" class="mw-redirect" title="Rotten flesh"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-32px -512px"></span><span class="sprite-text">Rotten Flesh</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="7"><sup>7</sup>⁄<sub>19</sub></td><td style="text-align:center;">89.3%</td><td style="text-align:center;">5.066</td><td style="text-align:center;">1.1</td></tr>
    <tr>
    <td><a href="/wiki/Redstone" class="mw-redirect" title="Redstone"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-16px -576px"></span><span class="sprite-text">Redstone Dust</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>19</sub></td><td style="text-align:center;">44.8%</td><td style="text-align:center;">1.447</td><td style="text-align:center;">2.2</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>19</sub></td><td style="text-align:center;">25.4%</td><td style="text-align:center;">0.724</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Lapis_lazuli" class="mw-redirect" title="Lapis lazuli"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -560px"></span><span class="sprite-text">Lapis Lazuli</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>19</sub></td><td style="text-align:center;">25.4%</td><td style="text-align:center;">0.724</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Gold_ingot" class="mw-redirect" title="Gold ingot"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-48px -560px"></span><span class="sprite-text">Gold Ingot</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>19</sub></td><td style="text-align:center;">25.4%</td><td style="text-align:center;">0.724</td><td style="text-align:center;">3.9</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <p>In <i><a href="/wiki/Bedrock_Edition" title="Bedrock Edition">Bedrock Edition</a></i>, each village temple chest contains 3–8 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_42-1" class="reference"><a href="#cite_note-stacksize-42">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_43-1" class="reference"><a href="#cite_note-weight-43">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_44-1" class="reference"><a href="#cite_note-chance-44">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_45-1" class="reference"><a href="#cite_note-items-45">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_46-1" class="reference"><a href="#cite_note-chests-46">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="7"><sup>7</sup>⁄<sub>19</sub></td><td style="text-align:center;">89.3%</td><td style="text-align:center;">5.066</td><td style="text-align:center;">1.1</td></tr>
    <tr>
    <td><a href="/wiki/Rotten_flesh" class="mw-redirect" title="Rotten flesh"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-32px -512px"></span><span class="sprite-text">Rotten Flesh</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="7"><sup>7</sup>⁄<sub>19</sub></td><td style="text-align:center;">89.3%</td><td style="text-align:center;">5.066</td><td style="text-align:center;">1.1</td></tr>
    <tr>
    <td><a href="/wiki/Redstone" class="mw-redirect" title="Redstone"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-16px -576px"></span><span class="sprite-text">Redstone Dust</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>19</sub></td><td style="text-align:center;">44.8%</td><td style="text-align:center;">1.447</td><td style="text-align:center;">2.2</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>19</sub></td><td style="text-align:center;">25.4%</td><td style="text-align:center;">0.724</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Lapis_lazuli" class="mw-redirect" title="Lapis lazuli"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -560px"></span><span class="sprite-text">Lapis Lazuli</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>19</sub></td><td style="text-align:center;">25.4%</td><td style="text-align:center;">0.724</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Gold_ingot" class="mw-redirect" title="Gold ingot"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-48px -560px"></span><span class="sprite-text">Gold Ingot</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>19</sub></td><td style="text-align:center;">25.4%</td><td style="text-align:center;">0.724</td><td style="text-align:center;">3.9</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <div class="mobileonly">
    <div class="reflist-upper-alpha"><div class="mw-references-wrap"><ol class="references">
    <li id="cite_note-stacksize-42"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-stacksize_42-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-stacksize_42-1">b</a></sup></span> <span class="reference-text">The size of stacks (or for unstackable items, number) of this item on any given roll.</span>
    </li>
    <li id="cite_note-weight-43"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-weight_43-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-weight_43-1">b</a></sup></span> <span class="reference-text">The weight of this item relative to other items in the pool.</span>
    </li>
    <li id="cite_note-chance-44"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chance_44-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chance_44-1">b</a></sup></span> <span class="reference-text">The odds of finding any of this item in a single chest.</span>
    </li>
    <li id="cite_note-items-45"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-items_45-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-items_45-1">b</a></sup></span> <span class="reference-text">The number of items expected per chest, averaged over a large number of chests.</span>
    </li>
    <li id="cite_note-chests-46"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chests_46-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chests_46-1">b</a></sup></span> <span class="reference-text">The average number of chests the player should expect to search to find any of this item.</span>
    </li>
    </ol></div></div>
    </div>
    <p><br>
    </p>
    <h3><span class="mw-headline" id="Toolsmith">Toolsmith</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><span class="mw-editsection-bracket">]</span></span></h3>
    <p>Only toolsmiths in desert and taiga villages contain chests.
    </p><p>In <i><a href="/wiki/Java_Edition" title="Java Edition">Java Edition</a></i>, each village toolsmith chest contains 3–8 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_47-0" class="reference"><a href="#cite_note-stacksize-47">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_48-0" class="reference"><a href="#cite_note-weight-48">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_49-0" class="reference"><a href="#cite_note-chance-49">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_50-0" class="reference"><a href="#cite_note-items-50">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_51-0" class="reference"><a href="#cite_note-chests-51">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Stick" title="Stick"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -48px"></span><span class="sprite-text">Stick</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="20"><sup>20</sup>⁄<sub>53</sub></td><td style="text-align:center;">90.0%</td><td style="text-align:center;">4.151</td><td style="text-align:center;">1.1</td></tr>
    <tr>
    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="15"><sup>15</sup>⁄<sub>53</sub></td><td style="text-align:center;">81.2%</td><td style="text-align:center;">3.113</td><td style="text-align:center;">1.2</td></tr>
    <tr>
    <td><a href="/wiki/Iron_ingot" class="mw-redirect" title="Iron ingot"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-112px -560px"></span><span class="sprite-text">Iron Ingot</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>53</sub></td><td style="text-align:center;">41.2%</td><td style="text-align:center;">1.557</td><td style="text-align:center;">2.4</td></tr>
    <tr>
    <td><a href="/wiki/Pickaxe" title="Pickaxe"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-96px -464px"></span><span class="sprite-text">Iron Pickaxe</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>53</sub></td><td style="text-align:center;">41.2%</td><td style="text-align:center;">0.519</td><td style="text-align:center;">2.4</td></tr>
    <tr>
    <td><a href="/wiki/Shovel" title="Shovel"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-112px -464px"></span><span class="sprite-text">Iron Shovel</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>53</sub></td><td style="text-align:center;">41.2%</td><td style="text-align:center;">0.519</td><td style="text-align:center;">2.4</td></tr>
    <tr>
    <td><a href="/wiki/Coal" title="Coal"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-176px -544px"></span><span class="sprite-text">Coal</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>53</sub></td><td style="text-align:center;">9.9%</td><td style="text-align:center;">0.208</td><td style="text-align:center;">10.1</td></tr>
    <tr>
    <td><a href="/wiki/Gold_ingot" class="mw-redirect" title="Gold ingot"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-48px -560px"></span><span class="sprite-text">Gold Ingot</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>53</sub></td><td style="text-align:center;">9.9%</td><td style="text-align:center;">0.208</td><td style="text-align:center;">10.1</td></tr>
    <tr>
    <td><a href="/wiki/Diamond" title="Diamond"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-192px -544px"></span><span class="sprite-text">Diamond</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>53</sub></td><td style="text-align:center;">9.9%</td><td style="text-align:center;">0.208</td><td style="text-align:center;">10.1</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <p>In <i><a href="/wiki/Bedrock_Edition" title="Bedrock Edition">Bedrock Edition</a></i>, each village toolsmith chest contains 3–8 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_47-1" class="reference"><a href="#cite_note-stacksize-47">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_48-1" class="reference"><a href="#cite_note-weight-48">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_49-1" class="reference"><a href="#cite_note-chance-49">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_50-1" class="reference"><a href="#cite_note-items-50">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_51-1" class="reference"><a href="#cite_note-chests-51">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Stick" title="Stick"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -48px"></span><span class="sprite-text">Stick</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="20"><sup>20</sup>⁄<sub>53</sub></td><td style="text-align:center;">90.0%</td><td style="text-align:center;">4.151</td><td style="text-align:center;">1.1</td></tr>
    <tr>
    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="15"><sup>15</sup>⁄<sub>53</sub></td><td style="text-align:center;">81.2%</td><td style="text-align:center;">3.113</td><td style="text-align:center;">1.2</td></tr>
    <tr>
    <td><a href="/wiki/Iron_ingot" class="mw-redirect" title="Iron ingot"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-112px -560px"></span><span class="sprite-text">Iron Ingot</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>53</sub></td><td style="text-align:center;">41.2%</td><td style="text-align:center;">1.557</td><td style="text-align:center;">2.4</td></tr>
    <tr>
    <td><a href="/wiki/Pickaxe" title="Pickaxe"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-96px -464px"></span><span class="sprite-text">Iron Pickaxe</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>53</sub></td><td style="text-align:center;">41.2%</td><td style="text-align:center;">0.519</td><td style="text-align:center;">2.4</td></tr>
    <tr>
    <td><a href="/wiki/Shovel" title="Shovel"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-112px -464px"></span><span class="sprite-text">Iron Shovel</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>53</sub></td><td style="text-align:center;">41.2%</td><td style="text-align:center;">0.519</td><td style="text-align:center;">2.4</td></tr>
    <tr>
    <td><a href="/wiki/Coal" title="Coal"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-176px -544px"></span><span class="sprite-text">Coal</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>53</sub></td><td style="text-align:center;">9.9%</td><td style="text-align:center;">0.208</td><td style="text-align:center;">10.1</td></tr>
    <tr>
    <td><a href="/wiki/Gold_ingot" class="mw-redirect" title="Gold ingot"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-48px -560px"></span><span class="sprite-text">Gold Ingot</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>53</sub></td><td style="text-align:center;">9.9%</td><td style="text-align:center;">0.208</td><td style="text-align:center;">10.1</td></tr>
    <tr>
    <td><a href="/wiki/Diamond" title="Diamond"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-192px -544px"></span><span class="sprite-text">Diamond</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>53</sub></td><td style="text-align:center;">9.9%</td><td style="text-align:center;">0.208</td><td style="text-align:center;">10.1</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <div class="mobileonly">
    <div class="reflist-upper-alpha"><div class="mw-references-wrap"><ol class="references">
    <li id="cite_note-stacksize-47"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-stacksize_47-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-stacksize_47-1">b</a></sup></span> <span class="reference-text">The size of stacks (or for unstackable items, number) of this item on any given roll.</span>
    </li>
    <li id="cite_note-weight-48"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-weight_48-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-weight_48-1">b</a></sup></span> <span class="reference-text">The weight of this item relative to other items in the pool.</span>
    </li>
    <li id="cite_note-chance-49"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chance_49-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chance_49-1">b</a></sup></span> <span class="reference-text">The odds of finding any of this item in a single chest.</span>
    </li>
    <li id="cite_note-items-50"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-items_50-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-items_50-1">b</a></sup></span> <span class="reference-text">The number of items expected per chest, averaged over a large number of chests.</span>
    </li>
    <li id="cite_note-chests-51"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chests_51-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chests_51-1">b</a></sup></span> <span class="reference-text">The average number of chests the player should expect to search to find any of this item.</span>
    </li>
    </ol></div></div>
    </div>
    <p><br>
    </p>
    <h3><span class="mw-headline" id="Weaponsmith">Weaponsmith</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><span class="mw-editsection-bracket">]</span></span></h3>
    <p>All weaponsmiths contain chests.
    </p><p>In <i><a href="/wiki/Java_Edition" title="Java Edition">Java Edition</a></i>, each village weaponsmith chest contains 3–8 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_52-0" class="reference"><a href="#cite_note-stacksize-52">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_53-0" class="reference"><a href="#cite_note-weight-53">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_54-0" class="reference"><a href="#cite_note-chance-54">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_55-0" class="reference"><a href="#cite_note-items-55">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_56-0" class="reference"><a href="#cite_note-chests-56">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Apple" title="Apple"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-48px -480px"></span><span class="sprite-text">Apple</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="15"><sup>15</sup>⁄<sub>94</sub></td><td style="text-align:center;">59.8%</td><td style="text-align:center;">1.755</td><td style="text-align:center;">1.7</td></tr>
    <tr>
    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="15"><sup>15</sup>⁄<sub>94</sub></td><td style="text-align:center;">59.8%</td><td style="text-align:center;">1.755</td><td style="text-align:center;">1.7</td></tr>
    <tr>
    <td><a href="/wiki/Iron_ingot" class="mw-redirect" title="Iron ingot"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-112px -560px"></span><span class="sprite-text">Iron Ingot</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>94</sub></td><td style="text-align:center;">45.1%</td><td style="text-align:center;">1.755</td><td style="text-align:center;">2.2</td></tr>
    <tr>
    <td><a href="/wiki/Sapling" title="Sapling"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-544px -464px"></span><span class="sprite-text">Oak Sapling</span></a></td>
    <td style="text-align:center;" data-sort-value="5">3–7</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>94</sub></td><td style="text-align:center;">25.6%</td><td style="text-align:center;">1.463</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Obsidian" title="Obsidian"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-320px -416px"></span><span class="sprite-text">Obsidian</span></a></td>
    <td style="text-align:center;" data-sort-value="5">3–7</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>94</sub></td><td style="text-align:center;">25.6%</td><td style="text-align:center;">1.463</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Gold_ingot" class="mw-redirect" title="Gold ingot"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-48px -560px"></span><span class="sprite-text">Gold Ingot</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>94</sub></td><td style="text-align:center;">25.6%</td><td style="text-align:center;">0.585</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Pickaxe" title="Pickaxe"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-96px -464px"></span><span class="sprite-text">Iron Pickaxe</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>94</sub></td><td style="text-align:center;">25.6%</td><td style="text-align:center;">0.293</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Sword" title="Sword"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-0px -448px"></span><span class="sprite-text">Iron Sword</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>94</sub></td><td style="text-align:center;">25.6%</td><td style="text-align:center;">0.293</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Armor" title="Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -416px"></span><span class="sprite-text">Iron Helmet</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>94</sub></td><td style="text-align:center;">25.6%</td><td style="text-align:center;">0.293</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Armor" title="Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-64px -416px"></span><span class="sprite-text">Iron Chestplate</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>94</sub></td><td style="text-align:center;">25.6%</td><td style="text-align:center;">0.293</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Armor" title="Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-112px -416px"></span><span class="sprite-text">Iron Leggings</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>94</sub></td><td style="text-align:center;">25.6%</td><td style="text-align:center;">0.293</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Armor" title="Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-48px -416px"></span><span class="sprite-text">Iron Boots</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>94</sub></td><td style="text-align:center;">25.6%</td><td style="text-align:center;">0.293</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Diamond" title="Diamond"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-192px -544px"></span><span class="sprite-text">Diamond</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="3"><sup>3</sup>⁄<sub>94</sub></td><td style="text-align:center;">16.2%</td><td style="text-align:center;">0.351</td><td style="text-align:center;">6.2</td></tr>
    <tr>
    <td><a href="/wiki/Saddle" title="Saddle"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -528px"></span><span class="sprite-text">Saddle</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="3"><sup>3</sup>⁄<sub>94</sub></td><td style="text-align:center;">16.2%</td><td style="text-align:center;">0.176</td><td style="text-align:center;">6.2</td></tr>
    <tr>
    <td><a href="/wiki/Horse_Armor" title="Horse Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-96px -416px"></span><span class="sprite-text">Iron Horse Armor</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>94</sub></td><td style="text-align:center;">5.7%</td><td style="text-align:center;">0.059</td><td style="text-align:center;">17.6</td></tr>
    <tr>
    <td><a href="/wiki/Horse_Armor" title="Horse Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-16px -416px"></span><span class="sprite-text">Golden Horse Armor</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>94</sub></td><td style="text-align:center;">5.7%</td><td style="text-align:center;">0.059</td><td style="text-align:center;">17.6</td></tr>
    <tr>
    <td><a href="/wiki/Horse_Armor" title="Horse Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-176px -400px"></span><span class="sprite-text">Diamond Horse Armor</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>94</sub></td><td style="text-align:center;">5.7%</td><td style="text-align:center;">0.059</td><td style="text-align:center;">17.6</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <p>In <i><a href="/wiki/Bedrock_Edition" title="Bedrock Edition">Bedrock Edition</a></i>, each village weaponsmith chest contains 3–8 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_52-1" class="reference"><a href="#cite_note-stacksize-52">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_53-1" class="reference"><a href="#cite_note-weight-53">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_54-1" class="reference"><a href="#cite_note-chance-54">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_55-1" class="reference"><a href="#cite_note-items-55">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_56-1" class="reference"><a href="#cite_note-chests-56">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Apple" title="Apple"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-48px -480px"></span><span class="sprite-text">Apple</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="15"><sup>15</sup>⁄<sub>94</sub></td><td style="text-align:center;">59.8%</td><td style="text-align:center;">1.755</td><td style="text-align:center;">1.7</td></tr>
    <tr>
    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="15"><sup>15</sup>⁄<sub>94</sub></td><td style="text-align:center;">59.8%</td><td style="text-align:center;">1.755</td><td style="text-align:center;">1.7</td></tr>
    <tr>
    <td><a href="/wiki/Iron_ingot" class="mw-redirect" title="Iron ingot"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-112px -560px"></span><span class="sprite-text">Iron Ingot</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>94</sub></td><td style="text-align:center;">45.1%</td><td style="text-align:center;">1.755</td><td style="text-align:center;">2.2</td></tr>
    <tr>
    <td><a href="/wiki/Sapling" title="Sapling"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-544px -464px"></span><span class="sprite-text">Oak Sapling</span></a></td>
    <td style="text-align:center;" data-sort-value="5">3–7</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>94</sub></td><td style="text-align:center;">25.6%</td><td style="text-align:center;">1.463</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Obsidian" title="Obsidian"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-320px -416px"></span><span class="sprite-text">Obsidian</span></a></td>
    <td style="text-align:center;" data-sort-value="5">3–7</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>94</sub></td><td style="text-align:center;">25.6%</td><td style="text-align:center;">1.463</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Gold_ingot" class="mw-redirect" title="Gold ingot"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-48px -560px"></span><span class="sprite-text">Gold Ingot</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>94</sub></td><td style="text-align:center;">25.6%</td><td style="text-align:center;">0.585</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Pickaxe" title="Pickaxe"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-96px -464px"></span><span class="sprite-text">Iron Pickaxe</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>94</sub></td><td style="text-align:center;">25.6%</td><td style="text-align:center;">0.293</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Sword" title="Sword"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-0px -448px"></span><span class="sprite-text">Iron Sword</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>94</sub></td><td style="text-align:center;">25.6%</td><td style="text-align:center;">0.293</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Armor" title="Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -416px"></span><span class="sprite-text">Iron Helmet</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>94</sub></td><td style="text-align:center;">25.6%</td><td style="text-align:center;">0.293</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Armor" title="Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-64px -416px"></span><span class="sprite-text">Iron Chestplate</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>94</sub></td><td style="text-align:center;">25.6%</td><td style="text-align:center;">0.293</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Armor" title="Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-112px -416px"></span><span class="sprite-text">Iron Leggings</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>94</sub></td><td style="text-align:center;">25.6%</td><td style="text-align:center;">0.293</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Armor" title="Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-48px -416px"></span><span class="sprite-text">Iron Boots</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>94</sub></td><td style="text-align:center;">25.6%</td><td style="text-align:center;">0.293</td><td style="text-align:center;">3.9</td></tr>
    <tr>
    <td><a href="/wiki/Diamond" title="Diamond"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-192px -544px"></span><span class="sprite-text">Diamond</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="3"><sup>3</sup>⁄<sub>94</sub></td><td style="text-align:center;">16.2%</td><td style="text-align:center;">0.351</td><td style="text-align:center;">6.2</td></tr>
    <tr>
    <td><a href="/wiki/Saddle" title="Saddle"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -528px"></span><span class="sprite-text">Saddle</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="3"><sup>3</sup>⁄<sub>94</sub></td><td style="text-align:center;">16.2%</td><td style="text-align:center;">0.176</td><td style="text-align:center;">6.2</td></tr>
    <tr>
    <td><a href="/wiki/Horse_Armor" title="Horse Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-96px -416px"></span><span class="sprite-text">Iron Horse Armor</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>94</sub></td><td style="text-align:center;">5.7%</td><td style="text-align:center;">0.059</td><td style="text-align:center;">17.6</td></tr>
    <tr>
    <td><a href="/wiki/Horse_Armor" title="Horse Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-16px -416px"></span><span class="sprite-text">Golden Horse Armor</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>94</sub></td><td style="text-align:center;">5.7%</td><td style="text-align:center;">0.059</td><td style="text-align:center;">17.6</td></tr>
    <tr>
    <td><a href="/wiki/Horse_Armor" title="Horse Armor"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-176px -400px"></span><span class="sprite-text">Diamond Horse Armor</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>94</sub></td><td style="text-align:center;">5.7%</td><td style="text-align:center;">0.059</td><td style="text-align:center;">17.6</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <div class="mobileonly">
    <div class="reflist-upper-alpha"><div class="mw-references-wrap"><ol class="references">
    <li id="cite_note-stacksize-52"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-stacksize_52-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-stacksize_52-1">b</a></sup></span> <span class="reference-text">The size of stacks (or for unstackable items, number) of this item on any given roll.</span>
    </li>
    <li id="cite_note-weight-53"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-weight_53-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-weight_53-1">b</a></sup></span> <span class="reference-text">The weight of this item relative to other items in the pool.</span>
    </li>
    <li id="cite_note-chance-54"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chance_54-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chance_54-1">b</a></sup></span> <span class="reference-text">The odds of finding any of this item in a single chest.</span>
    </li>
    <li id="cite_note-items-55"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-items_55-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-items_55-1">b</a></sup></span> <span class="reference-text">The number of items expected per chest, averaged over a large number of chests.</span>
    </li>
    <li id="cite_note-chests-56"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chests_56-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chests_56-1">b</a></sup></span> <span class="reference-text">The average number of chests the player should expect to search to find any of this item.</span>
    </li>
    </ol></div></div>
    </div>
    <p><br>
    </p>
    <h3><span class="mw-headline" id="Desert_House">Desert House</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><span class="mw-editsection-bracket">]</span></span></h3>
    <p>In <i><a href="/wiki/Java_Edition" title="Java Edition">Java Edition</a></i>, each village desert house chest contains 3–8 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_57-0" class="reference"><a href="#cite_note-stacksize-57">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_58-0" class="reference"><a href="#cite_note-weight-58">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_59-0" class="reference"><a href="#cite_note-chance-59">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_60-0" class="reference"><a href="#cite_note-items-60">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_61-0" class="reference"><a href="#cite_note-chests-61">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Wheat" title="Wheat"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-192px -576px"></span><span class="sprite-text">Wheat</span></a></td>
    <td style="text-align:center;" data-sort-value="4">1–7</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>36</sub></td><td style="text-align:center;">80.6%</td><td style="text-align:center;">6.111</td><td style="text-align:center;">1.2</td></tr>
    <tr>
    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>36</sub></td><td style="text-align:center;">80.6%</td><td style="text-align:center;">3.819</td><td style="text-align:center;">1.2</td></tr>
    <tr>
    <td><a href="/wiki/Cactus" title="Cactus"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-432px -464px"></span><span class="sprite-text">Cactus</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>36</sub></td><td style="text-align:center;">80.6%</td><td style="text-align:center;">3.819</td><td style="text-align:center;">1.2</td></tr>
    <tr>
    <td><a href="/wiki/Dead_Bush" title="Dead Bush"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-16px -560px"></span><span class="sprite-text">Dead Bush</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>36</sub></td><td style="text-align:center;">26.6%</td><td style="text-align:center;">0.611</td><td style="text-align:center;">3.8</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>36</sub></td><td style="text-align:center;">14.3%</td><td style="text-align:center;">0.306</td><td style="text-align:center;">7.0</td></tr>
    <tr>
    <td><a href="/wiki/Book" title="Book"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-192px -528px"></span><span class="sprite-text">Book</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>36</sub></td><td style="text-align:center;">14.3%</td><td style="text-align:center;">0.153</td><td style="text-align:center;">7.0</td></tr>
    <tr>
    <td><a href="/wiki/Clay_Ball" title="Clay Ball"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-160px -544px"></span><span class="sprite-text">Clay Ball</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>36</sub></td><td style="text-align:center;">14.3%</td><td style="text-align:center;">0.153</td><td style="text-align:center;">7.0</td></tr>
    <tr>
    <td><a href="/wiki/Dye" title="Dye"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-176px -592px"></span><span class="sprite-text">Green Dye</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>36</sub></td><td style="text-align:center;">14.3%</td><td style="text-align:center;">0.153</td><td style="text-align:center;">7.0</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <p>In <i><a href="/wiki/Bedrock_Edition" title="Bedrock Edition">Bedrock Edition</a></i>, each village desert house chest contains 3–8 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_57-1" class="reference"><a href="#cite_note-stacksize-57">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_58-1" class="reference"><a href="#cite_note-weight-58">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_59-1" class="reference"><a href="#cite_note-chance-59">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_60-1" class="reference"><a href="#cite_note-items-60">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_61-1" class="reference"><a href="#cite_note-chests-61">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Wheat" title="Wheat"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-192px -576px"></span><span class="sprite-text">Wheat</span></a></td>
    <td style="text-align:center;" data-sort-value="4">1–7</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>36</sub></td><td style="text-align:center;">80.6%</td><td style="text-align:center;">6.111</td><td style="text-align:center;">1.2</td></tr>
    <tr>
    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>36</sub></td><td style="text-align:center;">80.6%</td><td style="text-align:center;">3.819</td><td style="text-align:center;">1.2</td></tr>
    <tr>
    <td><a href="/wiki/Cactus" title="Cactus"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-432px -464px"></span><span class="sprite-text">Cactus</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>36</sub></td><td style="text-align:center;">80.6%</td><td style="text-align:center;">3.819</td><td style="text-align:center;">1.2</td></tr>
    <tr>
    <td><a href="/wiki/Dead_Bush" title="Dead Bush"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-16px -560px"></span><span class="sprite-text">Dead Bush</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>36</sub></td><td style="text-align:center;">26.6%</td><td style="text-align:center;">0.611</td><td style="text-align:center;">3.8</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>36</sub></td><td style="text-align:center;">14.3%</td><td style="text-align:center;">0.306</td><td style="text-align:center;">7.0</td></tr>
    <tr>
    <td><a href="/wiki/Book" title="Book"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-192px -528px"></span><span class="sprite-text">Book</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>36</sub></td><td style="text-align:center;">14.3%</td><td style="text-align:center;">0.153</td><td style="text-align:center;">7.0</td></tr>
    <tr>
    <td><a href="/wiki/Clay_Ball" title="Clay Ball"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-160px -544px"></span><span class="sprite-text">Clay Ball</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>36</sub></td><td style="text-align:center;">14.3%</td><td style="text-align:center;">0.153</td><td style="text-align:center;">7.0</td></tr>
    <tr>
    <td><a href="/wiki/Dye" title="Dye"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-176px -592px"></span><span class="sprite-text">Green Dye</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>36</sub></td><td style="text-align:center;">14.3%</td><td style="text-align:center;">0.153</td><td style="text-align:center;">7.0</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <div class="mobileonly">
    <div class="reflist-upper-alpha"><div class="mw-references-wrap"><ol class="references">
    <li id="cite_note-stacksize-57"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-stacksize_57-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-stacksize_57-1">b</a></sup></span> <span class="reference-text">The size of stacks (or for unstackable items, number) of this item on any given roll.</span>
    </li>
    <li id="cite_note-weight-58"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-weight_58-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-weight_58-1">b</a></sup></span> <span class="reference-text">The weight of this item relative to other items in the pool.</span>
    </li>
    <li id="cite_note-chance-59"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chance_59-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chance_59-1">b</a></sup></span> <span class="reference-text">The odds of finding any of this item in a single chest.</span>
    </li>
    <li id="cite_note-items-60"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-items_60-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-items_60-1">b</a></sup></span> <span class="reference-text">The number of items expected per chest, averaged over a large number of chests.</span>
    </li>
    <li id="cite_note-chests-61"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chests_61-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chests_61-1">b</a></sup></span> <span class="reference-text">The average number of chests the player should expect to search to find any of this item.</span>
    </li>
    </ol></div></div>
    </div>
    <p><br>
    </p>
    <h3><span class="mw-headline" id="Plain_House">Plain House</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><span class="mw-editsection-bracket">]</span></span></h3>
    <p>In <i><a href="/wiki/Java_Edition" title="Java Edition">Java Edition</a></i>, each village plains house chest contains 3–8 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_62-0" class="reference"><a href="#cite_note-stacksize-62">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_63-0" class="reference"><a href="#cite_note-weight-63">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_64-0" class="reference"><a href="#cite_note-chance-64">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_65-0" class="reference"><a href="#cite_note-items-65">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_66-0" class="reference"><a href="#cite_note-chests-66">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Potato" title="Potato"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-224px -496px"></span><span class="sprite-text">Potato</span></a></td>
    <td style="text-align:center;" data-sort-value="4">1–7</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>43</sub></td><td style="text-align:center;">74.2%</td><td style="text-align:center;">5.116</td><td style="text-align:center;">1.3</td></tr>
    <tr>
    <td><a href="/wiki/Apple" title="Apple"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-48px -480px"></span><span class="sprite-text">Apple</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>43</sub></td><td style="text-align:center;">74.2%</td><td style="text-align:center;">3.837</td><td style="text-align:center;">1.3</td></tr>
    <tr>
    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>43</sub></td><td style="text-align:center;">74.2%</td><td style="text-align:center;">3.198</td><td style="text-align:center;">1.3</td></tr>
    <tr>
    <td><a href="/wiki/Sapling" title="Sapling"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-544px -464px"></span><span class="sprite-text">Oak Sapling</span></a></td>
    <td style="text-align:center;" data-sort-value="1.5">1–2</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>43</sub></td><td style="text-align:center;">48.2%</td><td style="text-align:center;">0.959</td><td style="text-align:center;">2.1</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>43</sub></td><td style="text-align:center;">22.8%</td><td style="text-align:center;">0.640</td><td style="text-align:center;">4.4</td></tr>
    <tr>
    <td><a href="/wiki/Flower" title="Flower"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-192px -560px"></span><span class="sprite-text">Dandelion</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>43</sub></td><td style="text-align:center;">22.8%</td><td style="text-align:center;">0.256</td><td style="text-align:center;">4.4</td></tr>
    <tr>
    <td><a href="/wiki/Gold_nugget" class="mw-redirect" title="Gold nugget"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-64px -560px"></span><span class="sprite-text">Gold Nugget</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>43</sub></td><td style="text-align:center;">12.1%</td><td style="text-align:center;">0.256</td><td style="text-align:center;">8.3</td></tr>
    <tr>
    <td><a href="/wiki/Book" title="Book"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-192px -528px"></span><span class="sprite-text">Book</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>43</sub></td><td style="text-align:center;">12.1%</td><td style="text-align:center;">0.128</td><td style="text-align:center;">8.3</td></tr>
    <tr>
    <td><a href="/wiki/Feather" title="Feather"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-240px -544px"></span><span class="sprite-text">Feather</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>43</sub></td><td style="text-align:center;">12.1%</td><td style="text-align:center;">0.128</td><td style="text-align:center;">8.3</td></tr>
    <tr>
    <td><a href="/wiki/Flower" title="Flower"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-304px -560px"></span><span class="sprite-text">Poppy</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>43</sub></td><td style="text-align:center;">12.1%</td><td style="text-align:center;">0.128</td><td style="text-align:center;">8.3</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <p>In <i><a href="/wiki/Bedrock_Edition" title="Bedrock Edition">Bedrock Edition</a></i>, each village plains house chest contains 3–8 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_62-1" class="reference"><a href="#cite_note-stacksize-62">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_63-1" class="reference"><a href="#cite_note-weight-63">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_64-1" class="reference"><a href="#cite_note-chance-64">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_65-1" class="reference"><a href="#cite_note-items-65">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_66-1" class="reference"><a href="#cite_note-chests-66">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Potato" title="Potato"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-224px -496px"></span><span class="sprite-text">Potato</span></a></td>
    <td style="text-align:center;" data-sort-value="4">1–7</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>43</sub></td><td style="text-align:center;">74.2%</td><td style="text-align:center;">5.116</td><td style="text-align:center;">1.3</td></tr>
    <tr>
    <td><a href="/wiki/Apple" title="Apple"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-48px -480px"></span><span class="sprite-text">Apple</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>43</sub></td><td style="text-align:center;">74.2%</td><td style="text-align:center;">3.837</td><td style="text-align:center;">1.3</td></tr>
    <tr>
    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>43</sub></td><td style="text-align:center;">74.2%</td><td style="text-align:center;">3.198</td><td style="text-align:center;">1.3</td></tr>
    <tr>
    <td><a href="/wiki/Sapling" title="Sapling"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-544px -464px"></span><span class="sprite-text">Oak Sapling</span></a></td>
    <td style="text-align:center;" data-sort-value="1.5">1–2</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>43</sub></td><td style="text-align:center;">48.2%</td><td style="text-align:center;">0.959</td><td style="text-align:center;">2.1</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>43</sub></td><td style="text-align:center;">22.8%</td><td style="text-align:center;">0.640</td><td style="text-align:center;">4.4</td></tr>
    <tr>
    <td><a href="/wiki/Flower" title="Flower"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-192px -560px"></span><span class="sprite-text">Dandelion</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>43</sub></td><td style="text-align:center;">22.8%</td><td style="text-align:center;">0.256</td><td style="text-align:center;">4.4</td></tr>
    <tr>
    <td><a href="/wiki/Gold_nugget" class="mw-redirect" title="Gold nugget"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-64px -560px"></span><span class="sprite-text">Gold Nugget</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>43</sub></td><td style="text-align:center;">12.1%</td><td style="text-align:center;">0.256</td><td style="text-align:center;">8.3</td></tr>
    <tr>
    <td><a href="/wiki/Book" title="Book"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-192px -528px"></span><span class="sprite-text">Book</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>43</sub></td><td style="text-align:center;">12.1%</td><td style="text-align:center;">0.128</td><td style="text-align:center;">8.3</td></tr>
    <tr>
    <td><a href="/wiki/Feather" title="Feather"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-240px -544px"></span><span class="sprite-text">Feather</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>43</sub></td><td style="text-align:center;">12.1%</td><td style="text-align:center;">0.128</td><td style="text-align:center;">8.3</td></tr>
    <tr>
    <td><a href="/wiki/Flower" title="Flower"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-304px -560px"></span><span class="sprite-text">Poppy</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>43</sub></td><td style="text-align:center;">12.1%</td><td style="text-align:center;">0.128</td><td style="text-align:center;">8.3</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <div class="mobileonly">
    <div class="reflist-upper-alpha"><div class="mw-references-wrap"><ol class="references">
    <li id="cite_note-stacksize-62"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-stacksize_62-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-stacksize_62-1">b</a></sup></span> <span class="reference-text">The size of stacks (or for unstackable items, number) of this item on any given roll.</span>
    </li>
    <li id="cite_note-weight-63"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-weight_63-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-weight_63-1">b</a></sup></span> <span class="reference-text">The weight of this item relative to other items in the pool.</span>
    </li>
    <li id="cite_note-chance-64"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chance_64-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chance_64-1">b</a></sup></span> <span class="reference-text">The odds of finding any of this item in a single chest.</span>
    </li>
    <li id="cite_note-items-65"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-items_65-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-items_65-1">b</a></sup></span> <span class="reference-text">The number of items expected per chest, averaged over a large number of chests.</span>
    </li>
    <li id="cite_note-chests-66"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chests_66-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chests_66-1">b</a></sup></span> <span class="reference-text">The average number of chests the player should expect to search to find any of this item.</span>
    </li>
    </ol></div></div>
    </div>
    <p><br>
    </p>
    <h3><span class="mw-headline" id="Savanna_House">Savanna House</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><span class="mw-editsection-bracket">]</span></span></h3>
    <p>In <i><a href="/wiki/Java_Edition" title="Java Edition">Java Edition</a></i>, each village savanna house chest contains 3–8 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_67-0" class="reference"><a href="#cite_note-stacksize-67">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_68-0" class="reference"><a href="#cite_note-weight-68">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_69-0" class="reference"><a href="#cite_note-chance-69">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_70-0" class="reference"><a href="#cite_note-items-70">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_71-0" class="reference"><a href="#cite_note-chests-71">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Wheat_seeds" class="mw-redirect" title="Wheat seeds"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-144px -0px"></span><span class="sprite-text">Wheat Seeds</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>46</sub></td><td style="text-align:center;">71.7%</td><td style="text-align:center;">3.587</td><td style="text-align:center;">1.4</td></tr>
    <tr>
    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>46</sub></td><td style="text-align:center;">71.7%</td><td style="text-align:center;">2.989</td><td style="text-align:center;">1.4</td></tr>
    <tr>
    <td><a href="/wiki/Sapling" title="Sapling"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-480px -464px"></span><span class="sprite-text">Acacia Sapling</span></a></td>
    <td style="text-align:center;" data-sort-value="1.5">1–2</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>46</sub></td><td style="text-align:center;">71.7%</td><td style="text-align:center;">1.793</td><td style="text-align:center;">1.4</td></tr>
    <tr>
    <td><a href="/wiki/Grass" title="Grass"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-48px -560px"></span><span class="sprite-text">Grass</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>46</sub></td><td style="text-align:center;">45.9%</td><td style="text-align:center;">0.598</td><td style="text-align:center;">2.2</td></tr>
    <tr>
    <td><a href="/wiki/Grass" title="Grass"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-112px -560px"></span><span class="sprite-text">Tall Grass</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>46</sub></td><td style="text-align:center;">45.9%</td><td style="text-align:center;">0.598</td><td style="text-align:center;">2.2</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>46</sub></td><td style="text-align:center;">21.5%</td><td style="text-align:center;">0.598</td><td style="text-align:center;">4.7</td></tr>
    <tr>
    <td><a href="/wiki/Gold_nugget" class="mw-redirect" title="Gold nugget"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-64px -560px"></span><span class="sprite-text">Gold Nugget</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>46</sub></td><td style="text-align:center;">11.3%</td><td style="text-align:center;">0.239</td><td style="text-align:center;">8.8</td></tr>
    <tr>
    <td><a href="/wiki/Torch" title="Torch"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-480px -512px"></span><span class="sprite-text">Torch</span></a></td>
    <td style="text-align:center;" data-sort-value="1.5">1–2</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>46</sub></td><td style="text-align:center;">11.3%</td><td style="text-align:center;">0.179</td><td style="text-align:center;">8.8</td></tr>
    <tr>
    <td><a href="/wiki/Bucket" title="Bucket"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-112px -448px"></span><span class="sprite-text">Bucket</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>46</sub></td><td style="text-align:center;">11.3%</td><td style="text-align:center;">0.120</td><td style="text-align:center;">8.8</td></tr>
    <tr>
    <td><a href="/wiki/Saddle" title="Saddle"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -528px"></span><span class="sprite-text">Saddle</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>46</sub></td><td style="text-align:center;">11.3%</td><td style="text-align:center;">0.120</td><td style="text-align:center;">8.8</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <p>In <i><a href="/wiki/Bedrock_Edition" title="Bedrock Edition">Bedrock Edition</a></i>, each village savanna house chest contains 3–8 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_67-1" class="reference"><a href="#cite_note-stacksize-67">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_68-1" class="reference"><a href="#cite_note-weight-68">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_69-1" class="reference"><a href="#cite_note-chance-69">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_70-1" class="reference"><a href="#cite_note-items-70">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_71-1" class="reference"><a href="#cite_note-chests-71">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Wheat_seeds" class="mw-redirect" title="Wheat seeds"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-144px -0px"></span><span class="sprite-text">Wheat Seeds</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>46</sub></td><td style="text-align:center;">71.7%</td><td style="text-align:center;">3.587</td><td style="text-align:center;">1.4</td></tr>
    <tr>
    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>46</sub></td><td style="text-align:center;">71.7%</td><td style="text-align:center;">2.989</td><td style="text-align:center;">1.4</td></tr>
    <tr>
    <td><a href="/wiki/Sapling" title="Sapling"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-480px -464px"></span><span class="sprite-text">Acacia Sapling</span></a></td>
    <td style="text-align:center;" data-sort-value="1.5">1–2</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>46</sub></td><td style="text-align:center;">71.7%</td><td style="text-align:center;">1.793</td><td style="text-align:center;">1.4</td></tr>
    <tr>
    <td><a href="/wiki/Grass" title="Grass"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-48px -560px"></span><span class="sprite-text">Grass</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>46</sub></td><td style="text-align:center;">45.9%</td><td style="text-align:center;">0.598</td><td style="text-align:center;">2.2</td></tr>
    <tr>
    <td><a href="/wiki/Grass" title="Grass"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-112px -560px"></span><span class="sprite-text">Tall Grass</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>46</sub></td><td style="text-align:center;">45.9%</td><td style="text-align:center;">0.598</td><td style="text-align:center;">2.2</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>46</sub></td><td style="text-align:center;">21.5%</td><td style="text-align:center;">0.598</td><td style="text-align:center;">4.7</td></tr>
    <tr>
    <td><a href="/wiki/Gold_nugget" class="mw-redirect" title="Gold nugget"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-64px -560px"></span><span class="sprite-text">Gold Nugget</span></a></td>
    <td style="text-align:center;" data-sort-value="2">1–3</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>46</sub></td><td style="text-align:center;">11.3%</td><td style="text-align:center;">0.239</td><td style="text-align:center;">8.8</td></tr>
    <tr>
    <td><a href="/wiki/Torch" title="Torch"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-480px -512px"></span><span class="sprite-text">Torch</span></a></td>
    <td style="text-align:center;" data-sort-value="1.5">1–2</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>46</sub></td><td style="text-align:center;">11.3%</td><td style="text-align:center;">0.179</td><td style="text-align:center;">8.8</td></tr>
    <tr>
    <td><a href="/wiki/Bucket" title="Bucket"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-112px -448px"></span><span class="sprite-text">Bucket</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>46</sub></td><td style="text-align:center;">11.3%</td><td style="text-align:center;">0.120</td><td style="text-align:center;">8.8</td></tr>
    <tr>
    <td><a href="/wiki/Saddle" title="Saddle"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-80px -528px"></span><span class="sprite-text">Saddle</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>46</sub></td><td style="text-align:center;">11.3%</td><td style="text-align:center;">0.120</td><td style="text-align:center;">8.8</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <div class="mobileonly">
    <div class="reflist-upper-alpha"><div class="mw-references-wrap"><ol class="references">
    <li id="cite_note-stacksize-67"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-stacksize_67-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-stacksize_67-1">b</a></sup></span> <span class="reference-text">The size of stacks (or for unstackable items, number) of this item on any given roll.</span>
    </li>
    <li id="cite_note-weight-68"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-weight_68-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-weight_68-1">b</a></sup></span> <span class="reference-text">The weight of this item relative to other items in the pool.</span>
    </li>
    <li id="cite_note-chance-69"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chance_69-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chance_69-1">b</a></sup></span> <span class="reference-text">The odds of finding any of this item in a single chest.</span>
    </li>
    <li id="cite_note-items-70"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-items_70-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-items_70-1">b</a></sup></span> <span class="reference-text">The number of items expected per chest, averaged over a large number of chests.</span>
    </li>
    <li id="cite_note-chests-71"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chests_71-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chests_71-1">b</a></sup></span> <span class="reference-text">The average number of chests the player should expect to search to find any of this item.</span>
    </li>
    </ol></div></div>
    </div>
    <p><br>
    </p>
    <h3><span class="mw-headline" id="Snowy_House">Snowy House</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><span class="mw-editsection-bracket">]</span></span></h3>
    <p>In <i><a href="/wiki/Java_Edition" title="Java Edition">Java Edition</a></i>, each village snowy house chest contains 3–8 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_72-0" class="reference"><a href="#cite_note-stacksize-72">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_73-0" class="reference"><a href="#cite_note-weight-73">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_74-0" class="reference"><a href="#cite_note-chance-74">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_75-0" class="reference"><a href="#cite_note-items-75">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_76-0" class="reference"><a href="#cite_note-chests-76">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Potato" title="Potato"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-224px -496px"></span><span class="sprite-text">Potato</span></a></td>
    <td style="text-align:center;" data-sort-value="4">1–7</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>53</sub></td><td style="text-align:center;">66.3%</td><td style="text-align:center;">4.151</td><td style="text-align:center;">1.5</td></tr>
    <tr>
    <td><a href="/wiki/Snowball" title="Snowball"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-32px -448px"></span><span class="sprite-text">Snowball</span></a></td>
    <td style="text-align:center;" data-sort-value="4">1–7</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>53</sub></td><td style="text-align:center;">66.3%</td><td style="text-align:center;">4.151</td><td style="text-align:center;">1.5</td></tr>
    <tr>
    <td><a href="/wiki/Beetroot_seeds" class="mw-redirect" title="Beetroot seeds"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-144px -576px"></span><span class="sprite-text">Beetroot Seeds</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>53</sub></td><td style="text-align:center;">66.3%</td><td style="text-align:center;">3.113</td><td style="text-align:center;">1.5</td></tr>
    <tr>
    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>53</sub></td><td style="text-align:center;">66.3%</td><td style="text-align:center;">2.594</td><td style="text-align:center;">1.5</td></tr>
    <tr>
    <td><a href="/wiki/Coal" title="Coal"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-176px -544px"></span><span class="sprite-text">Coal</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>53</sub></td><td style="text-align:center;">41.2%</td><td style="text-align:center;">1.297</td><td style="text-align:center;">2.4</td></tr>
    <tr>
    <td><a href="/wiki/Snow_Block" title="Snow Block"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-544px -416px"></span><span class="sprite-text">Snow Block</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="4"><sup>4</sup>⁄<sub>53</sub></td><td style="text-align:center;">34.5%</td><td style="text-align:center;">0.415</td><td style="text-align:center;">2.9</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>53</sub></td><td style="text-align:center;">9.9%</td><td style="text-align:center;">0.259</td><td style="text-align:center;">10.1</td></tr>
    <tr>
    <td><a href="/wiki/Beetroot_soup" class="mw-redirect" title="Beetroot soup"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-112px -480px"></span><span class="sprite-text">Beetroot Soup</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>53</sub></td><td style="text-align:center;">9.9%</td><td style="text-align:center;">0.104</td><td style="text-align:center;">10.1</td></tr>
    <tr>
    <td><a href="/wiki/Blue_ice" class="mw-redirect" title="Blue ice"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-384px -256px"></span><span class="sprite-text">Blue Ice</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>53</sub></td><td style="text-align:center;">9.9%</td><td style="text-align:center;">0.104</td><td style="text-align:center;">10.1</td></tr>
    <tr>
    <td><a href="/wiki/Furnace" title="Furnace"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-400px -464px"></span><span class="sprite-text">Furnace</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>53</sub></td><td style="text-align:center;">9.9%</td><td style="text-align:center;">0.104</td><td style="text-align:center;">10.1</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <p>In <i><a href="/wiki/Bedrock_Edition" title="Bedrock Edition">Bedrock Edition</a></i>, each village snowy house chest contains 3–8 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_72-1" class="reference"><a href="#cite_note-stacksize-72">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_73-1" class="reference"><a href="#cite_note-weight-73">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_74-1" class="reference"><a href="#cite_note-chance-74">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_75-1" class="reference"><a href="#cite_note-items-75">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_76-1" class="reference"><a href="#cite_note-chests-76">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Potato" title="Potato"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-224px -496px"></span><span class="sprite-text">Potato</span></a></td>
    <td style="text-align:center;" data-sort-value="4">1–7</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>53</sub></td><td style="text-align:center;">66.3%</td><td style="text-align:center;">4.151</td><td style="text-align:center;">1.5</td></tr>
    <tr>
    <td><a href="/wiki/Snowball" title="Snowball"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-32px -448px"></span><span class="sprite-text">Snowball</span></a></td>
    <td style="text-align:center;" data-sort-value="4">1–7</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>53</sub></td><td style="text-align:center;">66.3%</td><td style="text-align:center;">4.151</td><td style="text-align:center;">1.5</td></tr>
    <tr>
    <td><a href="/wiki/Beetroot_seeds" class="mw-redirect" title="Beetroot seeds"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-144px -576px"></span><span class="sprite-text">Beetroot Seeds</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>53</sub></td><td style="text-align:center;">66.3%</td><td style="text-align:center;">3.113</td><td style="text-align:center;">1.5</td></tr>
    <tr>
    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>53</sub></td><td style="text-align:center;">66.3%</td><td style="text-align:center;">2.594</td><td style="text-align:center;">1.5</td></tr>
    <tr>
    <td><a href="/wiki/Coal" title="Coal"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-176px -544px"></span><span class="sprite-text">Coal</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>53</sub></td><td style="text-align:center;">41.2%</td><td style="text-align:center;">1.297</td><td style="text-align:center;">2.4</td></tr>
    <tr>
    <td><a href="/wiki/Snow_Block" title="Snow Block"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-544px -416px"></span><span class="sprite-text">Snow Block</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="4"><sup>4</sup>⁄<sub>53</sub></td><td style="text-align:center;">34.5%</td><td style="text-align:center;">0.415</td><td style="text-align:center;">2.9</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>53</sub></td><td style="text-align:center;">9.9%</td><td style="text-align:center;">0.259</td><td style="text-align:center;">10.1</td></tr>
    <tr>
    <td><a href="/wiki/Beetroot_soup" class="mw-redirect" title="Beetroot soup"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-112px -480px"></span><span class="sprite-text">Beetroot Soup</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>53</sub></td><td style="text-align:center;">9.9%</td><td style="text-align:center;">0.104</td><td style="text-align:center;">10.1</td></tr>
    <tr>
    <td><a href="/wiki/Blue_ice" class="mw-redirect" title="Blue ice"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-384px -256px"></span><span class="sprite-text">Blue Ice</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>53</sub></td><td style="text-align:center;">9.9%</td><td style="text-align:center;">0.104</td><td style="text-align:center;">10.1</td></tr>
    <tr>
    <td><a href="/wiki/Furnace" title="Furnace"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-400px -464px"></span><span class="sprite-text">Furnace</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>53</sub></td><td style="text-align:center;">9.9%</td><td style="text-align:center;">0.104</td><td style="text-align:center;">10.1</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <div class="mobileonly">
    <div class="reflist-upper-alpha"><div class="mw-references-wrap"><ol class="references">
    <li id="cite_note-stacksize-72"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-stacksize_72-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-stacksize_72-1">b</a></sup></span> <span class="reference-text">The size of stacks (or for unstackable items, number) of this item on any given roll.</span>
    </li>
    <li id="cite_note-weight-73"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-weight_73-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-weight_73-1">b</a></sup></span> <span class="reference-text">The weight of this item relative to other items in the pool.</span>
    </li>
    <li id="cite_note-chance-74"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chance_74-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chance_74-1">b</a></sup></span> <span class="reference-text">The odds of finding any of this item in a single chest.</span>
    </li>
    <li id="cite_note-items-75"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-items_75-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-items_75-1">b</a></sup></span> <span class="reference-text">The number of items expected per chest, averaged over a large number of chests.</span>
    </li>
    <li id="cite_note-chests-76"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chests_76-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chests_76-1">b</a></sup></span> <span class="reference-text">The average number of chests the player should expect to search to find any of this item.</span>
    </li>
    </ol></div></div>
    </div>
    <p><br>
    </p>
    <h3><span class="mw-headline" id="Taiga_House">Taiga House</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><span class="mw-editsection-bracket">]</span></span></h3>
    <p>In <i><a href="/wiki/Java_Edition" title="Java Edition">Java Edition</a></i>, each village taiga house chest contains 3–8 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_77-0" class="reference"><a href="#cite_note-stacksize-77">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_78-0" class="reference"><a href="#cite_note-weight-78">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_79-0" class="reference"><a href="#cite_note-chance-79">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_80-0" class="reference"><a href="#cite_note-items-80">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_81-0" class="reference"><a href="#cite_note-chests-81">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Potato" title="Potato"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-224px -496px"></span><span class="sprite-text">Potato</span></a></td>
    <td style="text-align:center;" data-sort-value="4">1–7</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>54</sub></td><td style="text-align:center;">65.6%</td><td style="text-align:center;">4.074</td><td style="text-align:center;">1.5</td></tr>
    <tr>
    <td><a href="/wiki/Log" title="Log"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-160px -432px"></span><span class="sprite-text">Spruce Log</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>54</sub></td><td style="text-align:center;">65.6%</td><td style="text-align:center;">3.056</td><td style="text-align:center;">1.5</td></tr>
    <tr>
    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>54</sub></td><td style="text-align:center;">65.6%</td><td style="text-align:center;">2.546</td><td style="text-align:center;">1.5</td></tr>
    <tr>
    <td><a href="/wiki/Sweet_berries" class="mw-redirect" title="Sweet berries"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-96px -384px"></span><span class="sprite-text">Sweet Berries</span></a></td>
    <td style="text-align:center;" data-sort-value="4">1–7</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>54</sub></td><td style="text-align:center;">40.6%</td><td style="text-align:center;">2.037</td><td style="text-align:center;">2.5</td></tr>
    <tr>
    <td><a href="/wiki/Pumpkin_seeds" class="mw-redirect" title="Pumpkin seeds"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -48px"></span><span class="sprite-text">Pumpkin Seeds</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>54</sub></td><td style="text-align:center;">40.6%</td><td style="text-align:center;">1.528</td><td style="text-align:center;">2.5</td></tr>
    <tr>
    <td><a href="/wiki/Sapling" title="Sapling"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-560px -464px"></span><span class="sprite-text">Spruce Sapling</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>54</sub></td><td style="text-align:center;">40.6%</td><td style="text-align:center;">1.528</td><td style="text-align:center;">2.5</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>54</sub></td><td style="text-align:center;">18.6%</td><td style="text-align:center;">0.509</td><td style="text-align:center;">5.4</td></tr>
    <tr>
    <td><a href="/wiki/Grass" title="Grass"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-32px -560px"></span><span class="sprite-text">Fern</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>54</sub></td><td style="text-align:center;">18.6%</td><td style="text-align:center;">0.204</td><td style="text-align:center;">5.4</td></tr>
    <tr>
    <td><a href="/wiki/Grass" title="Grass"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-64px -560px"></span><span class="sprite-text">Large Fern</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>54</sub></td><td style="text-align:center;">18.6%</td><td style="text-align:center;">0.204</td><td style="text-align:center;">5.4</td></tr>
    <tr>
    <td><a href="/wiki/Iron_nugget" class="mw-redirect" title="Iron nugget"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-240px -272px"></span><span class="sprite-text">Iron Nugget</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>54</sub></td><td style="text-align:center;">9.7%</td><td style="text-align:center;">0.306</td><td style="text-align:center;">10.3</td></tr>
    <tr>
    <td><a href="/wiki/Pumpkin_pie" class="mw-redirect" title="Pumpkin pie"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-240px -496px"></span><span class="sprite-text">Pumpkin Pie</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>54</sub></td><td style="text-align:center;">9.7%</td><td style="text-align:center;">0.102</td><td style="text-align:center;">10.3</td></tr>
    <tr>
    <td><a href="/wiki/Sign" title="Sign"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-16px -896px"></span><span class="sprite-text">Spruce Sign</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>54</sub></td><td style="text-align:center;">9.7%</td><td style="text-align:center;">0.102</td><td style="text-align:center;">10.3</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <p>In <i><a href="/wiki/Bedrock_Edition" title="Bedrock Edition">Bedrock Edition</a></i>, each village taiga house chest contains 3–8 item stacks,  with the following distribution:
    </p>
    <div style="overflow:auto">
    <table class="wikitable sortable jquery-tablesorter">
    <thead><tr>
    <th rowspan="1" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"> Item </th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The size of stacks (or for unstackable items, number) of this item on any given roll."> Stack Size </abbr> <span class="mobileonly"><sup id="cite_ref-stacksize_77-1" class="reference"><a href="#cite_note-stacksize-77">[A]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The weight of this item relative to other items in the pool."> Weight </abbr> <span class="mobileonly"> <sup id="cite_ref-weight_78-1" class="reference"><a href="#cite_note-weight-78">[B]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The odds of finding any of this item in a single chest."> Chance </abbr> <span class="mobileonly"> <sup id="cite_ref-chance_79-1" class="reference"><a href="#cite_note-chance-79">[C]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The number of items expected per chest, averaged over a large number of chests."> Avg.<br>per chest </abbr> <span class="mobileonly"> <sup id="cite_ref-items_80-1" class="reference"><a href="#cite_note-items-80">[D]</a></sup></span></th>
    <th class="headersort headerSort" role="columnheader button" data-sort-type="number" tabindex="0" title="Sort ascending"> <abbr title="The average number of chests the player should expect to search to find any of this item."> Avg. # chests<br>to search </abbr> <span class="mobileonly"> <sup id="cite_ref-chests_81-1" class="reference"><a href="#cite_note-chests-81">[E]</a></sup></span></th>
    </tr></thead><tbody><tr>

    <td><a href="/wiki/Potato" title="Potato"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-224px -496px"></span><span class="sprite-text">Potato</span></a></td>
    <td style="text-align:center;" data-sort-value="4">1–7</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>49</sub></td><td style="text-align:center;">69.3%</td><td style="text-align:center;">4.490</td><td style="text-align:center;">1.4</td></tr>
    <tr>
    <td><a href="/wiki/Log" title="Log"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-160px -432px"></span><span class="sprite-text">Spruce Log</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>49</sub></td><td style="text-align:center;">69.3%</td><td style="text-align:center;">3.367</td><td style="text-align:center;">1.4</td></tr>
    <tr>
    <td><a href="/wiki/Bread" title="Bread"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-128px -480px"></span><span class="sprite-text">Bread</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="10"><sup>10</sup>⁄<sub>49</sub></td><td style="text-align:center;">69.3%</td><td style="text-align:center;">2.806</td><td style="text-align:center;">1.4</td></tr>
    <tr>
    <td><a href="/wiki/Pumpkin_seeds" class="mw-redirect" title="Pumpkin seeds"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -48px"></span><span class="sprite-text">Pumpkin Seeds</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>49</sub></td><td style="text-align:center;">43.7%</td><td style="text-align:center;">1.684</td><td style="text-align:center;">2.3</td></tr>
    <tr>
    <td><a href="/wiki/Sapling" title="Sapling"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-560px -464px"></span><span class="sprite-text">Spruce Sapling</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="5"><sup>5</sup>⁄<sub>49</sub></td><td style="text-align:center;">43.7%</td><td style="text-align:center;">1.684</td><td style="text-align:center;">2.3</td></tr>
    <tr>
    <td><a href="/wiki/Emerald" title="Emerald"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-208px -544px"></span><span class="sprite-text">Emerald</span></a></td>
    <td style="text-align:center;" data-sort-value="2.5">1–4</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>49</sub></td><td style="text-align:center;">20.3%</td><td style="text-align:center;">0.561</td><td style="text-align:center;">4.9</td></tr>
    <tr>
    <td><a href="/wiki/Grass" title="Grass"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-32px -560px"></span><span class="sprite-text">Fern</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>49</sub></td><td style="text-align:center;">20.3%</td><td style="text-align:center;">0.224</td><td style="text-align:center;">4.9</td></tr>
    <tr>
    <td><a href="/wiki/Grass" title="Grass"><span class="sprite block-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/df/BlockCSS.png/revision/latest?cb=20240117193413&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;cb=20230918142842&amp;version=1695047332160);background-position:-64px -560px"></span><span class="sprite-text">Large Fern</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="2"><sup>2</sup>⁄<sub>49</sub></td><td style="text-align:center;">20.3%</td><td style="text-align:center;">0.224</td><td style="text-align:center;">4.9</td></tr>
    <tr>
    <td><a href="/wiki/Iron_nugget" class="mw-redirect" title="Iron nugget"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-240px -272px"></span><span class="sprite-text">Iron Nugget</span></a></td>
    <td style="text-align:center;" data-sort-value="3">1–5</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>49</sub></td><td style="text-align:center;">10.7%</td><td style="text-align:center;">0.337</td><td style="text-align:center;">9.4</td></tr>
    <tr>
    <td><a href="/wiki/Sign" title="Sign"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-240px -880px"></span><span class="sprite-text">Oak Sign</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>49</sub></td><td style="text-align:center;">10.7%</td><td style="text-align:center;">0.112</td><td style="text-align:center;">9.4</td></tr>
    <tr>
    <td><a href="/wiki/Pumpkin_pie" class="mw-redirect" title="Pumpkin pie"><span class="sprite item-sprite" style="background-image:url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f5/ItemCSS.png/revision/latest?cb=20231218214619);background-position:-240px -496px"></span><span class="sprite-text">Pumpkin Pie</span></a></td>
    <td style="text-align:center;" data-sort-value="1">1</td><td style="text-align:center;" data-sort-value="1"><sup>1</sup>⁄<sub>49</sub></td><td style="text-align:center;">10.7%</td><td style="text-align:center;">0.112</td><td style="text-align:center;">9.4</td></tr>
    </tbody><tfoot></tfoot></table></div>
    <div class="mobileonly">
    <div class="reflist-upper-alpha"><div class="mw-references-wrap"><ol class="references">
    <li id="cite_note-stacksize-77"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-stacksize_77-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-stacksize_77-1">b</a></sup></span> <span class="reference-text">The size of stacks (or for unstackable items, number) of this item on any given roll.</span>
    </li>
    <li id="cite_note-weight-78"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-weight_78-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-weight_78-1">b</a></sup></span> <span class="reference-text">The weight of this item relative to other items in the pool.</span>
    </li>
    <li id="cite_note-chance-79"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chance_79-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chance_79-1">b</a></sup></span> <span class="reference-text">The odds of finding any of this item in a single chest.</span>
    </li>
    <li id="cite_note-items-80"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-items_80-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-items_80-1">b</a></sup></span> <span class="reference-text">The number of items expected per chest, averaged over a large number of chests.</span>
    </li>
    <li id="cite_note-chests-81"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-chests_81-0"><span class="cite-accessibility-label">Jump up to: </span>a</a></sup> <sup><a href="#cite_ref-chests_81-1">b</a></sup></span> <span class="reference-text">The average number of chests the player should expect to search to find any of this item.</span>
    </li>
    </ol></div></div>
    </div>
    <p><br>
    </p>
    <!--
    NewPP limit report
    Cached time: 20240413133705
    Cache expiry: 1209600
    Reduced expiry: false
    Complications: [show‐toc]
    CPU time usage: 0.508 seconds
    Real time usage: 0.539 seconds
    Preprocessor visited node count: 4858/1000000
    Post‐expand include size: 708776/2097152 bytes
    Template argument size: 756/2097152 bytes
    Highest expansion depth: 13/100
    Expensive parser function count: 2/100
    Unstrip recursion depth: 0/20
    Unstrip post‐expand size: 39836/5000000 bytes
    Lua time usage: 0.252/7.000 seconds
    Lua memory usage: 6332780/104857600 bytes
    ExtLoops count: 0/200
    -->
    <!--
    Transclusion expansion time report (%,ms,calls,template)
    100.00%  295.562      1 Village/Loot
    100.00%  295.562      1 -total
    96.33%  284.715     16 Template:LootChest
    1.93%    5.702      1 Template:In
    1.44%    4.266      1 Template:Editions
    -->
    </div></div>
    </div>""")
]

    def linksLoot_htmlLoots_dataframeStructuresLoots(linksLoot,htmlsLoot):
      dataframeLoots1 , dataframeStructuresLoots1 = linksLoot_dataframeLoots_dataframeStructuresLoots(linksLoot)
      dataframeLoots2 , dataframeStructuresLoots2 = htmlsLoot_dataframeLoots_dataframeStructuresLoots(htmlsLoot)
      return pd.concat([dataframeLoots1,dataframeLoots2],ignore_index=True) , pd.concat([dataframeStructuresLoots1,dataframeStructuresLoots2],ignore_index=True)

    def linksLoot_dataframeLoots_dataframeStructuresLoots(linksLoot):
      dataframeLoots = {}
      dataframeStructuresLoots = []
      for linkLoot , indexTables in linksLoot:
        if indexTables != []:
          dataLoots , dataStructureLoots = linkLoot_dataLoots_dataStructureLoots(linkLoot,indexTables)
          dataframeLoots.update(dataLoots)
          dataframeStructuresLoots.extend(dataStructureLoots)
      dataColumnsLoots = ['identifier','name','rarity','renewable','stackable']
      dataColumnsStructuresLoots = ['structure_identifier','loot_identifier','stack_size_lower','stack_size_upper','chance']
      dataframeLoots = list(map(lambda item: [item[0]]+item[1],dataframeLoots.items()))
      dataframeLoots = pd.DataFrame(data=dataframeLoots,columns=dataColumnsLoots)
      dataframeStructuresLoots = pd.DataFrame(data=dataframeStructuresLoots,columns=dataColumnsStructuresLoots)
      return dataframeLoots , dataframeStructuresLoots

    def linkLoot_dataLoots_dataStructureLoots(linkLoot,indexTables):
      textLoot = linkLoot_textLoot(linkLoot)
      dataLoots = {}
      dataStructureLoots = []
      for tableLoot in textLoot_tablesLoot(textLoot,indexTables):
        tableLoot = tableLoot_tableLoot(tableLoot)
        dataTableLoots , dataTableStructureLoots = tableLoot_dataTableLoots_dataTableStructureLoots(tableLoot,linkLoot)
        dataLoots.update(dataTableLoots)
        dataStructureLoots.extend(dataTableStructureLoots)
      return dataLoots , dataStructureLoots

    def textLoot_tablesLoot(textLoot,indexTables):
      tablesLoot = []
      for tableLoot in textLoot.find_all(name='table'):
        if tableLoot.find(name='th'):
          if tableLoot.find(name='th').text.strip() == 'Item' or tableLoot.find(name='th').text.strip() == 'item':
            tablesLoot.append(tableLoot)
      for indexTable in indexTables:
        yield tablesLoot[indexTable]

    def tableLoot_tableLoot(tableLoot):
      return tableLoot.find_all(name='tr')[2:]

    def tableLoot_dataTableLoots_dataTableStructureLoots(tableLoot,linkLoot):
      dataTableLoots = {}
      dataTableStructureLoots = []
      dataIdentifierStructure = linkLoot_dataIdentifierStructure(linkLoot)
      for rowTableLoot in tableLoot:
        if (rowTableLoot.find(name='td').text != 'Nothing[F]') and (rowTableLoot.find(name='td').text != 'Nothing[G]') and (rowTableLoot.find(name='td').text != 'Nothing'):
         dataNameLoot , dataStackSizeLowLoot , dataStackSizeUpperLoot , chanceLoot , dataLinkLoot = rowTableLoot_dataRowLoot(rowTableLoot)
         rarity , renewable , stackable = dataLinkLoot_dataAdditionalLoot(dataLinkLoot)
         dataIdentifierLoot = dataNameLoot_dataIdentifierLoot(dataNameLoot)
         dataTableLoots.update({dataIdentifierLoot:[dataNameLoot,rarity,renewable,stackable]})
         dataTableStructureLoots.append((dataIdentifierStructure,dataIdentifierLoot,dataStackSizeLowLoot,dataStackSizeUpperLoot,chanceLoot))
      return dataTableLoots , dataTableStructureLoots

    def linkLoot_dataIdentifierStructure(linkLoot):
      dataIdentifierStructure = ''
      for charIdentifierStructure in linkLoot.lower()[::-1]:
        if charIdentifierStructure == '/':
          return dataIdentifierStructure[::-1]
        elif charIdentifierStructure == '#':
          return dataIdentifierStructure[:0:-1]
        else:
          dataIdentifierStructure += charIdentifierStructure

    def rowTableLoot_dataRowLoot(rowTableLoot):
      dataNameLoot = rowTableLoot.find(name='td').text.title()
      dataLinkLoot = 'https://minecraft.fandom.com' + rowTableLoot.find(name='a')['href']
      for columnTableLoot in rowTableLoot.find_all(name='td')[1:]:
        columnTextTableLoot= columnTableLoot.text
        if columnTextTableLoot != '–':
          if '–' in columnTextTableLoot or columnTextTableLoot in '0123456789':
            stackSizeLoot = columnTextTableLoot
            continue
          if '%' in columnTextTableLoot:
            chanceLoot = columnTextTableLoot[:-1]
            break
      dataNameLoot = dataNameLoot_dataNameNormalizeLoot(dataNameLoot)
      return dataNameLoot , *stackSizeLoot_stackSizeLoot(stackSizeLoot) , chanceLoot , dataLinkLoot

    def dataNameLoot_dataNameNormalizeLoot(dataNameLoot):
      dataNameNormalizeLoot = ''
      for charNameLoot in dataNameLoot:
        if charNameLoot == '[':
          break
        else:
          dataNameNormalizeLoot += charNameLoot
      return dataNameNormalizeLoot

    def stackSizeLoot_stackSizeLoot(stackSizeLoot):
      if '–' in stackSizeLoot:
        indexStackSizeLoot = stackSizeLoot.index('–')
        dataStackSizeLowLoot = stackSizeLoot[:indexStackSizeLoot]
        dataStackSizeUpperLoot = stackSizeLoot[indexStackSizeLoot+1:]
      else:
        dataStackSizeLowLoot = stackSizeLoot
        dataStackSizeUpperLoot = stackSizeLoot
      return dataStackSizeLowLoot , dataStackSizeUpperLoot

    def dataLinkLoot_dataAdditionalLoot(dataLinkLoot):
      textItemLoot = linkLoot_textLoot(dataLinkLoot)
      asideItemLoot = textItemLoot.find(name='aside')
      rarity , renewable , stackable = 'Common' , 'Yes' , '64'
      for rowAsideItemLoot in asideItemLoot.find_all(name='div',recursive=False):
        if rowAsideItemLoot.find(name='h3') and rowAsideItemLoot.find(name='div'):
          attributeNameItemLoot , attributeValueItemLoot = rowAsideItemLoot.find(name='h3').text.strip() , rowAsideItemLoot.find(name='div').text.strip()
          if (attributeNameItemLoot == 'Rarity color') or (attributeNameItemLoot == 'Rarity'):
            rarity = attributeValueItemLoot
          elif attributeNameItemLoot == 'Renewable':
            if 'Yes' in attributeValueItemLoot:
              renewable = 'Yes'
            else:
              renewable = 'No'
          elif attributeNameItemLoot == 'Stackable':
            if attributeValueItemLoot == 'No':
              stackable = '1'
            elif '64' in attributeValueItemLoot:
              stackable = '64'
            elif '16' in attributeValueItemLoot:
              stackable = '16'
            break
      return rarity , renewable , stackable

    def dataNameLoot_dataIdentifierLoot(dataNameLoot):
      return '_'.join(dataNameLoot.lower().split())

    def htmlsLoot_dataframeLoots_dataframeStructuresLoots(htmlsLoot):
      dataframeLoots = {}
      dataframeStructuresLoots = []
      for linkLoot , indexTables , htmlLoot in htmlsLoot:
        textLoot = htmlLoot_textLoot(htmlLoot)
        dataLoots , dataStructureLoots = textLoot_dataLoots_dataStructureLoots(linkLoot,indexTables,textLoot)
        dataframeLoots.update(dataLoots)
        dataframeStructuresLoots.extend(dataStructureLoots)
      dataColumnsLoots = ['identifier','name','rarity','renewable','stackable']
      dataColumnsStructuresLoots = ['structure_identifier','loot_identifier','stack_size_lower','stack_size_upper','chance']
      dataframeLoots = list(map(lambda item: [item[0]]+item[1],dataframeLoots.items()))
      dataframeLoots = pd.DataFrame(data=dataframeLoots,columns=dataColumnsLoots)
      dataframeStructuresLoots = pd.DataFrame(data=dataframeStructuresLoots,columns=dataColumnsStructuresLoots)
      return dataframeLoots , dataframeStructuresLoots

    def htmlLoot_textLoot(htmlLoot):
      return BeautifulSoup(htmlLoot,'html.parser')

    def textLoot_dataLoots_dataStructureLoots(linkLoot,indexTables,textLoot):
      dataLoots = {}
      dataStructureLoots = []
      for tableLoot in textLoot_tablesLoot(textLoot,indexTables):
        tableLoot = tableLoot_tableLoot(tableLoot)
        dataTableLoots , dataTableStructureLoots = tableLoot_dataTableLoots_dataTableStructureLoots(tableLoot,linkLoot)
        dataLoots.update(dataTableLoots)
        dataStructureLoots.extend(dataTableStructureLoots)
      return dataLoots , dataStructureLoots

    dataframeLoots , dataframeStructuresLoots = linksLoot_htmlLoots_dataframeStructuresLoots(linksLoot,htmlsLoot)

    dataframe_json([dataframeLoots,dataframeStructuresLoots],['jsonLoots','jsonStructures_Loots'])

if __name__=='__main__':
    jsonLoots()