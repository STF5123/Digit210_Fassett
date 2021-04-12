import spacy


nlp = spacy.load('en_core_web_sm')

grimm = open('grimm_fassett.txt', 'r')
words = grimm.read()
wordstrings = str(words)
print(wordstrings)

grimmwords = nlp(wordstrings)
for token in grimmwords:
    print(token.text,"---->", token.pos,":::::",token.lemma_)

   THE TWELVE HUNTSMEN
    There was once a kingâ€™s son who had a bride whom he loved very much. And when he was sitting
      beside her and very happy, news came that his father lay sick unto death, and desired to see
      him once again before his end. Then he Said to his beloved: â€˜I must now go and leave you, I
      give you a ring as a remembrance of me. When I am king, I will return and fetch you.â€™ So he
      rode away, and when he reached his father, the latter was dangerously ill, and near his death.
      He Said to him: â€˜Dear son, I wished to see you once again before my end, promise me to marry
      as I wish,â€™ and he named a certain kingâ€™s daughter who was to be his wife. The son was in such
      trouble that he did not think what he was doing, and Said: â€˜Yes, dear father, your will shall
      be done,â€™ and thereupon the king shut his eyes, and died.
    When therefore the son had been proclaimed king, and the time of mourning was over, he was
      forced to keep the promise which he had given his father, and caused the kingâ€™s daughter to be
      asked in marriage, and she was promised to him. His first betrothed heard of this, and fretted
      so much about his faithfulness that she nearly died. Then her father Said to her: â€˜Dearest
      child, why are you so sad? You shall have whatsoever you will.â€™ She thought for a moment and
      Said: â€˜Dear father, I wish for  eleven girls exactly like myself in face, figure, and size.â€™
      The father Said: â€˜If it be possible, your desire shall be fulfilled,â€™ and he caused a search
      to be made in his whole kingdom, until  eleven young maidens were found who exactly resembled
      his daughter in face, figure, and size.
    When they came to the kingâ€™s daughter, she had twelve suits of huntsmenâ€™s clothes made, all
      alike, and the  eleven maidens had to put on the huntsmenâ€™s clothes, and she herself put on the
      twelfth suit. Thereupon she took her leave of her father, and rode away with them, and rode to
      the court of her former betrothed, whom she loved so dearly. Then she asked if he required any
      huntsmen, and if he would take all of them into his service. The king looked at her and did
      not know her, but as they were such handsome fellows, he Said: â€˜Yes,â€™ and that he would
      willingly take them, and now they were the kingâ€™s twelve huntsmen.
    The king, however, had a lion which was a wondrous animal, for he knew all concealed and
      secret things. It came to pass that one evening he Said to the king: â€˜You think you have
      twelve huntsmen?â€™ â€˜Yes,â€™ Said the king, â€˜they are twelve huntsmen.â€™ The lion continued: â€˜You
      are mistaken, they are twelve girls.â€™ The king Said: â€˜That cannot be true! How will you prove
      that to me?â€™ â€˜Oh, just let some peas be strewn in the ante-chamber,â€™ answered the lion, â€˜and
      then you will soon see. Men have a firm step, and when they walk over peas none of them stir,
      but girls trip and skip, and drag their feet, and the peas roll about.â€™ The king was well
      pleased with the counsel, and caused the peas to be strewn.
    There was, however, a servant of the kingâ€™s who favoured the huntsmen, and when he heard that
      they were going to be put to this test he went to them and repeated everything, and Said: â€˜The
      lion wants to make the king believe that you are girls.â€™ Then the kingâ€™s daughter thanked him,
      and Said to her maidens: â€˜Show some strength, and step firmly on the peas.â€™ So next morning
      when the king had the twelve huntsmen called before him, and they came into the ante-chamber
      where the peas were lying, they stepped so firmly on them, and had such a strong, sure walk,
      that not one of the peas either rolled or stirred. Then they went away again, and the king
      Said to the lion: â€˜You have lied to me, they walk just like men.â€™ The lion Said: â€˜They have
      been informed that they were going to be put to the test, and have assumed some strength. Just
      let twelve spinning-wheels be brought into the ante-chamber, and they will go to them and be
      pleased with them, and that is what no man would do.â€™ The king liked the advice, and had the
      spinning-wheels placed in the ante-chamber.
    But the servant, who was well disposed to the huntsmen, went to them, and disclosed the
      project. So when they were alone the kingâ€™s daughter Said to her  eleven girls: â€˜Show some
      constraint, and do not look round at the spinning-wheels.â€™ And next morning when the king had
      his twelve huntsmen summoned, they went through the ante-chamber, and never once looked at the
      spinning-wheels. Then the king again Said to the lion: â€˜You have deceived me, they are men,
      for they have not looked at the spinning-wheels.â€™ The lion replied: â€˜They have restrained
      themselves.â€™ The king, however, would no longer believe the lion.
    The twelve huntsmen always followed the king to the chase, and his liking for them
      continually increased. Now it came to pass that once when they were out hunting, news came
      that the kingâ€™s bride was approaching. When the true bride heard that, it hurt her so much
      that her heart was almost broken, and she fell fainting to the ground. The king thought
      something had happened to his dear huntsman, ran up to him, wanted to help him, and drew his
      glove off. Then he saw the ring which he had given to his first bride, and when he looked in
      her face he recognized her. Then his heart was so touched that he kissed her, and when she
      opened her eyes he Said: â€˜You are mine, and I am yours, and no one in the world can alter
      that.â€™ He sent a messenger to the other bride, and entreated her to return to her own kingdom,
      for he had a wife already, and someone who had just found an old key did not require a new
      one. Thereupon the wedding was celebrated, and the lion was again taken into favour, because,
      after all, he had told the truth.
  

     ----> 103 ::::: 
    
THE ----> 90 ::::: the
TWELVE ----> 96 ::::: TWELVE
HUNTSMEN ----> 96 ::::: HUNTSMEN

     ----> 103 ::::: 
    
There ----> 95 ::::: there
was ----> 87 ::::: be
once ----> 86 ::::: once
a ----> 90 ::::: a
kingâ€ ----> 92 ::::: kingâ€
™ ----> 96 ::::: ™
s ----> 94 ::::: s
son ----> 92 ::::: son
who ----> 95 ::::: who
had ----> 100 ::::: have
a ----> 90 ::::: a
bride ----> 92 ::::: bride
whom ----> 95 ::::: whom
he ----> 95 ::::: he
loved ----> 100 ::::: love
very ----> 86 ::::: very
much ----> 86 ::::: much
. ----> 97 ::::: .
And ----> 89 ::::: and
when ----> 86 ::::: when
he ----> 95 ::::: he
was ----> 87 ::::: be
sitting ----> 100 ::::: sit

       ----> 103 ::::: 
      
