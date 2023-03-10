####################################################################################################################
#  Each quest record contains the following fields:
#  1) Info page id: used for referencing info pages in other files. The prefix ip_ is automatically added before each info page id.
#  2) Info page name: Name displayed in the info page screen.
#
####################################################################################################################

info_pages = [
 ("armies_size", "Army Size", "The size of your army, similar to the armies of the lords, depends on several factors:^^\
Leadership: each point will increase the maximum size of your army by 5. Companions with Leadership help lead the party.^^\
Charisma: each point of your charisma will increase the maximum size of your army by 1. It is your ability to attract men to your cause.^^\
Renown: every 9 points will increase the maximum size of your army by 1. Fame attracts followers.^^\
Holdings: every town will add 80 men and each fort 40 to the maximum size of your army. These spots represent men you can raise through a levy.^^\
Bear in mind that party size at sea is restricted by ship capacity. Extra troops can always be left at a settlement garrison, player Refuge (once built), or any Camp Quarters."),
 ("morale", "Morale", "Morale represents the ability and willingness of the troops in a party to summon up the endurance, bravery, and discipline they need to face the stresses of battle and the march. It is not the same thing as the troops' happiness. Elite troops may grumble and whine about the hardships of campaigning -- but then stand together as one when the arrows start to fly. On the other hand, a commander who gives his men everything they want may find that they grow soft, and waiver before the enemy's charge.^^Morale's greatest impact is on a party's behavior in battle, determining how aggressively troops engage the enemy, and how likely they are to break and run if they perceive the tide of battle turning against them. Morale also affects a party's march speed, as a less motivated party will move more slowly, as the men are not pushing themselves to their physical limit, and pause more frequently, as it waits for stragglers to catch up. Finally, a party with very low morale will start to suffer desertions.^^Some factors that affect morale are intuitive. For example, a charismatic commander with a reputation for winning battles can infuse his or her men with a sense of confidence. Leaders who give their men well ample and varied supplies of food, and pay them on time, demonstrate that they care about their troops' welfare and are less likely to lead them into disaster.^^Other factors are less intuitive -- particularly those related to a party's sense of group cohesion. In a small tight-knit party, for example, men will often fight hard against daunting odds to avoid showing cowardice before their comrades-in-arms. A large party on the other hand may see its cohesion strained, as the commander has less time to supervise the men, listen to their grievances, and resolve their disputes. Frequent battles will strengthen the bonds between men, while long periods without combat will see the troops become bored and quarrelsome.^^The morale report, accessible by hitting the 'Party Info' button on the 'Character' screen, will give the player a sense of the factors affecting his or her men's morale."),
 ("economy", "Economy", "Towns and villages in the Northlands need a wide variety of goods for their populations to remain healthy and productive. First in importance is food. Grain is the staple crop of the Northlands, but people also need fat and protein in the form of meat, fish, or cheese. It takes almost as much work to preserve meat as to produce it in the first place, so salt is also in high demand. After food comes clothing: heavy wool, lighter linens, or luxurious velvet. Finally, people need the tools of their trade: ironware, pottery, leatherware, and, of course, arms, armor, and horses for war.^^Most agricultural products are produced in the villages, while artisans in the towns specialize in manufactured or artisanal goods like fabrics or ironware. Also, different resources can be found in different parts of the country. Consequently, the key to prosperity in the Northlands is trade -- both between the villages and the towns, and between the major towns themselves.^^When trade flows, goods will be available and affordable, the population of a settlement will be healthy and energetic, and migrants will flock from the nearby regions. The settlement will produce more, consume more, and be able to contribute more in taxes to their lords. When trade dries up, towns and villages will see their workers flee to seek work elsewhere, and economic activity will drift to a stand-still. Thus, it is in the interests of rulers to protect trade routes from the hazards of war and banditry. A smart merchant, however, may want to seek out towns which have become isolated from the rest of the land, as he or she may be able to turn a tidy profit from the resulting price imbalances.^^Because villagers usually plan to take their goods to market in towns, village markets will be rather quiet places, and villagers will buy cheap and sell dear. Serious merchants will stick to the towns to make a profit, although some parties may decide to make a quick stop in a village to acquire supplies.^^A player who wants to know about the factors affecting a region's prosperity can speak to the mayor of the local town. Other information can be gleaned from passers-by, although they might not know very much outside of their own particular trade."),
 ("courtship", "Courtship", "You may wish to marry into one of the Northlands' noble families. Marriage is not necessary for someone to rise in power and stature, but it does provide them with an opportunity to improve their relation with lords and establish a claim to the throne.^^Marriage requirements will be different for males and females. A male character will usually need to pursue a traditional path of courtship. He should establish a reputation in aristocratic society, get on good terms with his bride's parents or guardians, and then woo the lady according to local custom. If a player grows impatient, he may attempt to take a shortcut -- but there will be consequences in his relations with other lords.^^A male character should keep in mind that other lords will be competing with him for the affections of the kingdom's ladies. Also, a lady's tastes are unpredictable, and a player may also find that the object of his love does not love him in return. Romance, in the Northlands as elsewhere, does not always prosper. Of course, a player may resort to other, less gentlemanly means of winning a lady's heart, but again, that will have a serious impact on his reputation.^^To get started on the path of courtship, a male player should try to get involved in the social life of the aristocracy of the Northlands, attending feasts and tournaments. Also, wandering troubadours and poets can serve as a useful repository of information on courtship, and keep the player up to date about the latest gossip.^^Female characters can also marry -- but they should keep in mind that these societies are very traditional, and, as adventurers, they have chosen a very unconventional path for a woman. A female character may have to look for a while to find a lord who is open-minded enough to marry her.^^On the bright side, a female character does not have to go through the elaborate rituals of courtship, and she also may gain more from a marriage than her male counterpart. For a woman adventurer, marriage can be a quick path to power -- and an unscrupulous character may be able to use her husband as a tool of her political ambitions."),
 ("politics", "Politics", "The realms of the Northlands, although they represent different cultures, all shared a basic political system that preceded feudalism. At the top of Germanic social hierarchy was the king, elected by a council of noblemen from the royal house. All the land of the realm belonged to the king, who distributed it among the aristocracy and the warriors who had performed outstanding deeds. This land however did not become their property and in case of death, either the king or the client, returned to the ruler. \
The nobility governed each shire in king's name with the responsibility for administration and justice, raising and leading the levies of men to the battlefield. For this purpose they divided their land into smaller parcels among the freemen who formed the backbone of the rural economy of the kingdom. These farmers and householders paid rent to their overlord and/or had several duties with him, such as building fortifications or working some days of the week during the harvest-time.^^\
This system of clientship was also practised between nobles, which established hierarchies of homage and political support. The increasingly powerful monasteries were autonomous ecclesiastical establishments with their own land and clients.^^\
A distinctive feature of the Celtic societies (Gaelic, Welsh and Pictish) was the importance of the corporate lineage-group, the clan. A large group of related people supposedly descended from one common ancestor, acting as an independent social and legal entity.^^\
When one realm in the Northlands makes war on another, the political unity of each kingdom is as important as the quality or number of its soldiers in determining the outcome. In a cohesive kingdom, nobles will join together in a large force to sweep their opponents before them. In a kingdom divided by petty quarrels, lords will fail to respond to the marshal's summons, or drift away to attend to their own business if a campaign is not going well. A faction's political cohesion will also impact warfare when campaigns are not in progress. In a divided faction, lords will be less likely to join together on raids and patrols or to come to each other's defense.^^If it seems nobles' bickering and quarrels are self-defeating when the enemy is just around the corner, keep in mind that ultimately, a noble's loyalty doesn't belong to a particular faction or culture, but to himself and to his family. If a noble fears that his faction is collapsing, or if he is being neglected by his liege, he can usually find a reason to withdraw his oath of allegiance and change sides. Players should keep this in mind, as they may find that there are opportunities to turn discontented former enemies into allies."),
 ("character_backgrounds", "Character_Backgrounds", "A player character in the Northlands may choose to come from a variety of social backgrounds. This choice will affect not just his or her starting skills and equipment, but also the course of his or her career as an adventurer.^^War and politics in the Northlands are traditionally dominated by male aristocrats. A nobleman player character may find that he is invited into this 'old boys' club' fairly quickly, but women and commoners may face a few extra hurdles on the way. If you choose to start the game as a male nobleman, you can think of it as the 'easy' setting. Starting as a noblewoman or a male commoner is somewhat more difficult, and starting as a female commoner is probably the most challenging way to begin a game.^^However, women have some starting advantages. Simply by taking up arms, a female warrior will draw attention to herself, and she may find that she can build up her reputation faster than a male. Also, it is traditionally easier for a woman to marry up the social ladder than it is for a man, and a woman may find she can gain more from a strategic marital alliance than her male counterpart.^^Finally, keep in mind that the game does not place any limits on the upward mobility of characters based on their background. Noble or common, male or female, married or unmarried -- anyone can rise to become ruler of all the Northlands, if they are sufficiently brave, lucky, or resourceful."),
 ("military_campaigns", "Military Campaigns", "When kingdoms in the Northlands go to war, their armies have two basic offensive options. They can try to attack villages and lay waste to the countryside, damaging their enemy's prestige and economy. Or, they can try to seize and hold castles or towns, taking territory. The second option can involve long, bloody sieges, but will yield more decisive results.^^It is important to note that the realms of the Northlands do not field standing armies, which remain in the field as long as the ruler desires. Rather, the realms of the Northlands are protected by the nobles, their companions, and the feudal levies they raise.  Sometimes, these nobles launch their own private attacks into enemy territory, but the most decisive events will usually take place when the great hosts are assembled. The kingdom's marshal, a noble appointed by the king, will summon the host before the campaign and lead them out to battle. However, he should be careful not to keep them in the field for too long. Otherwise, the host will begin to disintegrate, as the vassals drift off to pursue their own business, and the army will be vulnerable to a counter-attack.^^For this reason, the rhythm of wars in the Northlands often resemble the rhythm of a duel between two individual combatants. One side will gather its strength and seek to land a blow against the enemy's territory. If the marshal spends too little time gathering the vassals, he may not be able to do any real damage. If he spends too much time, then the campaign may end before it has even begun. A large realm will have an advantage over a smaller one, just as a brawny combatant has an edge over a smaller foe, but a realm's political cohesion can also be a factor, just as a fighter with great stamina can outlast her opponent. Sometimes, the armies of two realms will meet head on, resulting in a major battle in which both numbers and morale will decide the outcome.^^Kingdoms will have imperfect intelligence about their enemies. Attacking lords will need to frequently scout enemy territory to determine which fortresses may be vulnerable. An army defending its homeland will benefit from the alarms raised by castles and towns, which broadcast intelligence about enemy movements in the area. Such intelligence will be imprecise, however, particularly when it comes to numbers. A defending force which sets out to raise a siege or rescue a village may be able to overwhelm an unprepared attacker -- or it may miscalculate, and find that it is the one to be overwhelmed. Attackers, in turn, must be careful how far they advance into enemy territory, with aggressive marshals venturing further than cautious ones.^^Players will be expected to join in their faction's military campaign, either by joining the host, or by scouting ahead into enemy territory. Some players may find that their realm's marshal is too cautious, or too aggressive, for their tastes. In this case, they can intrigue with other lords to try to replace the marshal, or build support to become the marshal themselves.^^Most wars are of limited duration. A king who goes to war will, for the sake of honor, feel obligated to pursue the conflict for a short while. However, unless he is soundly beating his enemy, he may soon start looking for a way out of the conflict, lest he leave himself vulnerable to an attack by a third party. The Northlands' rulers are keenly aware that today's ally may be tomorrow's enemy, and vice versa."),
 ("siege_warfare","Siege Warfare", "Viking Conquest offers siege warfare accurate to the Dark Ages period. When the player besieges a settlement, two paths can be taken to conquer the place: by debilitation (hunger, diseases ...) or by assault.^^\
In the former case, the player's goal is to blockade the settlement and prevent it from receiving supplies or reinforcements. At the same time various actions can be performed to undermine morale, spread disease or destroy the food reserves of the settlement. This type of action will take longer, but also avoid a large number of casualties.^^\
In the latter case, direct action is undertaken, provided assault equipment is available or preparatory actions have been taken, such as wearing down the defenders or burning their houses and walls. This option should be used when the player feels ready to launch a full-scale assault to conquer the settlement. It has the advantage of leading to success more quickly, but usually at a relatively high cost in lives.^^\
In addition, when the settlement has a port, the player may equip a fleet and assault the port, leading an assault from the sea.^^\
The complexity and characteristics of the new siege system are too numerous to describe here in detail. The best thing is to discover and develop strategies on your own."),
 ("sea_travel","Sea Travel", "\
Ferries on the world map transport your party between two stations. While this is cheap when your party is small, \
it becomes more expensive with party size.^\
^\
To travel longer distances on the sea, one may travel from one port town to another. This can be initiated from the town \
menu or by talking to the shipwright in the port part of the town scene. Similar to ferries, this service becomes more expensive with party size.^\
^\
Once you have your own ship, you may embark from the port it is in by clicking on 'Sail from port' in the town menu. You will return to the map, but this time at sea on your ship. \
Sea travel then works much like land travel.^\
^\
There are two different ways to get back on land. \
You can either click on a port or use a landing point. \
To find a landing point, travel closely along the coast or right click on your party and select 'find closest landing point.' \
As with ports, click on the landing point to disembark. \
In either case, your ships will remain at the position where you landed.^\
^\
If your party's size is greater than the capacity of your ships, you won't be able to embark. \
In this case, you can establish troop quarters (Camp menu) at your \
current position and another troop quarters at your target position, then transport your army step by step between both quarters.^\
^\
When traveling by sea on the campaign map, you can always check the current weather. After clicking on the 'Camp' button, current conditions are \
shown on the left side. If the weather conditions change, you will be notified by a message in the \
lower left corner of the screen.^\
^\
On the one hand, windy weather is good for the speed of your ships on the campaign map and in sea battles. On the other hand, \
the chance that it will damage your ships also increases. \
Damage worsens the condition of a ship, slowing it or even destroying when the condition reaches 'Dangerous.' \
You may check the conditions of your ships by clicking on 'Camp' and then on 'Fleet.'^\
^\
Finally, the weather also determines the behaviour of ships in battle. This can always be checked beforehand by clicking 'Camp' and then on 'Check location.'^\
^\
Sea travel is dangerous and can lower the morale of your troops. When this happens, you will be notified by a message. \
Troops especially dislike spending the night on the water. Therefore, consider plotting your route to make landfall by night. \
If morale on the sea gets too low, troops may mutiny.^\
^\
Some troops like Sailors and certain Norse troops are experienced seamen and will increase the travel speed of your ships on the campaign map. \
You can check the effect on the left side of the camp menu.^\
^\
If there is more than one ship in your fleet, the speed of the fleet is determined by its slowest ship. \
However, as soon as you have more than one ship in your fleet, you can split the fleet. To do so, travel close to a shore. Then click on 'Camp', 'Fleet' \
and finally on 'Leave ship at shore' to leave the slower ship(s) there. To bring ships together again, one needs to bring them all to a port. \
To get a overview of all your ships at their location, click on 'Character' and then on 'Ships.'\
"),
 ("sea_battle","Sea Battle", "\
At some point after starting to travel on the sea, you will participate in a naval battle.^\
^\
First of all, you need to know how to control your ship. You can give the command to row forward, fast forward, backwards, or stay. \
The up and down arrow keys switch between these commands. \
You can also give the command to go straight, starboard, hard starboard, port or hard port. The left and right arrow keys switch between these \
commands.^\
^\
Current commands are represented by arrows around the representation of your ship in the upper right corner. Press Enter to set the \
sail and Backspace to get a tactical view of the scene. Try these commands to get a feeling for steering a ship and the effect of the wind.^\
^\
As soon as you get close enough to an enemy ship, boarding will commence. The ships are lashed together and the fight starts.^\
If you are lucky, you may capture the enemy flagship after winning the fight.^\
^\
In a sea battle where you have several ships, you can give a 'stand ground' or 'charge' command to your ships, which are assigned to the ninth 'division.' \
The first troops in your army list will be together with you on the flagship. \
The other troops will be in the remaining ships. One can change one's flagship in a port or while camping on the sea.^\
^\
With a reasonably large fleet, one may attack towns from their sea sides. \
To do so, simply click on the enemy port town and you will have option to attack it once you reach it without first disembarking.\
"),
 ("ship_info","Ships", "\
Sooner or later, you'll want to invest in a ship. There are several reasons to do this. Over the long term, it is the cheapest form of sea travel. It gives you complete \
freedom in movement on the sea. It opens new opportunities for trading and raiding.^\
^\
On the other hand, there are downsides. First of \
all, a ship is expensive, and you will have to save up some money to afford one. Furthermore, a ship can carry only a limited amount of troops.^\
^\
Another important consideration is speed. \
With a faster ship, you will more successfully catch or flee from other ships. \
The speed of a ship is determined by its type and condition.^\
^\
Finally the wood used for ship construction affects its durability. \
While ships made of oak wood are very durable, ships made of beech wood need to be repaired more often.^\
^\
When you feel ready to buy a ship, click on 'See the ships' in the town menu of a port town or talk to the shipwright. \
Port towns can have up to three ships for sale, but sometimes none are available. The type and amount of ships offered changes over time. While all \
port towns offer ships, one finds the best ships in Norse and Frisian ports. \
To see your ship, you can click on 'See the ships' in the town menu or walk to its pier.^\
^\
In a port, one may customize the sail of a ship or paint any ship made of oak. \
There is one special sail which is reserved for the ships of the player. It can be changed with a dedicated graphic editor \
(not included in Viking Conquest). For further information, see the 'Your Custom Sails' folder among the files of this DLC.^\
^\
Once you have a ship, the shipwright will interact with you in a different way and won't hesitate to offer advice. \
Shipwrights also offer to custom build ships. Better ships may require special materials that you will need \
to obtain and bring with you. Better ships also require more time for their construction and the more talented shipwrights in Norse ports. \
The first seven ships you have built can be named freely in the ship customization menu.^\
"),
 ("wounds","Wounds", "The player may receive specific, debilitating wounds in battle. Physicians in larger towns will treat these wounds for a price, after which they will heal within a few days. Any negative effects will then be removed. If wound is not treated after some time, it will change to a scar, and the negative effects will then be permanent."),
("traits","Traits", "When you reach level 13, you can get one of these traits depending on your skill choices:^^\
Berserker: Going berserk will give you momentary improved speed and strength in the heat of the battle. This brutal ferocity will make your vision turn red.^^\
Inspiring: This acquired skill will increase your leadership in battle as your war cries strengthen the fierceness of your men in combat.^^\
Tough: This skill will make your troops move faster and increase their agility in the battle.^^\
Strong: Your preoccupation with the maintenance of your men's shields and armors will make it harder for the enemy to wound them.^^\
Use key T to activate these traits on the battlefield."),
("recruitment", "Recruitment", "Recruitment in Viking Conquest is not automatic but depends on a number of factors.^^Firstly, in order to recruit in a village, fort or town, you need to obtain the permission of its lord. To do this, you'll need to have enough renown (150+) and be on good terms with the lord and his faction.^^\
For villages, you can also obtain permission from the village leader. For this route, you may use high renown (150+) and high relations (15+), or you can just try bribery. Bribing may or may not work, so you may have to try to bribe the leader more than once.^^\
Once permission is obtained, you are free to recruit as long as your relations with the settlement remain positive. In villages you may be able to recruit tier 1 troops. If have high enough relations (60+), you may be able to recruit tier 2 troops. If you happen to be the village's lord, you need only 20+ relations to do this.^^\
In castles and towns, you maybe able to recruit tier 2 troops. If your relations with the place are high enough (30+), there is 30% chance you may get a tier 3 troop. The maximum number of troops that you may be able to recruit is determined by your relations with the \
settlement, your leadership, your charisma, your religion, the predominant religion of the settlement, and whether or not you are the lord of the place.^^\
Other options are available. If you're Christian, you may be able to find some desperate refugees in monasteries. There is always a chance to find fellows looking for work at farmsteads."),
("wages", "Wages", "Troop wages in Viking Conquest are affected primarily by the player's leadership. For higher level troops, the player's persuasion skill may become a bonus or a malus, depending on how good it is. For outlaw type troops, such as Robbers and Vikings, the player's reputation comes into play, giving a discount if player's reputation is worse than Notorious."),
("skills", "Skills and Attributes", "When creating or developing a character in Viking Conquest, one has to pay attention to the many skills and attributes. Skills like persuasion and leadership are essential for trading, wages, lord and lady interaction, and forced conversion. Attributes such as intelligence and charisma are also essential in these activities, but will also affect your ability to marry or lead people.^\
^\
There are three important skills for the sea: 'Sea King,' 'Navigation' and 'Looting.'^\
^\
One's Sea King level determines the amount of ships one can command. Level one allows up to two ships. Seven ships are the maximum \
at the Sea King level of four.^\
^\
The Navigation skill allows one to travel faster on the sea. It is the naval equivalent of the Pathfinding skill on land (which, by the way, will not help on the sea).^\
^\
A higher Looting skill results in a higher chance of capturing enemy ships.^\
"), 
("tactical_controls", "Tactical Controls", "Use the keyboard NUMBERS to select a division. Press 0 to select your entire force.^^\
Use F1-F4 to order selected divisions. Keep the F1 key down to place selected divisions. You may target an enemy division through this mechanism.^^\
Pressing the ENTER key often initiates an overhead Strategy Camera.^^\
Pressing the BACKSPACE key often initiates a Battle Command Display with 'radar.^^\
Pressing the H key will make your horse come to you (requires riding skill of 4 or higher).^^\
Pressing the Z key will enable Crouching.^^\
Holding the game key for Defending and pressing the game key for Action will execute a Shield Bash.^^\
Once you have developed a Trait, pressing the T key will activate it.^^\
In Multiplayer, holding the Q key and pressing the key for Defending will allow you to Taunt your opponents.'"),  #copied from str_tactical_controls
("division_placement", "Division Placement", "When ONE division is selected, the center of its front rank is placed at the spot indicated.^^\
When MANY divisions are selected, they are separated and spread out as if the player were standing at the spot indicated.^^\
One may memorize the placement of selected divisions relative to the player by pressing F2, F7. Default is infantry to the left, cavalry right, and ranged forward. Placement is overridden for any division the player chooses to personally head through the Formations Options menu.^^\
If the camp menu game option is set, divisions will rotate to face the enemy. Otherwise, they will maintain the facing that the player had when they were placed."),  #mostly copied from str_division_placement
("formations", "Formations", "The Complex Formations on the Battle Menu are:^^\
- RANKS with best troops up front^\
- SHIELD WALL, ranks with shields in front and longer weapons in back^\
- WEDGE with best troops up front^\
- SQUARE in no particular order^\
- NO FORMATION^^\
Even in the last case, the player can make formations up to four lines by ordering Stand Closer enough times."),  #mostly copied from str_formations
 ("dog_companion","Dog Companion", "While wandering about, lost in your own thoughts, you suddenly hear a dog bark at you. \
Luckily, you have a piece of sausage with you. It's the beginning of a companionship. The dog will not leave your side, even on the battlefield, \
and soon earns a name.^\
On the battlefield, your dog is placed in division 9. The skills and abilities of your dog companion can be improved by giving him good food."),#VC-3197
("rents", "Rents", "Every settlement that you own generates rents. Rents are paid weekly on average over a long term, but the frequency of payment is variable. Some weeks you may get payments, and during others you may get nothing. If the payment hasn't been processed by paydate, the entry in your budget will state that the rents were unpaid. If the village is looted, or fort or town is plundered, the entry in your \
budget will state that no rents are available. Once the village/fort/town is back to normal state, they will restart processing rent payments. Rents are also affected by prosperity of the settlement, presence of any special buildings, religious composition, tax rate and difficulty settings. Special buildings will continue generating rents even if the place is plundered."),
("quarters", "Quarters", "\
Quarters allow you leave some of your troops at a particular location on the map. You can have up to two quarters.^^\
There are several scenarios which make quarters useful:^\
- If you need to travel on a boat, but you can't afford to pay passage for all your troops^\
- If the capacity of your fleet isn't big enough to transport all your troops at the same time^\
- If you want to sneak into a town^\
- If you want to travel faster over the world map"),
 ]
