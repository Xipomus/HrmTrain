﻿init -997 python:


  
# Класс - персона
    class Person(Entry):
    
        current = None
        wrd_menu_screen = "person_wrd_menu"
        wrd_menu_main_screen = "person_wrd_menu_main"
    
        # constructor 
        def __init__( self, Name, caption, charData=None, defVals=None, constVals=None):
        
            self.wrd_choice = None
            self.wrd_block = None
            self.wrd_new_len = 0
        
            self.wrd_set_upshirt = False
            self.wrd_set_upskirt = False
            self.wrd_set_downpanties = False
            self.wrd_set_noshirt = False
            
            self.wrd_upshirt = False
            self.wrd_upskirt = False
            self.wrd_downpanties = False
            self.wrd_noshirt = False
            self.wrd_sperm_dried = False
            
            self.wrd_new = []
            self.wrd_new_block = []
            self.wrd_adm = []
            self.wrd_adm_block = []
            self.wrd_wear = []
            self.wrd_wear_block = []
            self.wrd_set = []
            self.wrd_set_block = []
            
            self.wrd_adm_tmp = []
        
            if constVals==None:
                constVals={"caption": caption}
            else:
                constVals.update({"caption": caption})                

            if defVals==None:
                defVals={"liking":0, "whoring":0, "talkTime":0, "giftTime":0}
            else:
                defVals.update({"liking":0, "whoring":0, "talkTime":0})