beside ----> 85 ::::: beside
her ----> 95 ::::: she
and ----> 89 ::::: and
very ----> 86 ::::: very
happy ----> 84 ::::: happy
, ----> 97 ::::: ,
news ----> 92 ::::: news
came ----> 100 ::::: come
that ----> 98 ::::: that
his ----> 95 ::::: his
father ----> 92 ::::: father
lay ----> 100 ::::: lie
sick ----> 84 ::::: sick
unto ----> 85 ::::: unto
death ----> 92 ::::: death
, ----> 97 ::::: ,
and ----> 89 ::::: and
desired ----> 100 ::::: desire
to ----> 94 ::::: to
see ----> 100 ::::: see

       ----> 103 ::::: 
      
him ----> 95 ::::: he
once ----> 86 ::::: once
again ----> 86 ::::: again
before ----> 85 ::::: before
his ----> 95 ::::: his
end ----> 92 ::::: end
. ----> 97 ::::: .
Then ----> 86 ::::: then
he ----> 95 ::::: he
Said ----> 100 ::::: say
to ----> 85 ::::: to
his ----> 95 ::::: his
beloved ----> 84 ::::: beloved
: ----> 97 ::::: :
â€˜I ----> 92 ::::: â€˜i
must ----> 87 ::::: must
now ----> 86 ::::: now
go ----> 100 ::::: go
and ----> 89 ::::: and
leave ----> 100 ::::: leave
you ----> 95 ::::: you
, ----> 97 ::::: ,
I ----> 95 ::::: I

       ----> 103 ::::: 
      
give ----> 100 ::::: give
you ----> 95 ::::: you
a ----> 90 ::::: a
ring ----> 92 ::::: ring
as ----> 85 ::::: as
a ----> 90 ::::: a
remembrance ----> 92 ::::: remembrance
of ----> 85 ::::: of
me ----> 95 ::::: I
. ----> 97 ::::: .
When ----> 86 ::::: when
I ----> 95 ::::: I
am ----> 100 ::::: be
king ----> 92 ::::: king
, ----> 97 ::::: ,
I ----> 95 ::::: I
will ----> 87 ::::: will
return ----> 100 ::::: return
and ----> 89 ::::: and
fetch ----> 100 ::::: fetch
you.â€ ----> 92 ::::: you.â€
™ ----> 100 ::::: ™
So ----> 86 ::::: so
he ----> 95 ::::: he

       ----> 103 ::::: 
      
rode ----> 100 ::::: ride
away ----> 86 ::::: away
, ----> 97 ::::: ,
and ----> 89 ::::: and
when ----> 86 ::::: when
he ----> 95 ::::: he
reached ----> 100 ::::: reach
his ----> 95 ::::: his
father ----> 92 ::::: father
, ----> 97 ::::: ,
the ----> 90 ::::: the
latter ----> 84 ::::: latter
was ----> 100 ::::: be
dangerously ----> 86 ::::: dangerously
ill ----> 84 ::::: ill
, ----> 97 ::::: ,
and ----> 89 ::::: and
near ----> 98 ::::: near
his ----> 95 ::::: his
death ----> 92 ::::: death
. ----> 97 ::::: .

       ----> 103 ::::: 
      
He ----> 95 ::::: he
Said ----> 100 ::::: say
to ----> 85 ::::: to
him ----> 95 ::::: he
: ----> 97 ::::: :
â€˜Dear ----> 100 ::::: â€˜dear
son ----> 92 ::::: son
, ----> 97 ::::: ,
I ----> 95 ::::: I
wished ----> 100 ::::: wish
to ----> 94 ::::: to
see ----> 100 ::::: see
you ----> 95 ::::: you
once ----> 86 ::::: once
again ----> 86 ::::: again
before ----> 85 ::::: before
my ----> 95 ::::: my
end ----> 92 ::::: end
, ----> 97 ::::: ,
promise ----> 100 ::::: promise
me ----> 95 ::::: I
to ----> 94 ::::: to
marry ----> 100 ::::: marry

       ----> 103 ::::: 
      
as ----> 85 ::::: as
I ----> 95 ::::: I
wish ----> 100 ::::: wish
, ----> 97 ::::: ,
â€ ----> 93 ::::: â€
™ ----> 92 ::::: ™
and ----> 89 ::::: and
he ----> 95 ::::: he
named ----> 100 ::::: name
a ----> 90 ::::: a
certain ----> 84 ::::: certain
kingâ€ ----> 96 ::::: kingâ€
™ ----> 96 ::::: ™
s ----> 94 ::::: s
daughter ----> 92 ::::: daughter
who ----> 95 ::::: who
was ----> 100 ::::: be
to ----> 94 ::::: to
be ----> 100 ::::: be
his ----> 95 ::::: his
wife ----> 92 ::::: wife
. ----> 97 ::::: .
The ----> 90 ::::: the
son ----> 92 ::::: son
was ----> 87 ::::: be
in ----> 85 ::::: in
such ----> 84 ::::: such

       ----> 103 ::::: 
      
trouble ----> 92 ::::: trouble
that ----> 90 ::::: that
he ----> 95 ::::: he
did ----> 87 ::::: do
not ----> 94 ::::: not
think ----> 100 ::::: think
what ----> 95 ::::: what
he ----> 95 ::::: he
was ----> 87 ::::: be
doing ----> 100 ::::: do
, ----> 97 ::::: ,
and ----> 89 ::::: and
Said ----> 100 ::::: say
: ----> 97 ::::: :
â€˜Yes ----> 91 ::::: â€˜yes
, ----> 97 ::::: ,
dear ----> 84 ::::: dear
father ----> 92 ::::: father
, ----> 97 ::::: ,
your ----> 95 ::::: your
will ----> 92 ::::: will
shall ----> 87 ::::: shall

       ----> 103 ::::: 
      
be ----> 87 ::::: be
done ----> 100 ::::: do
, ----> 97 ::::: ,
â€ ----> 93 ::::: â€
™ ----> 92 ::::: ™
and ----> 89 ::::: and
thereupon ----> 86 ::::: thereupon
the ----> 90 ::::: the
king ----> 92 ::::: king
shut ----> 100 ::::: shut
his ----> 95 ::::: his
eyes ----> 92 ::::: eye
, ----> 97 ::::: ,
and ----> 89 ::::: and
died ----> 100 ::::: die
. ----> 97 ::::: .

     ----> 103 ::::: 
    
