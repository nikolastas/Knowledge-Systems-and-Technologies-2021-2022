from owlready2 import *
import datetime
#################
import owlready2
import types
import string
import pandas as pd

onto = get_ontology("file://D:/Users/Nikos/Projects/stg/Part2/songs.nt").load()
# prop = onto.get_namespace("http://www.example.org/props/")
# ns = onto.get_namespace("http://www.example.org/ns/")

with onto:
    prop = onto.get_namespace("http://example.org/props/")
    ns = onto.get_namespace("http://example.org/ns/")
    with ns :
        class Song(Thing):
            # γραφουμε κάτι ;
            pass
        class Composer(Thing):
            pass
        class Year(Thing):
            pass
        class Genres(Thing):
            pass
        class Title(Thing):
            pass
        class Instrument(Thing):
            pass
        class Emotions(Thing):
            pass
        class Publisher(Thing):
            pass
        class Place(Thing):
            pass
    with prop:
        
        class hasDateOfBirth(DataProperty, FunctionalProperty): 
            domain   = [Composer]
            range     = [datetime.date]
            pass
        class hasDateOfDeath(DataProperty, FunctionalProperty): 
            domain   = [Composer]
            range     = [datetime.date]
            pass
        class hasDuration(DataProperty, FunctionalProperty): 
            domain   = [Song]
            range     = [int]
            pass
        class hasYear(DataProperty, FunctionalProperty): 
            domain   = [Song]
            range     = [datetime.date]
            pass

        class hasComposer(ObjectProperty, FunctionalProperty): 
            domain   = [Song]
            range     = [ns.Composer]
            pass
        class hasPlace(ObjectProperty, FunctionalProperty): 
            domain   = [Song]
            range     = [ns.Place]
            pass
        class hasPublisher(ObjectProperty, FunctionalProperty): 
            domain   = [Song]
            range     = [ns.Publisher]
            pass
        class hasTitle(ObjectProperty, FunctionalProperty): 
            domain   = [Song]
            range     = [ns.Title]
            pass
        class hasGenre(ObjectProperty):
            domain = [Song]
            range = [ns.Genres]
            
        class hasEmotion(ObjectProperty):
            domain = [Song]
            range = [ns.Emotions]
            pass


#################
with onto:
    onto.save('myonto1.owl')
