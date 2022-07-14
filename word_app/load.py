import os
import random
from datetime import datetime
from .utils.ECDICT.stardict import DictCsv

#print(os.getcwd())

class word_app():
    
    def __init__(self) -> None:
        self.words_not_in_dict=[]
        self.dict,self.word_list=self.Load()
        random.seed(datetime.now().microsecond)

    def Load(self):
        dict=DictCsv('word_app/utils/ECDICT/ecdict.csv')
        wordfile=open("wordtable.txt","r")
        word_list=[  [x.strip() for x in line.split(',')]  for line in wordfile if line.split()!=[]]
        return dict,word_list

    def random_word(self):
        return self.word_list[random.randint(0,len(self.word_list)-1)]

    def get_list(self,size=20):
        tmp_word_list=self.word_list[:]
        random.shuffle(tmp_word_list)
        size=min(size,len(tmp_word_list))
        tmp_word_list=tmp_word_list[0:size]

        return tmp_word_list

    def generate_word_note(self,num=1,size=20,lang=''):
        for i in range(num):
            with open('output/wordnote'+str(i)+'_'+lang+'.txt', 'w',encoding='utf-8') as fp:
                L=self.get_list(size)
                for line in L:
                    #s=','.join(line)
                    #s+='\n'
                    if lang=='english':
                        for x in line:
                            #print(type(dict.query(x)['definition']))
                            #break
                            if x not in self.dict:
                                self.words_not_in_dict.append(x)
                            else :
                                fp.write("%s\n\t%s\n" %(x,self.dict.query(x)['definition'].replace('\n','\n\t') )) 
                                #s+=dict.query(x)['definition']
                    elif lang=='chinese':
                        for x in line:
                            #print(dict.query(x)['definition'])
                            #break
                            #print(x)
                            if x not in self.dict:
                                self.words_not_in_dict.append(x)   
                            else :     
                                fp.write("%s\n\t%s\n" %(x,self.dict.query(x)['translation'].replace('\n','\n\t'))) 
                    else:
                        for x in line:
                            fp.write("%s\n" %x)        
                    #s+='\n'
                    fp.write('\n')


    # def generate_word_note_withenglish(num=1,size=20):
    #     for i in range(num):
    #         with open('output/wordnote'+str(i)+'_english.txt', 'w') as fp:
    #             L=get_list(size)
    #             for line in L:
    #                 s=','.join(line)
    #                 s+='\n'
    #                 for x in line:
    #                     #print(dict.query(x)['definition'])
    #                     #break
    #                     s+=dict.query(x)['definition']
    #                 s+='\n'
    #                 fp.write(s)


    # def generate_word_note_withchinese(num=1,size=20):
    #     for i in range(num):
    #         with open('output/wordnote'+str(i)+'_chinese.txt', 'w') as fp:
    #             L=get_list(size)
    #             for line in L:
    #                 s=','.join(line)
    #                 s+='\n'
    #                 for x in line:
    #                     #print(dict.query(x))
    #                     #break
    #                     s+=dict.query(x)['translation']
    #                 s+='\n'
    #                 fp.write(s)


if __name__=="__main__":
    app=word_app()
    app.generate_word_note(lang='')
    app.generate_word_note(size=200,lang='english')
    app.generate_word_note(lang='chinese')

    

    if len(app.words_not_in_dict)>0:
        print('\n'+'########################---WARNING---##########################'+'\n')
        print('Some words DO NOT APPEAR in the DICTIONARY')
        app.words_not_in_dict=list(set(app.words_not_in_dict))
        print(app.words_not_in_dict)

        print('\n'+'########################---WARNING---##########################'+'\n')



#print(dict.query('tide sb over'))