When ----> 86 ::::: when
therefore ----> 86 ::::: therefore
the ----> 90 ::::: the
son ----> 92 ::::: son
had ----> 87 ::::: have
been ----> 87 ::::: be
proclaimed ----> 100 ::::: proclaim
king ----> 92 ::::: king
, ----> 97 ::::: ,
and ----> 89 ::::: and
the ----> 90 ::::: the
time ----> 92 ::::: time
of ----> 85 ::::: of
mourning ----> 92 ::::: mourning
was ----> 100 ::::: be
over ----> 86 ::::: over
, ----> 97 ::::: ,
he ----> 95 ::::: he
was ----> 87 ::::: be

       ----> 103 ::::: 
      
forced ----> 100 ::::: force
to ----> 94 ::::: to
keep ----> 100 ::::: keep
the ----> 90 ::::: the
promise ----> 92 ::::: promise
which ----> 90 ::::: which
he ----> 95 ::::: he
had ----> 87 ::::: have
given ----> 100 ::::: give
his ----> 95 ::::: his
father ----> 92 ::::: father
, ----> 97 ::::: ,
and ----> 89 ::::: and
caused ----> 100 ::::: cause
the ----> 90 ::::: the
kingâ€ ----> 96 ::::: kingâ€
™ ----> 96 ::::: ™
s ----> 94 ::::: s
daughter ----> 92 ::::: daughter
to ----> 94 ::::: to
be ----> 100 ::::: be

       ----> 103 ::::: 
      
asked ----> 100 ::::: ask
in ----> 85 ::::: in
marriage ----> 92 ::::: marriage
, ----> 97 ::::: ,
and ----> 89 ::::: and
she ----> 95 ::::: she
was ----> 87 ::::: be
promised ----> 100 ::::: promise
to ----> 85 ::::: to
him ----> 95 ::::: he
. ----> 97 ::::: .
His ----> 95 ::::: his
first ----> 84 ::::: first
betrothed ----> 84 ::::: betrothed
heard ----> 92 ::::: heard
of ----> 85 ::::: of
this ----> 90 ::::: this
, ----> 97 ::::: ,
and ----> 89 ::::: and
fretted ----> 100 ::::: fret

       ----> 103 ::::: 
      
so ----> 86 ::::: so
much ----> 86 ::::: much
about ----> 85 ::::: about
his ----> 95 ::::: his
faithfulness ----> 92 ::::: faithfulness
that ----> 98 ::::: that
she ----> 95 ::::: she
nearly ----> 86 ::::: nearly
died ----> 100 ::::: die
. ----> 97 ::::: .
Then ----> 86 ::::: then
her ----> 95 ::::: her
father ----> 92 ::::: father
Said ----> 100 ::::: say
to ----> 85 ::::: to
her ----> 95 ::::: she
: ----> 97 ::::: :
â€˜Dearest ----> 101 ::::: â€˜dearest

       ----> 103 ::::: 
      
child ----> 92 ::::: child
, ----> 97 ::::: ,
why ----> 86 ::::: why
are ----> 87 ::::: be
you ----> 95 ::::: you
so ----> 86 ::::: so
sad ----> 84 ::::: sad
? ----> 97 ::::: ?
You ----> 95 ::::: you
shall ----> 87 ::::: shall
have ----> 100 ::::: have
whatsoever ----> 86 ::::: whatsoever
you ----> 95 ::::: you
will.â€ ----> 100 ::::: will.â€
™ ----> 96 ::::: ™
She ----> 95 ::::: she
thought ----> 100 ::::: think
for ----> 85 ::::: for
a ----> 90 ::::: a
moment ----> 92 ::::: moment
and ----> 89 ::::: and

       ----> 103 ::::: 
      
Said ----> 100 ::::: say
: ----> 97 ::::: :
â€˜Dear ----> 100 ::::: â€˜dear
father ----> 92 ::::: father
, ----> 97 ::::: ,
I ----> 95 ::::: I
wish ----> 100 ::::: wish
for ----> 85 ::::: for
  ----> 103 :::::  
eleven ----> 93 ::::: eleven
girls ----> 92 ::::: girl
exactly ----> 86 ::::: exactly
like ----> 85 ::::: like
myself ----> 95 ::::: myself
in ----> 85 ::::: in
face ----> 92 ::::: face
, ----> 97 ::::: ,
figure ----> 92 ::::: figure
, ----> 97 ::::: ,
and ----> 89 ::::: and
size.â€ ----> 92 ::::: size.â€
™ ----> 100 ::::: ™

       ----> 103 ::::: 
      
The ----> 90 ::::: the
father ----> 92 ::::: father
Said ----> 100 ::::: say
: ----> 97 ::::: :
â€˜If ----> 92 ::::: â€˜if
it ----> 95 ::::: it
be ----> 100 ::::: be
possible ----> 84 ::::: possible
, ----> 97 ::::: ,
your ----> 95 ::::: your
desire ----> 92 ::::: desire
shall ----> 87 ::::: shall
be ----> 87 ::::: be
fulfilled ----> 100 ::::: fulfil
, ----> 97 ::::: ,
â€ ----> 93 ::::: â€
™ ----> 92 ::::: ™
and ----> 89 ::::: and
he ----> 95 ::::: he
caused ----> 100 ::::: cause
a ----> 90 ::::: a
search ----> 92 ::::: search

       ----> 103 ::::: 
      
to ----> 94 ::::: to
be ----> 87 ::::: be
made ----> 100 ::::: make
in ----> 85 ::::: in
his ----> 95 ::::: his
whole ----> 84 ::::: whole
kingdom ----> 92 ::::: kingdom
, ----> 97 ::::: ,
until ----> 85 ::::: until
  ----> 103 :::::  
eleven ----> 93 ::::: eleven
young ----> 84 ::::: young
maidens ----> 92 ::::: maiden
were ----> 87 ::::: be
found ----> 100 ::::: find
who ----> 95 ::::: who
exactly ----> 86 ::::: exactly
resembled ----> 100 ::::: resemble

       ----> 103 ::::: 
      
his ----> 95 ::::: his
daughter ----> 92 ::::: daughter
in ----> 85 ::::: in
face ----> 92 ::::: face
, ----> 97 ::::: ,
figure ----> 92 ::::: figure
, ----> 97 ::::: ,
and ----> 89 ::::: and
size ----> 92 ::::: size
. ----> 97 ::::: .

     ----> 103 ::::: 
    
When ----> 86 ::::: when
they ----> 95 ::::: they
came ----> 100 ::::: come
to ----> 85 ::::: to
the ----> 90 ::::: the
kingâ€ ----> 96 ::::: kingâ€
™ ----> 96 ::::: ™
s ----> 94 ::::: s
daughter ----> 92 ::::: daughter
, ----> 97 ::::: ,
she ----> 95 ::::: she
had ----> 100 ::::: have
twelve ----> 93 ::::: twelve
suits ----> 92 ::::: suit
of ----> 85 ::::: of
huntsmenâ€ ----> 92 ::::: huntsmenâ€
™ ----> 92 ::::: ™
s ----> 94 ::::: s
clothes ----> 92 ::::: clothe
made ----> 100 ::::: make
, ----> 97 ::::: ,
all ----> 90 ::::: all

       ----> 103 ::::: 
      