# Инициализация объектов тела и головы
            if charData!=None:
                charData.clearState()
                defVals.update({"vData": charData, 
                    "body": CharacterExView( 5, 
                        Character(caption, color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed"), "body"+Name ), 
                    "head": CharacterExView( 8, 
                        Character(caption, color="#402313", window_right_padding=220, show_two_window=True, ctc="ctc3", ctc_position="fixed"), "head"+Name )
                    })

                defVals["body"].attach( charData )
                defVals["head"].pushScreenTag( 'head' )
                defVals["head"].attach( charData )
                defVals["body"].data().addItemSet( Name+'_body' )
                defVals["body"].data().addItemSet( Name+'_start_clothes' )

            defVals.update({"curchar": None, "talkingView": "body", "Visible": False})

            super(Person, self).__init__(Name=Name, Type="Person", defVals=defVals, constVals=constVals )

            self.Items=RegEntry(ItemCollection("items"+Name))        # Коллекция ивентов
            self.chibi=RegEntry(Chibi("chibi"+Name))                # Чибик

            return


        def __call__( self, arg1, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None, arg8=None, arg9=None, arg10=None, 
                        arg11=None, arg12=None, arg13=None, arg14=None, arg15=None, arg16=None, arg17=None, arg18=None, arg19=None, 
                        arg20=None, arg21=None, arg22=None, arg23=None, arg24=None):
            self.__args=[]
# Разбираем исходный массив на элементы. На вход могут подаваться строки или Character             
            for o in [arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20, arg21, arg22, arg23, arg24]:
                if o==None:
                    break
                if isinstance( o, ADVCharacter ): # Если ADVCharacter, то добавляем в массив
                    self.__args.append(o)
                else: # Иначе - разбираем на подстроки
                    debug.SaveString("o: "+str(o), 3)
                    for p in o.split("//"):
                        debug.SaveString("p: "+str(p), 3)
                        if p!=None:
                            if p.strip()!=None:
                                self.__args.append(p.strip(" "))
                                debug.SaveString("p.strip: "+str(p.strip(" ")), 3)

# Разобрано, начинаем отображать

# Если было не видимо - показать
            self.__trans=None #d3
            if not self.GetValue("Visible"):
                self.Visibility(self._talkingView, True, self.__trans)
# Если аргументы закончились - прервать                
            for o in self.__args:
                if (o==None) or (o==""):
                    break
                if not isinstance( o, basestring ): # если не строка, значит Character
                    self.curchar=o
                else: # теперь столько строки
                    if o[0]=="~": # если это фейс, то показать его
                        self.Face(o.replace("~",""))    
                    else:
# Если это герой, то скрыть всех персонажей, для которых не указано отбражаться при реплике героя                        
                        if self.Name=="hero": 
                            for p in GetEntriesByType("Person"):
                                if p.Name not in {"hero"}:
                                    if p.GetValue("Visible"):
                                        p.Visibility(p._talkingView, False, None)
#                                    if "body+" not in p._talkingView:
#                                        p.body.hideQ()
#                                        p.SetValue("Visible", False)
#                                    if "head+" not in p._talkingView:
#                                        p.head.hideQ()
#                                        p.SetValue("Visible", False)
                        renpy.say(self.curchar, StringFormat(o))
            return self

# Смена лица персонажа
        def Face(self, s):
# Если есть пробелы - значит это набор стилей бровей, глаз, щек и рта через пробел
# Если нет пробелов - значит название стиля лица
# Если есть точка - значит это имя файла
            if not " " in s:
                if "." in s:
                    self.body.addFaceName( s )
                else:
                    self.body.data().setStyleKey( "face", "face_"+s )
            else:

                self.__temp=s.split(" ")
                for i in range(4):
                    self.body.data().setStyleKey( ['brows', 'eyes', 'blush', 'mouth'][i], ['brows', 'eyes', 'blush', 'mouth'][i]+"_"+self.__temp[i] )

            return

        def Answer(self, pers): # Для конструкций типа   $hero("...").Answer(hermi("...")) - не факт, что будет удобно
            return self


        def ItemSetsCustomize(self, sets, isClear=True): 
            if isClear:
                self.data.mItems.clear() # Удалить все итемы
            for o in sets:
                self.body.data().addItemSet( self.Name+'_'+o )
            return self

        def ItemsCustomize(self, update=None, delete=None): # chibi=None): 
            if delete!=None:
                for o in delete:
                    self.data.delItem( 'item_'+o )

            if update!=None:
                for o in update:
                    oo=o.split(":")
                    self.data.addItem('item_'+oo[0], "default" if len(oo)==1 else oo[0]+"_"+oo[1])

#            if chibi!=None:
#                self.chibi.appearance=chibi

            return self


        def LoadDefItemSets(self): # Пригодилось только один раз - когда изначально подгрузился неправильный набор сетов, перегрузить его в процесс игры
            self.ItemSetsCustomize({"body", "start_clothes"}, True)
#            self.body.data().addItemSet( self.Name+'_body' )
#            self.body.data().addItemSet( self.Name+'_start_clothes' )
            return
                
        def WrdAdd (self, Name = None, Block = None, Type = "new") :
            if Name != None and Block in ["gears_shirt","gears_skirt","gears_other","gears_stockings"] :
                if Type == "new" and not Name in self.wrd_new:
                    self.wrd_new.append(Name)
                    self.wrd_new_block.append(Block)
                elif Type == "adm" and not Name in self.wrd_adm :
                    self.wrd_adm.append(Name)
                    self.wrd_adm_block.append(Block)
                elif Type == "wear" and not Name in self.wrd_wear :
                    self.wrd_wear.append(Name)
                    self.wrd_wear_block.append(Block)
                elif Type == "set" and not Name in self.wrd_set :
                    self.wrd_set.append(Name)
                    self.wrd_set_block.append(Block)
                    
                if self.Items.Count(Name) < 1:
                    self.Items.AddItem (Name,1)
                    
        def WrdRem (self, Name = None, Type = "new") :
            block = self.Items.GetBlock(Name)

            if Name != None and block in ["gears_shirt","gears_skirt","gears_other","gears_stockings"] :
 
                if Type == "new" :
                    i = 0
                    for o in self.wrd_new :
                        if o == Name :
                            del (self.wrd_new[i])
                            del (self.wrd_new_block[i])
                        else :
                            i += 1
                elif Type == "adm" :
                    i = 0
                    for o in self.wrd_adm :
                        if o == Name :
                            del (self.wrd_new[i])
                            del (self.wrd_new_block[i])
                        else :
                            i += 1
                elif Type == "wear" :
                    i = 0
                    for o in self.wrd_wear :
                        if o == Name :
                            del (self.wrd_new[i])
                            del (self.wrd_new_block[i])
                        else :
                            i += 1
                elif Type == "set" :
                    i = 0
                    for o in self.wrd_set :
                        if o == Name :
                            del (self.wrd_new[i])
                            del (self.wrd_new_block[i])
                        else :
                            i += 1
                
        def WrdInit (self) :
            self.WrdAdd("dress","gears_shirt","adm")
            self.WrdAdd("dress","gears_shirt","wear")
            self.WrdAdd("dress","gears_shirt","set")
            self.WrdAdd("skirt","gears_skirt","adm")
            self.WrdAdd("skirt","gears_skirt","wear")
            self.WrdAdd("skirt","gears_skirt","set")
            
            self.WrdAdd("standart2","gears_shirt","new")
            
            self.wrd_set_upshirt = False
            self.wrd_set_upskirt = False
            self.wrd_set_downpanties = False
            self.wrd_set_noshirt = False
            
            self.WrdSetMain()
                
        def WrdDelShirt (self) :   
            i = 0
            for o in self.wrd_wear :
                if self.wrd_wear_block[i] == "gears_shirt" :
                    self.wrd_wear.pop(i)
                    self.wrd_wear_block.pop(i)
                else :
                    i += 1
            self.wrd_set_upshirt = False
        
        def WrdDelSkirt (self) :
            i = 0
            for o in self.wrd_wear :
                if self.wrd_wear_block[i] == "gears_skirt" :
                    self.wrd_wear.pop(i)
                    self.wrd_wear_block.pop(i)
                else :
                    i += 1
            self.wrd_set_upskirt = False
        
        def WrdDelOther (self) :
            i = 0
            for o in self.wrd_wear :
                if self.wrd_wear_block[i] == "gears_other" :
                    self.wrd_wear.pop(i)
                    self.wrd_wear_block.pop(i)
                else :
                    i += 1                    
        
        def WrdDelStockings (self) :                    
            i = 0
            for o in self.wrd_wear :
                if self.wrd_wear_block[i] == "gears_stockings" :
                    self.wrd_wear.pop(i)
                    self.wrd_wear_block.pop(i)
                else :
                    i += 1     
                    
        def WrdDelBlock (self, Block = None) :
            if Block == "gears_shirt" :
                self.WrdDelShirt()
            elif Block == "gears_skirt" :
                self.WrdDelSkirt()
            elif Block == "gears_other" :
                self.WrdDelOther()
            elif Block == "gears_stockings" :
                self.WrdDelStockings()
                
        def WrdSetDelShirt (self) :   
            i = 0
            for o in self.wrd_set :
                if self.wrd_set_block[i] == "gears_shirt" :
                    self.wrd_set.pop(i)
                    self.wrd_set_block.pop(i)
                else :
                    i += 1
        
        def WrdSetDelSkirt (self) :
            i = 0
            for o in self.wrd_set :
                if self.wrd_set_block[i] == "gears_skirt" :
                    self.wrd_set.pop(i)
                    self.wrd_set_block.pop(i)
                else :
                    i += 1
        
        def WrdSetDelOther (self) :
            i = 0
            for o in self.wrd_set :
                if self.wrd_set_block[i] == "gears_other" :
                    self.wrd_set.pop(i)
                    self.wrd_set_block.pop(i)
                else :
                    i += 1                    
        
        def WrdSetDelStockings (self) :                    
            i = 0
            for o in self.wrd_set :
                if self.wrd_set_block[i] == "gears_stockings" :
                    self.wrd_set.pop(i)
                    self.wrd_set_block.pop(i)
                else :
                    i += 1     
                    
        def WrdSetDelBlock (self, Block = None) :
            if Block == "gears_shirt" :
                self.WrdSetDelShirt()
            elif Block == "gears_skirt" :
                self.WrdSetDelSkirt()
            elif Block == "gears_other" :
                self.WrdSetDelOther()
            elif Block == "gears_stockings" :
                self.WrdSetDelStockings()
                
        def WrdIsAdm (self, Name = None) :
            if Name != None and Name in self.wrd_adm :
                return True
            
            return False
                
        def WrdMain (self) :
            self.data.mItems.clear() # Удалить все итемы
            self.body.data().addItemSet( self.Name+'_body' )
            self.body.data().addItem( 'item_tits' )
            self.body.data().addItem( 'item_tits_no' )
            self.body.data().addItem( 'item_panties' )
 
            i = 0
            for o in self.wrd_wear:
                if self.wrd_wear_block[i] == "gears_other" :
                    if self.wrd_upshirt == False and self.wrd_noshirt == False :
                        self.body.data().addItem("item_" + o)
                elif self.wrd_wear_block[i] == "gears_shirt" :
                    if self.wrd_upshirt == True :
                        self.body.data().addItem("item_pose_up_" + o)
                    else :
                        self.body.data().addItem("item_" + o)
                elif self.wrd_wear_block[i] == "gears_skirt" :
                    if self.wrd_upskirt == True :
                        self.body.data().addItem("item_pose_lifted_" + o)
                    else :
                        self.body.data().addItem("item_" + o)
                elif self.wrd_wear_block[i] == "gears_stockings" :
                    self.body.data().addItem("item_" + o)
                i += 1
            if self.wrd_sperm_dried :
                self.body.data().setStyleAll('sperm_dried')
            return self
            
        def WrdSetMain (self) :
            
            self.wrd_upshirt = self.wrd_set_upshirt
            self.wrd_upskirt = self.wrd_set_upskirt
            self.wrd_downpanties = self.wrd_set_downpanties
            self.wrd_noshirt = self.wrd_set_noshirt
            self.wrd_sperm_dried = False
            
            self.wrd_wear = self.wrd_set [ : ]
            self.wrd_wear_block = self.wrd_set_block [ : ]

            self.WrdMain()
            return self
            
        def WrdSetMainBL (self, Face="body_01.png") :
    
            screens.Show(Dissolve(1), "blkfade") #Completely black screen.

            self.WrdSetMain()
            
            self.body.hideshowQQ( Face, pos )
    
            renpy.pause (0.5)
            screens.Hide(Dissolve(1), "blkfade") #Completely black screen.
            screens.Show("ctc").Pause().Hide("ctc")

            return self
            
        def WrdMainBL (self, Face="body_01.png") :

            screens.Show(Dissolve(1), "blkfade") #Completely black screen.
    
            self.WrdMain()

            self.body.hideshowQQ( Face, pos )
    
            renpy.pause (0.5)
            screens.Hide(Dissolve(1), "blkfade") #Completely black screen.
            screens.Show("ctc").Pause().Hide("ctc")

            return self
                
        def WrdSetAddNew (self, Item = None) :
            block = self.Items.GetBlock(Item)
            if Item != None and block in ["gears_shirt","gears_skirt","gears_stockings","gears_other"] :             
                self.WrdAdd(Item,block,"new")   
                
        def WrdSetUnlock (self, Item = None) :
            block = self.Items.GetBlock(Item)
            if Item != None and block in ["gears_shirt","gears_skirt","gears_stockings","gears_other"] :   
                self.WrdRem(Item,"new")
                self.WrdAdd(Item,block,"adm")
            
        def WrdDress (self, Item = None) :
            block = self.Items.GetBlock(Item)
            if Item != None and block in ["gears_shirt","gears_skirt","gears_stockings","gears_other"] :             
                self.WrdDelBlock (block)
                self.WrdAdd(Item, block, "wear")
                if block == "shirt" :
                    self.wrd_noshirt = False
                    self.wrd_upshirt = False
                elif block == "skirt" :
                    self.wrd_upskirt = False  
                self.WrdMain()
                
        def WrdSetDress (self, Item = None) :
            block = self.Items.GetBlock(Item)
            if Item != None and block in ["gears_shirt","gears_skirt","gears_stockings","gears_other"] and Item in self.wrd_adm : 
                self.WrdSetDelBlock (block)
                self.WrdAdd(Item, block, "set")
                if block == "shirt" :
                    self.set_noshirt = False
                    self.set_upshirt = False
                elif block == "skirt" :
                    self.set_upskirt = False  
                self.WrdSetMain()
        
        def WrdUpSkirt (self) :
            self.wrd_upskirt = True
            self.WrdDownShirt() 
            self.WrdMain()
            
        def WrdDownSkirt (self) :
            self.wrd_upskirt = False
            self.WrdMain()
            
        def WrdUpShirt (self) :
            self.wrd_upshirt = True
            self.WrdDownSkirt() 
            self.WrdMain()
            
        def WrdDownShirt (self) :
            self.wrd_upshirt = False
            self.WrdMain()
            
        def WrdNoShirt (self) :
            self.wrd_noshirt = True
            self.WrdDelShirt()
            self.WrdMain()
            
        def WrdNoSkirt (self) :
            self.WrdDelSkirt()
            self.WrdMain()
            
        def WrdNoOther (self) :
            self.WrdDelOther()
            self.WrdMain()
        
        def WrdNoStockings (self) :
            self.WrdDelStockings()
            self.WrdMain()
            
        def WrdSetUpSkirt (self) :
            self.set_upskirt = True
            self.WrdSetDownShirt() 
            self.WrdSetMain()
            
        def WrdSetDownSkirt (self) :
            self.set_upskirt = False
            self.WrdSetMain()
            
        def WrdSetUpShirt (self) :
            self.set_upshirt = True
            self.WrdSetDownSkirt() 
            self.WrdSetMain()
            
        def WrdSetDownShirt (self) :
            self.set_upshirt = False
            self.WrdSetMain()
            
        def WrdSetNoShirt (self) :
            self.set_noshirt = True
            self.WrdSetDelShirt()
            self.WrdSetMain()
            
        def WrdSetNoSkirt (self) :
            self.WrdSetDelSkirt()
            self.WrdSetMain()
            
        def WrdSetNoOther (self) :
            self.WrdSetDelOther()
            self.WrdSetMain()
        
        def WrdSetNoStockings (self) :
            self.WrdSetDelStockings()
            self.WrdSetMain()
            
        def WrdSpermDried (self) :
            self.wrd_sperm_dried = True
            self.wrd_upshirt = False
            self.wrd_upskirt = False
            self.WrdMain()
            
        def WrdNoSpermDried (self) :
            self.wrd_sperm_dried = False
            self.WrdMain()
            
        def WrdMenuRun ( self , block = "new"):
        
            Person.current = self
            self.wrd_block = block

            j = 0
            del self.wrd_adm_tmp[:]
            for i in self.wrd_adm :
                if self.wrd_adm_block[j] == self.wrd_block :
                    self.wrd_adm_tmp.append(i)
                j += 1
            
            renpy.call_screen(Person.wrd_menu_screen)
            
            return
            
        def WrdMenuMainRun ( self ):
        
            Person.current = self
            self.wrd_new_len = len(self.wrd_new)
            self.wrd_block = "main"
            
            while self.wrd_block != "out" :
                if self.wrd_block == "main" :
                    renpy.call_screen(Person.wrd_menu_main_screen)
                elif self.wrd_block != "out" :
                    self.WrdMenuRun (self.wrd_block)
                    if self.wrd_choice != None and self.wrd_block == "new" :
                        renpy.call("wrd_first_" + self.wrd_choice)
                    elif self.wrd_block != "main" :
                        self.WrdSetDress(self.wrd_choice)
                        self.WrdSetMainBL ()
            
            return
            
        def WrdSetChoice (self, iName) :
            self.wrd_choice = iName
            
        def WrdSetBlock (self, iBlock) :
            self.wrd_block = iBlock
        
# Задает видимость персоны. 
# body+ - показывать тело всегда, без плюса только во время реплики, 
# head+ - показывать голову всегда, без плюса только во время реплики
# Например, строка: bodyhead  означает, что во время реплики необходимо показать и голову и тело. а когда говорит герой все скрывать
# isTalking - если истина, то сразу показывать в режиме реплики
        def Visibility(self, talkingView=" ", isTalking=True, transition=None):
            debug.SaveString(self.Name+" "+talkingView+" "+str(isTalking))
            self.SetValue("talkingView", talkingView)
            if self.Name!="hero":
                if (isTalking and ('head' in self._talkingView)) or ('head+' in self._talkingView):
                    self.head.showQ(None, self.pos2, transition)
                else:
                    self.head.hideQ(transition)
                    self.curchar=self.char
                if (isTalking and ('body' in self._talkingView)) or ('body+' in self._talkingView):  
                    self.body.showQ(None, self.pos, transition)
#                    self.SetValue("Visible", True)
                else:
                    self.body.hideQ(transition)
#                    self.SetValue("Visible", False)
                    self.curchar=self.char2

                if isTalking:
                    if len(talkingView)>1: # Если длина строки больше 1 значит она - не пробел и значит что-то теперь отображается
                        self.SetValue("Visible", True)    
                else:
                    if not "+" in talkingView: # Если в строке нет плюса, значит сейчас все спрятано
                        self.SetValue("Visible", False)
            return self

        def State(self, pos=None, pos2=None):
            if pos!=None:
                if isinstance( pos, basestring ):
                    self.pos=self.GetValue("pos_"+pos)
                else:
                    self.pos=pos
            if pos2!=None:
                if isinstance( pos2, basestring ):
                    self.pos2=self.GetValue("pos2_"+pos)
                else:
                    self.pos2=pos2

            return self

        def IsTalk(self):
            return self.GetValue("talkTime")==time.stamp

        def CommitTalk(self):
            return self.SetValue("talkTime", time.stamp) 

        def IsGift(self):
            return self.GetValue("giftTime")==time.stamp 

        def CommitGift(self):
            return self.SetValue("giftTime", time.stamp) 

        @property
        def pos(self):
            return self.GetValue("pos")
        @pos.setter
        def pos(self, value):
            self.SetValue("pos", value)
#            self.body.showQ(None, self.GetValue(value))

        @property
        def pos2(self):
            return self.GetValue("pos2")
        @pos2.setter
        def pos2(self, value):
            self.SetValue("pos2", value)
#            self.head.showQ(None, self.GetValue(value))


        @property
        def data(self):
            return self.body.data()

        @property
        def char(self):
            return self.body.mCh

        @property
        def char2(self):
            return self.head.mCh

        @property
        def curchar(self):
            return self.GetValue("curchar")
        @curchar.setter
        def curchar(self, value):
            self.SetValue("curchar", value)



        @property
        def liking(self):
            return self.GetValue("liking")
        @liking.setter
        def liking(self, value):
            self.SetValue("liking", value, minim=-100, maxim=0)

        @property
        def whoring(self):
            return self.GetValue("whoring")
        @whoring.setter
        def whoring(self, value):
            self.SetValue("whoring", value, minim=0)

        @property
        def body(self):
            return self.GetValue("body")

        @property
        def head(self):
            return self.GetValue("head")
          
            

            
            
screen person_wrd_menu_main:
    add "03_hp/11_misc/bld.png"
    window:
        style "menu_window"
        xalign menu_x
        yalign 0.5

        vbox:
            style "menu"
            spacing 2
            
            if Person.current.wrd_new_len > 0 :
                button :
                    action [Function (Person.current.WrdSetBlock, iBlock = "new"), Return ()] 
                    style "menu_choice_button"

                    text "Новые вещи" style "menu_choice"    
                    
            button :
                action [Function (Person.current.WrdSetBlock, iBlock = "gears_shirt"), Return ()] 
                style "menu_choice_button"

                text "Одежда: Верх" style "menu_choice"  
                    
            button :
                action [Function (Person.current.WrdSetBlock, iBlock = "gears_skirt"), Return ()] 
                style "menu_choice_button"

                text "Одежда: Низ" style "menu_choice"  
                    
            button :
                action [Function (Person.current.WrdSetBlock, iBlock = "gears_stockings"), Return ()] 
                style "menu_choice_button"

                text "Чулки/колготки" style "menu_choice"  
                    
            button :
                action [Function (Person.current.WrdSetBlock, iBlock = "gears_other"), Return ()] 
                style "menu_choice_button"

                text "Прочее" style "menu_choice"
                    
            button:
                action [Function (Person.current.WrdSetBlock, iBlock = "out"), Return ()] 
                style "menu_choice_button"

                text "Назад" style "menu_choice"              
            
            
    zorder 7
            
screen person_wrd_menu:
    add "03_hp/11_misc/bld.png"
    window:
        style "menu_window"
        xalign menu_x
        yalign 0.5

        vbox:
            style "menu"
            spacing 2
            
            if Person.current.wrd_block == "new" :
            
                for i in Person.current.wrd_new :
                    button:
                        action [Function(Person.current.WrdSetChoice, iName=i), Return()] 
                        style "menu_choice_button"

                        text Person.current.Items.GetCaption(i) style "menu_choice"
                        
            else :
                for i in Person.current.wrd_adm_tmp :
                    button:
                        action [Function(Person.current.WrdSetChoice, iName=i), Return()] 
                        style "menu_choice_button"
                            
                        if i in Person.current.wrd_wear :
                            text "{color=222277}" + Person.current.Items.GetCaption(i) + "{/color}" style "menu_choice"
                        else :
                            text Person.current.Items.GetCaption(i) style "menu_choice"
                        
            button:
                action [Function (Person.current.WrdSetBlock, iBlock = "main"), Return ()] 
                style "menu_choice_button"

                text "Назад" style "menu_choice"                



    zorder 7

