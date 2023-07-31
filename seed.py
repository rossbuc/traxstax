from app import db
from models.user import User
from models.song import Song
from models.tracklist import Tracklist
from models.tracklists import Tracklists

import click

from flask.cli import with_appcontext

@click.command(name='seed')
@with_appcontext

def seed():
    Tracklists.query.delete()
    Tracklist.query.delete()
    User.query.delete()
    Song.query.delete()

    user1 = User(username="rosbuc", password="12345678", profile_image="/static/img/user_1_profile_pic.jpg", bio="The first user")
    user2 = User(username="jerrysmith", password="iamlame", profile_image="p", bio="The second user")
    user3 = User(username="mp3daddy", password="123thethe", profile_image="p", bio="The third user")
    user4 = User(username="waxnotflacs", password="123$moothoperator", profile_image="p", bio="The fourth user")

    song1 = Song(name="How High", artist="The Salsoul Orchestra", album="How High", genre="Disco")
    song2 = Song(name="Young Hearts Run Free", artist="Candi Staton", album="Young Hearts Run Free", genre="Disco")
    song3 = Song(name="Respect", artist="Aretha Franklin", album="Aretha Now", genre="Soul")
    song4 = Song(name="Time To Move", artist="Carmen", album="Time To Move", genre="Boogie")
    song5 = Song(name="Always", artist="Brief Encounter", album="Always", genre="Gospel")
    song6 = Song(name="Find Your Love", artist="Mary Stevens", album="Find Your Love", genre="Boogie")
    song7 = Song(name="Dancing in the Moonlight", artist="Toploader", album="Onka's Big Moka", genre="Pop")
    song8 = Song(name="Bohemian Rhapsody", artist="Queen", album="A Night at the Opera", genre="Rock")
    song9 = Song(name="Shape of You", artist="Ed Sheeran", album="÷ (Divide)", genre="Pop")
    song10 = Song(name="Hotel California", artist="Eagles", album="Hotel California", genre="Rock")
    song11 = Song(name="Despacito", artist="Luis Fonsi ft. Daddy Yankee", album="Vida", genre="Reggaeton")
    song12 = Song(name="Thriller", artist="Michael Jackson", album="Thriller", genre="Pop")
    song13 = Song(name="Stairway to Heaven", artist="Led Zeppelin", album="Led Zeppelin IV", genre="Rock")
    song14 = Song(name="Billie Jean", artist="Michael Jackson", album="Thriller", genre="Pop")
    song15 = Song(name="Rolling in the Deep", artist="Adele", album="21", genre="Pop")
    song16 = Song(name="Imagine", artist="John Lennon", album="Imagine", genre="Rock")
    song17 = Song(name="Uptown Funk", artist="Mark Ronson ft. Bruno Mars", album="Uptown Special", genre="Funk")
    song18 = Song(name="Smooth", artist="Santana ft. Rob Thomas", album="Supernatural", genre="Rock")
    song19 = Song(name="Let It Be", artist="The Beatles", album="Let It Be", genre="Rock")
    song20 = Song(name="Shape of My Heart", artist="Sting", album="Ten Summoner's Tales", genre="Pop")
    song21 = Song(name="Like a Rolling Stone", artist="Bob Dylan", album="Highway 61 Revisited", genre="Rock")
    song22 = Song(name="Don't Stop Believin'", artist="Journey", album="Escape", genre="Rock")
    song23 = Song(name="Wonderwall", artist="Oasis", album="(What's the Story) Morning Glory?", genre="Rock")
    song24 = Song(name="Hallelujah", artist="Jeff Buckley", album="Grace", genre="Rock")
    song25 = Song(name="Viva la Vida", artist="Coldplay", album="Viva la Vida or Death and All His Friends", genre="Rock")
    song21 = Song(name="Stayin' Alive", artist="Bee Gees", album="Saturday Night Fever Soundtrack", genre="Disco")
    song22 = Song(name="Le Freak", artist="Chic", album="C'est Chic", genre="Disco")
    song23 = Song(name="I Will Survive", artist="Gloria Gaynor", album="Love Tracks", genre="Disco")
    song24 = Song(name="Don't Stop 'Til You Get Enough", artist="Michael Jackson", album="Off the Wall", genre="Disco")
    song25 = Song(name="Funkytown", artist="Lipps Inc.", album="Mouth to Mouth", genre="Disco")
    song26 = Song(name="Y.M.C.A.", artist="Village People", album="Cruisin'", genre="Disco")
    song27 = Song(name="Dancing Queen", artist="ABBA", album="Arrival", genre="Disco")
    song28 = Song(name="Super Freak", artist="Rick James", album="Street Songs", genre="Disco")
    song29 = Song(name="You Should Be Dancing", artist="Bee Gees", album="Children of the World", genre="Disco")
    song30 = Song(name="Car Wash", artist="Rose Royce", album="Car Wash Soundtrack", genre="Disco")
    song31 = Song(name="Boogie Wonderland", artist="Earth, Wind & Fire", album="I Am", genre="Disco")
    song32 = Song(name="Got to Be Real", artist="Cheryl Lynn", album="Cheryl Lynn", genre="Disco")
    song33 = Song(name="I'm Coming Out", artist="Diana Ross", album="diana", genre="Disco")
    song34 = Song(name="Don't Leave Me This Way", artist="Thelma Houston", album="Any Way You Like It", genre="Disco")
    song35 = Song(name="Ring My Bell", artist="Anita Ward", album="Songs of Love", genre="Disco")
    song36 = Song(name="Lady Marmalade", artist="Labelle", album="Nightbirds", genre="Disco")
    song37 = Song(name="You Make Me Feel (Mighty Real)", artist="Sylvester", album="Step II", genre="Disco")
    song38 = Song(name="Bad Girls", artist="Donna Summer", album="Bad Girls", genre="Disco")
    song39 = Song(name="Shake Your Groove Thing", artist="Peaches & Herb", album="2 Hot!", genre="Disco")
    song40 = Song(name="He's the Greatest Dancer", artist="Sister Sledge", album="We Are Family", genre="Disco")
    song41 = Song(name="Ain't No Sunshine", artist="Bill Withers", album="Just As I Am", genre="Soul")
    song42 = Song(name="Let's Stay Together", artist="Al Green", album="Let's Stay Together", genre="Soul")
    song43 = Song(name="Respect", artist="Aretha Franklin", album="I Never Loved a Man the Way I Love You", genre="Soul")
    song44 = Song(name="Stand by Me", artist="Ben E. King", album="Don't Play That Song!", genre="Soul")
    song45 = Song(name="Sittin' On The Dock Of The Bay", artist="Otis Redding", album="The Dock of the Bay", genre="Soul")
    song46 = Song(name="My Girl", artist="The Temptations", album="The Temptations Sing Smokey", genre="Soul")
    song47 = Song(name="Lean on Me", artist="Bill Withers", album="Still Bill", genre="Soul")
    song48 = Song(name="I Heard It Through The Grapevine", artist="Marvin Gaye", album="In the Groove", genre="Soul")
    song49 = Song(name="Soul Man", artist="Sam & Dave", album="Soul Men", genre="Soul")
    song50 = Song(name="Superstition", artist="Stevie Wonder", album="Talking Book", genre="Soul")
    song51 = Song(name="What's Going On", artist="Marvin Gaye", album="What's Going On", genre="Soul")
    song52 = Song(name="Papa Was A Rollin' Stone", artist="The Temptations", album="All Directions", genre="Soul")
    song53 = Song(name="A Change Is Gonna Come", artist="Sam Cooke", album="Ain't That Good News", genre="Soul")
    song54 = Song(name="I Want You Back", artist="Jackson 5", album="Diana Ross Presents The Jackson 5", genre="Soul")
    song55 = Song(name="I'll Take You There", artist="The Staple Singers", album="Bealtitude: Respect Yourself", genre="Soul")
    song56 = Song(name="Midnight Train to Georgia", artist="Gladys Knight & The Pips", album="Imagination", genre="Soul")
    song57 = Song(name="Kiss and Say Goodbye", artist="The Manhattans", album="The Manhattans", genre="Soul")
    song58 = Song(name="Me and Mrs. Jones", artist="Billy Paul", album="360 Degrees of Billy Paul", genre="Soul")
    song59 = Song(name="If You Don't Know Me by Now", artist="Harold Melvin & The Blue Notes", album="Harold Melvin & The Blue Notes", genre="Soul")
    song60 = Song(name="Lovely Day", artist="Bill Withers", album="Menagerie", genre="Soul")
    song61 = Song(name="Super Freak", artist="Rick James", album="Street Songs", genre="Funk")
    song62 = Song(name="Play That Funky Music", artist="Wild Cherry", album="Wild Cherry", genre="Funk")
    song63 = Song(name="Give Up the Funk (Tear the Roof off the Sucker)", artist="Parliament", album="Mothership Connection", genre="Funk")
    song64 = Song(name="Brick House", artist="The Commodores", album="Commodores", genre="Funk")
    song65 = Song(name="Funky Town", artist="Lipps Inc.", album="Mouth to Mouth", genre="Funk")
    song66 = Song(name="Jungle Boogie", artist="Kool & The Gang", album="Wild and Peaceful", genre="Funk")
    song67 = Song(name="Get Up (I Feel Like Being a) Sex Machine", artist="James Brown", album="Sex Machine", genre="Funk")
    song68 = Song(name="Flash Light", artist="Parliament", album="Funkentelechy Vs. the Placebo Syndrome", genre="Funk")
    song69 = Song(name="Pick Up the Pieces", artist="Average White Band", album="AWB", genre="Funk")
    song70 = Song(name="Dance to the Music", artist="Sly & The Family Stone", album="Dance to the Music", genre="Funk")
    song71 = Song(name="I Want to Take You Higher", artist="Sly & The Family Stone", album="Stand!", genre="Funk")
    song72 = Song(name="Shining Star", artist="Earth, Wind & Fire", album="That's the Way of the World", genre="Funk")
    song73 = Song(name="Thank You (Falettinme Be Mice Elf Agin)", artist="Sly & The Family Stone", album="Greatest Hits", genre="Funk")
    song74 = Song(name="Get Down on It", artist="Kool & The Gang", album="Something Special", genre="Funk")
    song75 = Song(name="Love Rollercoaster", artist="Ohio Players", album="Honey", genre="Funk")
    song76 = Song(name="Fantastic Voyage", artist="Lakeside", album="Fantastic Voyage", genre="Funk")
    song77 = Song(name="Jungle Love", artist="The Time", album="Ice Cream Castle", genre="Funk")
    song78 = Song(name="Fire", artist="Ohio Players", album="Fire", genre="Funk")
    song79 = Song(name="It's Your Thing", artist="The Isley Brothers", album="It's Our Thing", genre="Funk")
    song80 = Song(name="Let's Groove", artist="Earth, Wind & Fire", album="Raise!", genre="Funk")
    song81 = Song(name="One More Time", artist="Daft Punk", album="Discovery", genre="House")
    song82 = Song(name="Show Me Love", artist="Robin S", album="Show Me Love", genre="House")
    song83 = Song(name="Faded", artist="Alan Walker", album="Different World", genre="House")
    song84 = Song(name="Promises", artist="Calvin Harris, Sam Smith", album="Promises", genre="House")
    song85 = Song(name="Children", artist="Robert Miles", album="Dreamland", genre="House")
    song86 = Song(name="Finally", artist="CeCe Peniston", album="Finally", genre="House")
    song87 = Song(name="Don't You Worry Child", artist="Swedish House Mafia", album="Until Now", genre="House")
    song88 = Song(name="Pjanoo", artist="Eric Prydz", album="Pjanoo", genre="House")
    song89 = Song(name="This Is What It Feels Like", artist="Armin van Buuren ft. Trevor Guthrie", album="Intense", genre="House")
    song90 = Song(name="Need U (100%)", artist="Duke Dumont ft. AME", album="Blasé Boys Club Part 1", genre="House")
    song91 = Song(name="I Remember", artist="deadmau5 & Kaskade", album="Random Album Title", genre="House")
    song92 = Song(name="Cola", artist="CamelPhat & Elderbrook", album="Cola", genre="House")
    song93 = Song(name="How Deep Is Your Love", artist="Calvin Harris & Disciples", album="Motion", genre="House")
    song94 = Song(name="Don't Be So Shy (Filatov & Karas Remix)", artist="Imany", album="The Wrong Kind of War", genre="House")
    song95 = Song(name="Changes", artist="Faul & Wad Ad vs. Pnau", album="Changes", genre="House")
    song96 = Song(name="Gypsy Woman (She's Homeless)", artist="Crystal Waters", album="Surprise", genre="House")
    song97 = Song(name="Insomnia", artist="Faithless", album="Reverence", genre="House")
    song98 = Song(name="Ghosts 'n' Stuff", artist="deadmau5 ft. Rob Swire", album="For Lack of a Better Name", genre="House")
    song99 = Song(name="Latch", artist="Disclosure ft. Sam Smith", album="Settle", genre="House")
    song100 = Song(name="Rhythm Is a Dancer", artist="Snap!", album="The Madman's Return", genre="House")
    song101 = Song(name="Oye Como Va", artist="Santana", album="Abraxas", genre="Latin")
    song102 = Song(name="Quimbara", artist="Celia Cruz", album="Celia & Johnny", genre="Latin")
    song103 = Song(name="Bamboléo", artist="Gipsy Kings", album="Gipsy Kings", genre="Latin")
    song104 = Song(name="La Vida Es Un Carnaval", artist="Celia Cruz", album="Mi Vida Es Cantar", genre="Latin")
    song105 = Song(name="Guantanamera", artist="Celia Cruz", album="The Best of Celia Cruz", genre="Latin")
    song106 = Song(name="La Bamba", artist="Los Lobos", album="La Bamba (Original Motion Picture Soundtrack)", genre="Latin")
    song107 = Song(name="Conga", artist="Gloria Estefan & Miami Sound Machine", album="Primitive Love", genre="Latin")
    song108 = Song(name="Bésame Mucho", artist="Consuelo Velázquez", album="N/A", genre="Latin")
    song109 = Song(name="Volare (Nel Blu Dipinto Di Blu)", artist="Dean Martin", album="This Time I'm Swingin'!", genre="Latin")
    song110 = Song(name="Guajira", artist="Santana", album="Santana", genre="Latin")
    song111 = Song(name="Cucurrucucú Paloma", artist="Caetano Veloso", album="N/A", genre="Latin")
    song112 = Song(name="Lambada", artist="Kaoma", album="Worldbeat", genre="Latin")
    song113 = Song(name="La Murga", artist="Willie Colón", album="La Gran Fuga", genre="Latin")
    song114 = Song(name="Soy Guajiro", artist="Ibrahim Ferrer", album="Buenos Hermanos", genre="Latin")
    song115 = Song(name="Frenesí", artist="Linda Ronstadt", album="Frenesí", genre="Latin")
    song116 = Song(name="Aquellos Ojos Verdes", artist="Natalia Lafourcade", album="Musas (Un Homenaje al Folclore Latinoamericano en Manos de Los Macorinos)", genre="Latin")
    song117 = Song(name="La Plaga", artist="Los Terricolas", album="N/A", genre="Latin")
    song118 = Song(name="La Cumbia de los Trapos", artist="Rodolfo Aicardi", album="N/A", genre="Latin")
    song119 = Song(name="Amor Eterno", artist="Rocío Dúrcal", album="Canta a Juan Gabriel Volumen 6", genre="Latin")
    song120 = Song(name="La Rebelión", artist="Joe Arroyo y La Verdad", album="Fuego", genre="Latin")
    song121 = Song(name="Let's Just Praise The Lord", artist="Andraé Crouch", album="Don't Give Up", genre="Gospel Disco")
    song122 = Song(name="He's A Friend", artist="Eddie Kendricks", album="Slick", genre="Gospel Disco")
    song123 = Song(name="Shining Star", artist="The Manhattans", album="Manhattans", genre="Gospel Disco")
    song124 = Song(name="Reach Out", artist="George McCrae", album="Rock Your Baby", genre="Gospel Disco")
    song125 = Song(name="Hallelujah, Glory Hallelujah", artist="Karen Young", album="Hot Shot", genre="Gospel Disco")
    song126 = Song(name="Free Man", artist="South Shore Commission", album="South Shore Commission", genre="Gospel Disco")
    song127 = Song(name="Heaven Bound", artist="Linda Clifford", album="If My Friends Could See Me Now", genre="Gospel Disco")
    song128 = Song(name="Keep On Dancin'", artist="Gary's Gang", album="Keep On Dancin'", genre="Gospel Disco")
    song129 = Song(name="Go With The Flow", artist="Weeks & Co.", album="Weeks & Co.", genre="Gospel Disco")
    song130 = Song(name="Jesus Knows", artist="Bimbo Jet", album="El Bimbo", genre="Gospel Disco")
    song131 = Song(name="Don't Stop 'Til You Get Enough", artist="Michael Jackson", album="Off the Wall", genre="Boogie")
    song132 = Song(name="Rock with You", artist="Michael Jackson", album="Off the Wall", genre="Boogie")
    song133 = Song(name="Rhythm of the Night", artist="DeBarge", album="Rhythm of the Night", genre="Boogie")
    song134 = Song(name="I Wanna Dance with Somebody (Who Loves Me)", artist="Whitney Houston", album="Whitney", genre="Boogie")
    song135 = Song(name="Let's Groove", artist="Earth, Wind & Fire", album="Raise!", genre="Boogie")
    song136 = Song(name="Let the Music Play", artist="Shannon", album="Let the Music Play", genre="Boogie")
    song137 = Song(name="Automatic", artist="The Pointer Sisters", album="Break Out", genre="Boogie")
    song138 = Song(name="A Night to Remember", artist="Shalamar", album="Friends", genre="Boogie")
    song139 = Song(name="Running with the Night", artist="Lionel Richie", album="Can't Slow Down", genre="Boogie")
    song140 = Song(name="All Night Long (All Night)", artist="Lionel Richie", album="Can't Slow Down", genre="Boogie")
    song141 = Song(name="You're the One for Me", artist="D. Train", album="You're the One for Me", genre="Boogie")
    song142 = Song(name="Encore", artist="Cheryl Lynn", album="Instant Love", genre="Boogie")
    song143 = Song(name="Just an Illusion", artist="Imagination", album="In the Heat of the Night", genre="Boogie")
    song144 = Song(name="Last Night a D.J. Saved My Life", artist="Indeep", album="Last Night a D.J. Saved My Life", genre="Boogie")
    song145 = Song(name="I Can't Go for That (No Can Do)", artist="Hall & Oates", album="Private Eyes", genre="Boogie")
    song146 = Song(name="Juicy Fruit", artist="Mtume", album="Juicy Fruit", genre="Boogie")
    song147 = Song(name="Running Back to You", artist="Vanessa Williams", album="The Right Stuff", genre="Boogie")
    song148 = Song(name="You Give Good Love", artist="Whitney Houston", album="Whitney Houston", genre="Boogie")
    song149 = Song(name="Automatic", artist="The Whispers", album="The Whispers", genre="Boogie")
    song150 = Song(name="She's Strange", artist="Cameo", album="She's Strange", genre="Boogie")
    song151 = Song(name="I Can Make You Feel Good", artist="Shalamar", album="Big Fun", genre="Boogie")
    song152 = Song(name="Forget Me Nots", artist="Patrice Rushen", album="Straight from the Heart", genre="Boogie")
    song153 = Song(name="And the Beat Goes On", artist="The Whispers", album="The Whispers", genre="Boogie")
    song154 = Song(name="Off the Wall", artist="Michael Jackson", album="Off the Wall", genre="Boogie")
    song155 = Song(name="Nasty", artist="Janet Jackson", album="Control", genre="Boogie")
    song156 = Song(name="Hangin' On a String (Contemplating)", artist="Loose Ends", album="So Where Are You?", genre="Boogie")
    song157 = Song(name="Behind the Groove", artist="Teena Marie", album="Lady T", genre="Boogie")
    song158 = Song(name="Midnight Lady", artist="Marvin Gaye", album="Midnight Love", genre="Boogie")
    song159 = Song(name="You and Me Tonight", artist="Aurra", album="A Little Love", genre="Boogie")
    song160 = Song(name="Ain't Nobody", artist="Chaka Khan", album="I Feel for You", genre="Boogie")
    song161 = Song(name="Don't You Want Me", artist="The Human League", album="Dare", genre="Boogie")
    song162 = Song(name="I'm Coming Out", artist="Diana Ross", album="diana", genre="Boogie")
    song163 = Song(name="Change of Heart", artist="Change", album="Change of Heart", genre="Boogie")
    song164 = Song(name="Candy", artist="Cameo", album="Word Up!", genre="Boogie")
    song165 = Song(name="A Lover's Holiday", artist="Change", album="The Glow of Love", genre="Boogie")
    song166 = Song(name="Jump to It", artist="Aretha Franklin", album="Jump to It", genre="Boogie")
    song167 = Song(name="Automatic", artist="The Pointer Sisters", album="Break Out", genre="Boogie")
    song168 = Song(name="Feel So Real", artist="Steve Arrington", album="Dancin' in the Key of Life", genre="Boogie")
    song169 = Song(name="Bounce, Rock, Skate, Roll", artist="Vaughan Mason & Crew", album="Bounce, Rock, Skate, Roll", genre="Boogie")
    song170 = Song(name="Love Come Down", artist="Evelyn 'Champagne' King", album="Get Loose", genre="Boogie")
    song171 = Song(name="Back to Life (However Do You Want Me)", artist="Soul II Soul ft. Caron Wheeler", album="Club Classics Vol. One", genre="Street Soul")
    song172 = Song(name="Keep On Movin'", artist="Soul II Soul ft. Caron Wheeler", album="Club Classics Vol. One", genre="Street Soul")
    song173 = Song(name="Fairplay", artist="Soul II Soul ft. Rose Windross", album="Club Classics Vol. One", genre="Street Soul")
    song174 = Song(name="Dreams", artist="Gabrielle", album="Find Your Way", genre="Street Soul")
    song175 = Song(name="Don't Walk Away", artist="Jade", album="Jade to the Max", genre="Street Soul")
    song176 = Song(name="Tender Love", artist="Kenny Thomas", album="Voices", genre="Street Soul")
    song177 = Song(name="Kissing You", artist="Keith Washington", album="Make Time for Love", genre="Street Soul")
    song178 = Song(name="Never Gonna Let You Go", artist="Tina Moore", album="Time Will Tell", genre="Street Soul")
    song179 = Song(name="Sometimes", artist="Brand New Heavies", album="Brand New Heavies", genre="Street Soul")
    song180 = Song(name="No Ordinary Love", artist="Sade", album="Love Deluxe", genre="Street Soul")
    song181 = Song(name="Don't Be a Fool", artist="Loose Ends", album="Look How Long", genre="Street Soul")
    song182 = Song(name="Don't Look Any Further", artist="Dennis Edwards ft. Siedah Garrett", album="Don't Look Any Further", genre="Street Soul")
    song183 = Song(name="Criticize", artist="Alexander O'Neal", album="Hearsay", genre="Street Soul")
    song184 = Song(name="Close to You", artist="Maxi Priest", album="Bonafide", genre="Street Soul")
    song185 = Song(name="Fair-Weather Friend", artist="Johnny Gill", album="Johnny Gill", genre="Street Soul")
    song186 = Song(name="If You Love Me", artist="Brownstone", album="From the Bottom Up", genre="Street Soul")
    song187 = Song(name="All Around the World", artist="Lisa Stansfield", album="Affection", genre="Street Soul")
    song188 = Song(name="Sensitivity", artist="Ralph Tresvant", album="Ralph Tresvant", genre="Street Soul")
    song189 = Song(name="I'll Be Good to You", artist="Brothers in Rhythm", album="I'll Be Good to You", genre="Street Soul")
    song190 = Song(name="Something's Going On", artist="Terry Callier", album="Timepeace", genre="Street Soul")
    song191 = Song(name="Finally", artist="CeCe Peniston", album="Finally", genre="Soulful House")
    song192 = Song(name="Gypsy Woman (She's Homeless)", artist="Crystal Waters", album="Surprise", genre="Soulful House")
    song193 = Song(name="You Don't Know Me", artist="Armand Van Helden ft. Duane Harden", album="2 Future 4 U", genre="Soulful House")
    song194 = Song(name="Show Me Love", artist="Robin S", album="Show Me Love", genre="Soulful House")
    song195 = Song(name="The Bomb! (These Sounds Fall into My Mind)", artist="The Bucketheads", album="All in the Mind", genre="Soulful House")
    song196 = Song(name="Beautiful People", artist="Barbara Tucker", album="Beautiful People", genre="Soulful House")
    song197 = Song(name="Found Love", artist="Double Dee ft. Dany", album="Found Love", genre="Soulful House")
    song198 = Song(name="Push the Feeling On", artist="Nightcrawlers", album="Let's Push It", genre="Soulful House")
    song199 = Song(name="Finally Found", artist="Honeyz", album="Wonder No. 8", genre="Soulful House")
    song200 = Song(name="Big Love", artist="Pete Heller", album="Big Love", genre="Soulful House")
    song201 = Song(name="Someday", artist="Mariah Carey", album="Mariah Carey", genre="Soulful House")
    song202 = Song(name="Your Loving Arms", artist="Billie Ray Martin", album="Deadline for My Memories", genre="Soulful House")
    song203 = Song(name="Deep Inside", artist="Hardrive", album="Hardrive 2000", genre="Soulful House")
    song204 = Song(name="I Want You", artist="Gary Low", album="I Want You", genre="Soulful House")
    song205 = Song(name="Free", artist="Ultra Naté", album="Situation: Critical", genre="Soulful House")
    song206 = Song(name="Singing in My Mind", artist="Sugarland Gang", album="Singing in My Mind", genre="Soulful House")
    song207 = Song(name="What You Need", artist="Soft House Company", album="What You Need", genre="Soulful House")
    song208 = Song(name="Lift Every Voice (Take Me Away)", artist="Mass Order", album="Maybe One Day", genre="Soulful House")
    song209 = Song(name="I Can't Get No Sleep", artist="MAW ft. India", album="The Album", genre="Soulful House")
    song210 = Song(name="Moving On Up", artist="M People", album="Elegant Slumming", genre="Soulful House")
    song211 = Song(name="Plastic Love", artist="Mariya Takeuchi", album="VARIETY", genre="City Pop")
    song212 = Song(name="Stay With Me", artist="Miki Matsubara", album="Pocket Park", genre="City Pop")
    song213 = Song(name="Big Wave", artist="Anri", album="Bi・Ki・Ni", genre="City Pop")
    song214 = Song(name="Ride on Time", artist="Tatsuro Yamashita", album="Ride on Time", genre="City Pop")
    song215 = Song(name="Telephone Number", artist="Junko Ohashi", album="Magical", genre="City Pop")
    song216 = Song(name="Summer Connection", artist="Meiko Nakahara", album="Fantastic", genre="City Pop")
    song217 = Song(name="Sweetest Music", artist="Taeko Ohnuki", album="Aventure", genre="City Pop")
    song218 = Song(name="Sepia", artist="Yumi Matsutoya", album="DA・DI・DA", genre="City Pop")
    song219 = Song(name="Windy Summer", artist="Minako Yoshida", album="Twilight Zone", genre="City Pop")
    song220 = Song(name="Piano in Summer", artist="Yurie Kokubu", album="La Dolce Vita", genre="City Pop")
    song221 = Song(name="Midnight Pretenders", artist="Tomoko Aran", album="Fuyu-Kukan", genre="City Pop")
    song222 = Song(name="Love Talkin' (Honey It's You)", artist="Tatsuro Yamashita", album="For You", genre="City Pop")
    song223 = Song(name="Cinderella", artist="Anri", album="Heaven Beach", genre="City Pop")
    song224 = Song(name="Silhouette Call", artist="Hiroshi Sato", album="Awakening", genre="City Pop")
    song225 = Song(name="4:00 AM", artist="Taeko Ohnuki", album="Sunshower", genre="City Pop")
    song226 = Song(name="City", artist="Jun Togawa", album="20th Jun Togawa", genre="City Pop")
    song227 = Song(name="Driving All Night", artist="Cindy", album="Daylight", genre="City Pop")
    song228 = Song(name="Good-Bye", artist="Anri", album="Timely!!", genre="City Pop")
    song229 = Song(name="Anklet", artist="Yumi Matsutoya", album="Reincarnation", genre="City Pop")
    song230 = Song(name="Bayside Candle Lights", artist="Taeko Ohnuki", album="Cliche", genre="City Pop")








    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(user4)

    db.session.add(song1)
    db.session.add(song2)
    db.session.add(song3)
    db.session.add(song4)
    db.session.add(song5)
    db.session.add(song6)

    db.session.commit()