alike ----> 86 ::::: alike
, ----> 97 ::::: ,
and ----> 89 ::::: and
the ----> 90 ::::: the
  ----> 103 :::::  
eleven ----> 93 ::::: eleven
maidens ----> 92 ::::: maiden
had ----> 100 ::::: have
to ----> 94 ::::: to
put ----> 100 ::::: put
on ----> 85 ::::: on
the ----> 90 ::::: the
huntsmenâ€ ----> 92 ::::: huntsmenâ€
™ ----> 92 ::::: ™
s ----> 94 ::::: s
clothes ----> 92 ::::: clothe
, ----> 97 ::::: ,
and ----> 89 ::::: and
she ----> 95 ::::: she
herself ----> 95 ::::: herself
put ----> 100 ::::: put
on ----> 85 ::::: on
the ----> 90 ::::: the

       ----> 103 ::::: 
      
twelfth ----> 84 ::::: twelfth
suit ----> 92 ::::: suit
. ----> 97 ::::: .
Thereupon ----> 86 ::::: thereupon
she ----> 95 ::::: she
took ----> 100 ::::: take
her ----> 95 ::::: her
leave ----> 92 ::::: leave
of ----> 85 ::::: of
her ----> 95 ::::: her
father ----> 92 ::::: father
, ----> 97 ::::: ,
and ----> 89 ::::: and
rode ----> 100 ::::: ride
away ----> 86 ::::: away
with ----> 85 ::::: with
them ----> 95 ::::: they
, ----> 97 ::::: ,
and ----> 89 ::::: and
rode ----> 100 ::::: ride
to ----> 85 ::::: to

       ----> 103 ::::: 
      
the ----> 90 ::::: the
court ----> 92 ::::: court
of ----> 85 ::::: of
her ----> 95 ::::: her
former ----> 84 ::::: former
betrothed ----> 92 ::::: betrothed
, ----> 97 ::::: ,
whom ----> 95 ::::: whom
she ----> 95 ::::: she
loved ----> 100 ::::: love
so ----> 86 ::::: so
dearly ----> 86 ::::: dearly
. ----> 97 ::::: .
Then ----> 86 ::::: then
she ----> 95 ::::: she
asked ----> 100 ::::: ask
if ----> 98 ::::: if
he ----> 95 ::::: he
required ----> 100 ::::: require
any ----> 90 ::::: any

       ----> 103 ::::: 
      
huntsmen ----> 92 ::::: huntsman
, ----> 97 ::::: ,
and ----> 89 ::::: and
if ----> 98 ::::: if
he ----> 95 ::::: he
would ----> 87 ::::: would
take ----> 100 ::::: take
all ----> 90 ::::: all
of ----> 85 ::::: of
them ----> 95 ::::: they
into ----> 85 ::::: into
his ----> 95 ::::: his
service ----> 92 ::::: service
. ----> 97 ::::: .
The ----> 90 ::::: the
king ----> 92 ::::: king
looked ----> 100 ::::: look
at ----> 85 ::::: at
her ----> 95 ::::: she
and ----> 89 ::::: and
did ----> 87 ::::: do

       ----> 103 ::::: 
      
not ----> 94 ::::: not
know ----> 100 ::::: know
her ----> 95 ::::: she
, ----> 97 ::::: ,
but ----> 89 ::::: but
as ----> 85 ::::: as
they ----> 95 ::::: they
were ----> 100 ::::: be
such ----> 84 ::::: such
handsome ----> 84 ::::: handsome
fellows ----> 92 ::::: fellow
, ----> 97 ::::: ,
he ----> 95 ::::: he
Said ----> 100 ::::: say
: ----> 97 ::::: :
â€˜Yes ----> 92 ::::: â€˜yes
, ----> 97 ::::: ,
â€ ----> 93 ::::: â€
™ ----> 92 ::::: ™
and ----> 89 ::::: and
that ----> 98 ::::: that
he ----> 95 ::::: he
would ----> 87 ::::: would

       ----> 103 ::::: 
      
willingly ----> 86 ::::: willingly
take ----> 100 ::::: take
them ----> 95 ::::: they
, ----> 97 ::::: ,
and ----> 89 ::::: and
now ----> 86 ::::: now
they ----> 95 ::::: they
were ----> 100 ::::: be
the ----> 90 ::::: the
kingâ€ ----> 92 ::::: kingâ€
™ ----> 96 ::::: ™
s ----> 94 ::::: s
twelve ----> 93 ::::: twelve
huntsmen ----> 92 ::::: huntsman
. ----> 97 ::::: .

     ----> 103 ::::: 
    
The ----> 90 ::::: the
king ----> 92 ::::: king
, ----> 97 ::::: ,
however ----> 86 ::::: however
, ----> 97 ::::: ,
had ----> 100 ::::: have
a ----> 90 ::::: a
lion ----> 92 ::::: lion
which ----> 90 ::::: which
was ----> 100 ::::: be
a ----> 90 ::::: a
wondrous ----> 84 ::::: wondrous
animal ----> 92 ::::: animal
, ----> 97 ::::: ,
for ----> 85 ::::: for
he ----> 95 ::::: he
knew ----> 100 ::::: know
all ----> 90 ::::: all
concealed ----> 100 ::::: conceal
and ----> 89 ::::: and

       ----> 103 ::::: 
      
secret ----> 84 ::::: secret
things ----> 92 ::::: thing
. ----> 97 ::::: .
It ----> 95 ::::: it
came ----> 100 ::::: come
to ----> 94 ::::: to
pass ----> 100 ::::: pass
that ----> 90 ::::: that
one ----> 93 ::::: one
evening ----> 92 ::::: evening
he ----> 95 ::::: he
Said ----> 100 ::::: say
to ----> 85 ::::: to
the ----> 90 ::::: the
king ----> 92 ::::: king
: ----> 97 ::::: :
â€˜You ----> 91 ::::: â€˜you
think ----> 100 ::::: think
you ----> 95 ::::: you
have ----> 100 ::::: have

       ----> 103 ::::: 
      
twelve ----> 84 ::::: twelve
huntsmen?â€ ----> 93 ::::: huntsmen?â€
™ ----> 92 ::::: ™
â€˜Yes ----> 92 ::::: â€˜yes
, ----> 97 ::::: ,
â€ ----> 93 ::::: â€
™ ----> 92 ::::: ™
Said ----> 100 ::::: say
the ----> 90 ::::: the
king ----> 92 ::::: king
, ----> 97 ::::: ,
â€˜they ----> 95 ::::: â€˜they
are ----> 87 ::::: be
twelve ----> 93 ::::: twelve
huntsmen.â€ ----> 92 ::::: huntsmen.â€
™ ----> 92 ::::: ™
The ----> 90 ::::: the
lion ----> 92 ::::: lion
continued ----> 100 ::::: continue
: ----> 97 ::::: :
â€˜You ----> 96 ::::: â€˜You

       ----> 103 ::::: 
      
are ----> 100 ::::: be
mistaken ----> 84 ::::: mistaken
, ----> 97 ::::: ,
they ----> 95 ::::: they
are ----> 100 ::::: be
twelve ----> 93 ::::: twelve
girls.â€ ----> 85 ::::: girls.â€
™ ----> 92 ::::: ™
The ----> 90 ::::: the
king ----> 92 ::::: king
Said ----> 100 ::::: say
: ----> 97 ::::: :
â€˜That ----> 90 ::::: â€˜that
can ----> 87 ::::: can
not ----> 94 ::::: not
be ----> 100 ::::: be
true ----> 84 ::::: true
! ----> 97 ::::: !
How ----> 86 ::::: how
will ----> 87 ::::: will
you ----> 95 ::::: you
prove ----> 100 ::::: prove

       ----> 103 ::::: 
      
that ----> 98 ::::: that
to ----> 85 ::::: to
me?â€ ----> 101 ::::: me?â€
™ ----> 96 ::::: ™
â€˜Oh ----> 96 ::::: â€˜Oh
, ----> 97 ::::: ,
just ----> 86 ::::: just
let ----> 100 ::::: let
some ----> 90 ::::: some
peas ----> 92 ::::: pea
be ----> 87 ::::: be
strewn ----> 100 ::::: strew
in ----> 85 ::::: in
the ----> 90 ::::: the
ante ----> 92 ::::: ante
- ----> 97 ::::: -
chamber ----> 92 ::::: chamber
, ----> 97 ::::: ,
â€ ----> 93 ::::: â€
™ ----> 92 ::::: ™
answered ----> 100 ::::: answer
the ----> 90 ::::: the
lion ----> 92 ::::: lion
, ----> 97 ::::: ,
â€˜and ----> 96 ::::: â€˜and

       ----> 103 ::::: 
      
then ----> 86 ::::: then
you ----> 95 ::::: you
will ----> 87 ::::: will
soon ----> 86 ::::: soon
see ----> 100 ::::: see
. ----> 97 ::::: .
Men ----> 92 ::::: man
have ----> 100 ::::: have
a ----> 90 ::::: a
firm ----> 84 ::::: firm
step ----> 92 ::::: step
, ----> 97 ::::: ,
and ----> 89 ::::: and
when ----> 86 ::::: when
they ----> 95 ::::: they
walk ----> 100 ::::: walk
over ----> 85 ::::: over
peas ----> 92 ::::: pea
none ----> 92 ::::: none
of ----> 85 ::::: of
them ----> 95 ::::: they
stir ----> 100 ::::: stir
, ----> 97 ::::: ,

       ----> 103 ::::: 
      
but ----> 89 ::::: but
girls ----> 92 ::::: girl
trip ----> 92 ::::: trip
and ----> 89 ::::: and
skip ----> 100 ::::: skip
, ----> 97 ::::: ,
and ----> 89 ::::: and
drag ----> 100 ::::: drag
their ----> 95 ::::: their
feet ----> 92 ::::: foot
, ----> 97 ::::: ,
and ----> 89 ::::: and
the ----> 90 ::::: the
peas ----> 92 ::::: pea
roll ----> 100 ::::: roll
about.â€ ----> 92 ::::: about.â€
™ ----> 92 ::::: ™
The ----> 90 ::::: the
king ----> 92 ::::: king
was ----> 87 ::::: be
well ----> 86 ::::: well

       ----> 103 ::::: 
      
pleased ----> 84 ::::: pleased
with ----> 85 ::::: with
the ----> 90 ::::: the
counsel ----> 92 ::::: counsel
, ----> 97 ::::: ,
and ----> 89 ::::: and
caused ----> 100 ::::: cause
the ----> 90 ::::: the
peas ----> 92 ::::: pea
to ----> 94 ::::: to
be ----> 87 ::::: be
strewn ----> 100 ::::: strew
. ----> 97 ::::: .

     ----> 103 ::::: 
    
There ----> 95 ::::: there
was ----> 100 ::::: be
, ----> 97 ::::: ,
however ----> 86 ::::: however
, ----> 97 ::::: ,
a ----> 90 ::::: a
servant ----> 92 ::::: servant
of ----> 85 ::::: of
the ----> 90 ::::: the
kingâ€ ----> 96 ::::: kingâ€
™ ----> 96 ::::: ™
s ----> 92 ::::: s
who ----> 95 ::::: who
favoured ----> 100 ::::: favour
the ----> 90 ::::: the
huntsmen ----> 92 ::::: huntsman
, ----> 97 ::::: ,
and ----> 89 ::::: and
when ----> 86 ::::: when
he ----> 95 ::::: he
heard ----> 100 ::::: hear
that ----> 98 ::::: that

       ----> 103 ::::: 
      
they ----> 95 ::::: they
were ----> 87 ::::: be
going ----> 100 ::::: go
to ----> 94 ::::: to
be ----> 87 ::::: be
put ----> 100 ::::: put
to ----> 85 ::::: to
this ----> 90 ::::: this
test ----> 92 ::::: test
he ----> 95 ::::: he
went ----> 100 ::::: go
to ----> 85 ::::: to
them ----> 95 ::::: they
and ----> 89 ::::: and
repeated ----> 100 ::::: repeat
everything ----> 95 ::::: everything
, ----> 97 ::::: ,
and ----> 89 ::::: and
Said ----> 100 ::::: say
: ----> 97 ::::: :
â€˜The ----> 96 ::::: â€˜The

       ----> 103 ::::: 
      
lion ----> 92 ::::: lion
wants ----> 100 ::::: want
to ----> 94 ::::: to
make ----> 100 ::::: make
the ----> 90 ::::: the
king ----> 92 ::::: king
believe ----> 100 ::::: believe
that ----> 98 ::::: that
you ----> 95 ::::: you
are ----> 87 ::::: be
girls.â€ ----> 92 ::::: girls.â€
™ ----> 92 ::::: ™
Then ----> 86 ::::: then
the ----> 90 ::::: the
kingâ€ ----> 96 ::::: kingâ€
™ ----> 96 ::::: ™
s ----> 94 ::::: s
daughter ----> 92 ::::: daughter
thanked ----> 100 ::::: thank
him ----> 95 ::::: he
, ----> 97 ::::: ,

       ----> 103 ::::: 
      
and ----> 89 ::::: and
Said ----> 100 ::::: say
to ----> 85 ::::: to
her ----> 95 ::::: her
maidens ----> 92 ::::: maiden
: ----> 97 ::::: :
â€˜Show ----> 85 ::::: â€˜show
some ----> 90 ::::: some
strength ----> 92 ::::: strength
, ----> 97 ::::: ,
and ----> 89 ::::: and
step ----> 100 ::::: step
firmly ----> 86 ::::: firmly
on ----> 85 ::::: on
the ----> 90 ::::: the
peas.â€ ----> 96 ::::: peas.â€
™ ----> 92 ::::: ™
So ----> 86 ::::: so
next ----> 84 ::::: next
morning ----> 92 ::::: morning

       ----> 103 ::::: 
      
when ----> 86 ::::: when
the ----> 90 ::::: the
king ----> 92 ::::: king
had ----> 100 ::::: have
the ----> 90 ::::: the
twelve ----> 93 ::::: twelve
huntsmen ----> 92 ::::: huntsman
called ----> 100 ::::: call
before ----> 85 ::::: before
him ----> 95 ::::: he
, ----> 97 ::::: ,
and ----> 89 ::::: and
they ----> 95 ::::: they
came ----> 100 ::::: come
into ----> 85 ::::: into
the ----> 90 ::::: the
ante ----> 92 ::::: ante
- ----> 97 ::::: -
chamber ----> 92 ::::: chamber

       ----> 103 ::::: 
      
where ----> 86 ::::: where
the ----> 90 ::::: the
peas ----> 92 ::::: pea
were ----> 87 ::::: be
lying ----> 100 ::::: lie
, ----> 97 ::::: ,
they ----> 95 ::::: they
stepped ----> 100 ::::: step
so ----> 86 ::::: so
firmly ----> 86 ::::: firmly
on ----> 85 ::::: on
them ----> 95 ::::: they
, ----> 97 ::::: ,
and ----> 89 ::::: and
had ----> 100 ::::: have
such ----> 90 ::::: such
a ----> 90 ::::: a
strong ----> 84 ::::: strong
, ----> 97 ::::: ,
sure ----> 84 ::::: sure
walk ----> 92 ::::: walk
, ----> 97 ::::: ,

       ----> 103 ::::: 
      
that ----> 90 ::::: that
not ----> 94 ::::: not
one ----> 93 ::::: one
of ----> 85 ::::: of
the ----> 90 ::::: the
peas ----> 92 ::::: pea
either ----> 89 ::::: either
rolled ----> 100 ::::: roll
or ----> 89 ::::: or
stirred ----> 100 ::::: stir
. ----> 97 ::::: .
Then ----> 86 ::::: then
they ----> 95 ::::: they
went ----> 100 ::::: go
away ----> 86 ::::: away
again ----> 86 ::::: again
, ----> 97 ::::: ,
and ----> 89 ::::: and
the ----> 90 ::::: the
king ----> 92 ::::: king

       ----> 103 ::::: 
      
Said ----> 100 ::::: say
to ----> 85 ::::: to
the ----> 90 ::::: the
lion ----> 92 ::::: lion
: ----> 97 ::::: :
â€˜You ----> 95 ::::: â€˜you
have ----> 87 ::::: have
lied ----> 100 ::::: lie
to ----> 85 ::::: to
me ----> 95 ::::: I
, ----> 97 ::::: ,
they ----> 95 ::::: they
walk ----> 100 ::::: walk
just ----> 86 ::::: just
like ----> 85 ::::: like
men.â€ ----> 92 ::::: men.â€
™ ----> 100 ::::: ™
The ----> 90 ::::: the
lion ----> 92 ::::: lion
Said ----> 100 ::::: say
: ----> 97 ::::: :
â€˜They ----> 95 ::::: â€˜they
have ----> 87 ::::: have

       ----> 103 ::::: 
      
been ----> 87 ::::: be
informed ----> 100 ::::: inform
that ----> 98 ::::: that
they ----> 95 ::::: they
were ----> 87 ::::: be
going ----> 100 ::::: go
to ----> 94 ::::: to
be ----> 87 ::::: be
put ----> 100 ::::: put
to ----> 85 ::::: to
the ----> 90 ::::: the
test ----> 92 ::::: test
, ----> 97 ::::: ,
and ----> 89 ::::: and
have ----> 87 ::::: have
assumed ----> 100 ::::: assume
some ----> 90 ::::: some
strength ----> 92 ::::: strength
. ----> 97 ::::: .
Just ----> 86 ::::: just

       ----> 103 ::::: 
      
let ----> 100 ::::: let
twelve ----> 93 ::::: twelve
spinning ----> 92 ::::: spinning
- ----> 97 ::::: -
wheels ----> 92 ::::: wheel
be ----> 87 ::::: be
brought ----> 100 ::::: bring
into ----> 85 ::::: into
the ----> 90 ::::: the
ante ----> 92 ::::: ante
- ----> 97 ::::: -
chamber ----> 92 ::::: chamber
, ----> 97 ::::: ,
and ----> 89 ::::: and
they ----> 95 ::::: they
will ----> 87 ::::: will
go ----> 100 ::::: go
to ----> 85 ::::: to
them ----> 95 ::::: they
and ----> 89 ::::: and
be ----> 100 ::::: be

       ----> 103 ::::: 
      
pleased ----> 84 ::::: pleased
with ----> 85 ::::: with
them ----> 95 ::::: they
, ----> 97 ::::: ,
and ----> 89 ::::: and
that ----> 90 ::::: that
is ----> 100 ::::: be
what ----> 95 ::::: what
no ----> 90 ::::: no
man ----> 92 ::::: man
would ----> 87 ::::: would
do.â€ ----> 100 ::::: do.â€
™ ----> 92 ::::: ™
The ----> 90 ::::: the
king ----> 92 ::::: king
liked ----> 100 ::::: like
the ----> 90 ::::: the
advice ----> 92 ::::: advice
, ----> 97 ::::: ,
and ----> 89 ::::: and
had ----> 100 ::::: have
the ----> 90 ::::: the

       ----> 103 ::::: 
      
spinning ----> 92 ::::: spinning
- ----> 97 ::::: -
wheels ----> 92 ::::: wheel
placed ----> 100 ::::: place
in ----> 85 ::::: in
the ----> 90 ::::: the
ante ----> 92 ::::: ante
- ----> 97 ::::: -
chamber ----> 92 ::::: chamber
. ----> 97 ::::: .

     ----> 103 ::::: 
    
But ----> 89 ::::: but
the ----> 90 ::::: the
servant ----> 92 ::::: servant
, ----> 97 ::::: ,
who ----> 95 ::::: who
was ----> 100 ::::: be
well ----> 86 ::::: well
disposed ----> 84 ::::: disposed
to ----> 85 ::::: to
the ----> 90 ::::: the
huntsmen ----> 92 ::::: huntsman
, ----> 97 ::::: ,
went ----> 100 ::::: go
to ----> 85 ::::: to
them ----> 95 ::::: they
, ----> 97 ::::: ,
and ----> 89 ::::: and
disclosed ----> 100 ::::: disclose
the ----> 90 ::::: the

       ----> 103 ::::: 
      
project ----> 92 ::::: project
. ----> 97 ::::: .
So ----> 86 ::::: so
when ----> 86 ::::: when
they ----> 95 ::::: they
were ----> 100 ::::: be
alone ----> 84 ::::: alone
the ----> 90 ::::: the
kingâ€ ----> 96 ::::: kingâ€
™ ----> 96 ::::: ™
s ----> 94 ::::: s
daughter ----> 92 ::::: daughter
Said ----> 100 ::::: say
to ----> 85 ::::: to
her ----> 95 ::::: her
  ----> 103 :::::  
eleven ----> 93 ::::: eleven
girls ----> 92 ::::: girl
: ----> 97 ::::: :
â€˜Show ----> 85 ::::: â€˜show
some ----> 90 ::::: some

       ----> 103 ::::: 
      
constraint ----> 92 ::::: constraint
, ----> 97 ::::: ,
and ----> 89 ::::: and
do ----> 87 ::::: do
not ----> 94 ::::: not
look ----> 100 ::::: look
round ----> 86 ::::: round
at ----> 85 ::::: at
the ----> 90 ::::: the
spinning ----> 92 ::::: spinning
- ----> 97 ::::: -
wheels.â€ ----> 92 ::::: wheels.â€
™ ----> 96 ::::: ™
And ----> 89 ::::: and
next ----> 84 ::::: next
morning ----> 92 ::::: morning
when ----> 86 ::::: when
the ----> 90 ::::: the
king ----> 92 ::::: king
had ----> 100 ::::: have

       ----> 103 ::::: 
      
his ----> 95 ::::: his
twelve ----> 93 ::::: twelve
huntsmen ----> 92 ::::: huntsman
summoned ----> 100 ::::: summon
, ----> 97 ::::: ,
they ----> 95 ::::: they
went ----> 100 ::::: go
through ----> 85 ::::: through
the ----> 90 ::::: the
ante ----> 92 ::::: ante
- ----> 97 ::::: -
chamber ----> 92 ::::: chamber
, ----> 97 ::::: ,
and ----> 89 ::::: and
never ----> 86 ::::: never
once ----> 86 ::::: once
looked ----> 100 ::::: look
at ----> 85 ::::: at
the ----> 90 ::::: the

       ----> 103 ::::: 
      
spinning ----> 92 ::::: spinning
- ----> 97 ::::: -
wheels ----> 92 ::::: wheel
. ----> 97 ::::: .
Then ----> 86 ::::: then
the ----> 90 ::::: the
king ----> 92 ::::: king
again ----> 86 ::::: again
Said ----> 100 ::::: say
to ----> 85 ::::: to
the ----> 90 ::::: the
lion ----> 92 ::::: lion
: ----> 97 ::::: :
â€˜You ----> 95 ::::: â€˜you
have ----> 87 ::::: have
deceived ----> 100 ::::: deceive
me ----> 95 ::::: I
, ----> 97 ::::: ,
they ----> 95 ::::: they
are ----> 87 ::::: be
men ----> 92 ::::: man
, ----> 97 ::::: ,

       ----> 103 ::::: 
      
for ----> 85 ::::: for
they ----> 95 ::::: they
have ----> 87 ::::: have
not ----> 94 ::::: not
looked ----> 100 ::::: look
at ----> 85 ::::: at
the ----> 90 ::::: the
spinning ----> 92 ::::: spinning
- ----> 97 ::::: -
wheels.â€ ----> 92 ::::: wheels.â€
™ ----> 92 ::::: ™
The ----> 90 ::::: the
lion ----> 92 ::::: lion
replied ----> 100 ::::: reply
: ----> 97 ::::: :
â€˜They ----> 95 ::::: â€˜they
have ----> 87 ::::: have
restrained ----> 100 ::::: restrain

       ----> 103 ::::: 
      
themselves.â€ ----> 100 ::::: themselves.â€
™ ----> 96 ::::: ™
The ----> 90 ::::: the
king ----> 92 ::::: king
, ----> 97 ::::: ,
however ----> 86 ::::: however
, ----> 97 ::::: ,
would ----> 87 ::::: would
no ----> 86 ::::: no
longer ----> 86 ::::: long
believe ----> 100 ::::: believe
the ----> 90 ::::: the
lion ----> 92 ::::: lion
. ----> 97 ::::: .

     ----> 103 ::::: 
    
The ----> 90 ::::: the
twelve ----> 93 ::::: twelve
huntsmen ----> 92 ::::: huntsman
always ----> 86 ::::: always
followed ----> 100 ::::: follow
the ----> 90 ::::: the
king ----> 92 ::::: king
to ----> 85 ::::: to
the ----> 90 ::::: the
chase ----> 92 ::::: chase
, ----> 97 ::::: ,
and ----> 89 ::::: and
his ----> 95 ::::: his
liking ----> 92 ::::: liking
for ----> 85 ::::: for
them ----> 95 ::::: they

       ----> 103 ::::: 
      
continually ----> 86 ::::: continually
increased ----> 100 ::::: increase
. ----> 97 ::::: .
Now ----> 86 ::::: now
it ----> 95 ::::: it
came ----> 100 ::::: come
to ----> 94 ::::: to
pass ----> 100 ::::: pass
that ----> 90 ::::: that
once ----> 86 ::::: once
when ----> 86 ::::: when
they ----> 95 ::::: they
were ----> 100 ::::: be
out ----> 85 ::::: out
hunting ----> 92 ::::: hunting
, ----> 97 ::::: ,
news ----> 92 ::::: news
came ----> 100 ::::: come

       ----> 103 ::::: 
      
that ----> 98 ::::: that
the ----> 90 ::::: the
kingâ€ ----> 96 ::::: kingâ€
™ ----> 96 ::::: ™
s ----> 94 ::::: s
bride ----> 92 ::::: bride
was ----> 87 ::::: be
approaching ----> 100 ::::: approach
. ----> 97 ::::: .
When ----> 86 ::::: when
the ----> 90 ::::: the
true ----> 84 ::::: true
bride ----> 92 ::::: bride
heard ----> 100 ::::: hear
that ----> 98 ::::: that
, ----> 97 ::::: ,
it ----> 95 ::::: it
hurt ----> 100 ::::: hurt
her ----> 95 ::::: she
so ----> 86 ::::: so
much ----> 84 ::::: much

       ----> 103 ::::: 
      
that ----> 98 ::::: that
her ----> 95 ::::: her
heart ----> 92 ::::: heart
was ----> 100 ::::: be
almost ----> 86 ::::: almost
broken ----> 100 ::::: break
, ----> 97 ::::: ,
and ----> 89 ::::: and
she ----> 95 ::::: she
fell ----> 100 ::::: fall
fainting ----> 100 ::::: faint
to ----> 85 ::::: to
the ----> 90 ::::: the
ground ----> 92 ::::: ground
. ----> 97 ::::: .
The ----> 90 ::::: the
king ----> 92 ::::: king
thought ----> 100 ::::: think

       ----> 103 ::::: 
      
something ----> 95 ::::: something
had ----> 87 ::::: have
happened ----> 100 ::::: happen
to ----> 85 ::::: to
his ----> 95 ::::: his
dear ----> 84 ::::: dear
huntsman ----> 92 ::::: huntsman
, ----> 97 ::::: ,
ran ----> 100 ::::: run
up ----> 85 ::::: up
to ----> 85 ::::: to
him ----> 95 ::::: he
, ----> 97 ::::: ,
wanted ----> 100 ::::: want
to ----> 94 ::::: to
help ----> 100 ::::: help
him ----> 95 ::::: he
, ----> 97 ::::: ,
and ----> 89 ::::: and
drew ----> 100 ::::: draw
his ----> 95 ::::: his

       ----> 103 ::::: 
      
glove ----> 92 ::::: glove
off ----> 85 ::::: off
. ----> 97 ::::: .
Then ----> 86 ::::: then
he ----> 95 ::::: he
saw ----> 100 ::::: see
the ----> 90 ::::: the
ring ----> 92 ::::: ring
which ----> 90 ::::: which
he ----> 95 ::::: he
had ----> 87 ::::: have
given ----> 100 ::::: give
to ----> 85 ::::: to
his ----> 95 ::::: his
first ----> 84 ::::: first
bride ----> 92 ::::: bride
, ----> 97 ::::: ,
and ----> 89 ::::: and
when ----> 86 ::::: when
he ----> 95 ::::: he
looked ----> 100 ::::: look
in ----> 85 ::::: in

       ----> 103 ::::: 
      
her ----> 95 ::::: her
face ----> 92 ::::: face
he ----> 95 ::::: he
recognized ----> 100 ::::: recognize
her ----> 95 ::::: she
. ----> 97 ::::: .
Then ----> 86 ::::: then
his ----> 95 ::::: his
heart ----> 92 ::::: heart
was ----> 87 ::::: be
so ----> 86 ::::: so
touched ----> 100 ::::: touch
that ----> 98 ::::: that
he ----> 95 ::::: he
kissed ----> 100 ::::: kiss
her ----> 95 ::::: she
, ----> 97 ::::: ,
and ----> 89 ::::: and
when ----> 86 ::::: when
she ----> 95 ::::: she

       ----> 103 ::::: 
      
opened ----> 100 ::::: open
her ----> 95 ::::: her
eyes ----> 92 ::::: eye
he ----> 95 ::::: he
Said ----> 100 ::::: say
: ----> 97 ::::: :
â€˜You ----> 95 ::::: â€˜you
are ----> 87 ::::: be
mine ----> 95 ::::: mine
, ----> 97 ::::: ,
and ----> 89 ::::: and
I ----> 95 ::::: I
am ----> 100 ::::: be
yours ----> 95 ::::: yours
, ----> 97 ::::: ,
and ----> 89 ::::: and
no ----> 90 ::::: no
one ----> 92 ::::: one
in ----> 85 ::::: in
the ----> 90 ::::: the
world ----> 92 ::::: world
can ----> 87 ::::: can
alter ----> 100 ::::: alter

       ----> 103 ::::: 
      
that.â€ ----> 96 ::::: that.â€
™ ----> 92 ::::: ™
He ----> 95 ::::: he
sent ----> 100 ::::: send
a ----> 90 ::::: a
messenger ----> 92 ::::: messenger
to ----> 85 ::::: to
the ----> 90 ::::: the
other ----> 84 ::::: other
bride ----> 92 ::::: bride
, ----> 97 ::::: ,
and ----> 89 ::::: and
entreated ----> 100 ::::: entreat
her ----> 95 ::::: she
to ----> 94 ::::: to
return ----> 100 ::::: return
to ----> 85 ::::: to
her ----> 95 ::::: her
own ----> 84 ::::: own
kingdom ----> 92 ::::: kingdom
, ----> 97 ::::: ,

       ----> 103 ::::: 
      
for ----> 85 ::::: for
he ----> 95 ::::: he
had ----> 100 ::::: have
a ----> 90 ::::: a
wife ----> 92 ::::: wife
already ----> 86 ::::: already
, ----> 97 ::::: ,
and ----> 89 ::::: and
someone ----> 95 ::::: someone
who ----> 95 ::::: who
had ----> 87 ::::: have
just ----> 86 ::::: just
found ----> 100 ::::: find
an ----> 90 ::::: an
old ----> 84 ::::: old
key ----> 92 ::::: key
did ----> 87 ::::: do
not ----> 94 ::::: not
require ----> 100 ::::: require
a ----> 90 ::::: a
new ----> 84 ::::: new

       ----> 103 ::::: 
      
one ----> 93 ::::: one
. ----> 97 ::::: .
Thereupon ----> 86 ::::: thereupon
the ----> 90 ::::: the
wedding ----> 92 ::::: wedding
was ----> 87 ::::: be
celebrated ----> 100 ::::: celebrate
, ----> 97 ::::: ,
and ----> 89 ::::: and
the ----> 90 ::::: the
lion ----> 92 ::::: lion
was ----> 87 ::::: be
again ----> 86 ::::: again
taken ----> 100 ::::: take
into ----> 85 ::::: into
favour ----> 92 ::::: favour
, ----> 97 ::::: ,
because ----> 98 ::::: because
, ----> 97 ::::: ,

       ----> 103 ::::: 
      
after ----> 86 ::::: after
all ----> 86 ::::: all
, ----> 97 ::::: ,
he ----> 95 ::::: he
had ----> 87 ::::: have
told ----> 100 ::::: tell
the ----> 90 ::::: the
truth ----> 92 ::::: truth
. ----> 97 ::::: .

   ----> 103 ::::: 
