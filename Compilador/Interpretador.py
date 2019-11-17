from Compilador.AnalizadorSemantico import *

listamadre = []

def raquetaGlobo(list, varList):
    rubsList=[]
    subList=[]

    #global rubsList
    for i in range(len(list)):
        if list[i][0] == 0:

            if list[i][1].encode('ascii','ignore') == "Texto":
                subList.append(list[i][3])
                subList.append(list[i][4])
                rubsList.append(subList)
                subList=[]
            if len(list[i])==3:
                subList.append(list[i][1])
                flag=decideIfArray(varList,subList)
                if flag==False:
                    subList.append(list[i][2])
                    rubsList.append(subList)
                    subList=[]
                else:
                    rubsList.append(lookIntElems(varList,subList))
                    subList=[]

            else:
                if len(list[i])==5:
                    subList.append(list[i][3])
                    rubsList.append(lookTextElems(varList,subList,list[i][4]))
                    subList=[]


        if list[i][0] == 1:
            subList.append('Balloon')
            if not isinstance(list[i][1], int):
                name1=changeNames(rubsList,list[i][1],'alt')
                subList.append(rubsList[name1][0])
            if not isinstance(list[i][2],int):
                name2=changeNames(rubsList,list[i][2],'lat')
                subList.append(rubsList[name2][0])
            else:
                subList.append(list[i][1])
                subList.append(list[i][2])
            rubsList.append(subList)
            subList=[]

        if list[i][0] == 2:
            subList.append('START')
            rubsList.append(subList)
            subList=[]
            subList.append('Reps')
            if not isinstance(list[i][1], int):
                name1=changeNames(rubsList,list[i][1],'cantidad')
                subList.append(rubsList[name1][0])
            else:
                subList.append(list[i][1])
            rubsList.append(subList)
            subList=[]

        if list[i][0] == 3:
            subList.append('Random')
            if not isinstance(list[i][1], int):
                name1=changeNames(rubsList,list[i][1],'color')
                subList.append(rubsList[name1][0])
            else:
                subList.append(list[i][1])

            if not isinstance(list[i][2], int):
                name2=changeNames(rubsList,list[i][2],'cant')
                subList.append(rubsList[name2][0])
            else:
                subList.append(list[i][2])

            if not isinstance(list[i][3], int):
                name3=changeNames(rubsList,list[i][3],'tiempo')
                subList.append(rubsList[name3][0])
            else:
                subList.append(list[i][3])

            rubsList.append(subList)
            subList=[]

        if list[i][0] == 5:
            subList.append('Inc')
            if not isinstance(list[i][1], int):
                print(list[i][1])
                name1=changeNames(rubsList,list[i][1],'alt')
                subList.append(rubsList[name1][0])
            else:
                subList.append(list[i][1])
            subList.append(list[i][2])
            rubsList.append(subList)
            subList=[]

        if list[i][0] == 6:
            subList.append('Dec')
            if not isinstance(list[i][1], int):
                name1=changeNames(rubsList,list[i][1],'lat')
                subList.append(rubsList[name1][0])
            else:
                subList.append(list[i][1])
            subList.append(list[i][2])
            rubsList.append(subList)
            subList=[]

        if list[i][0] == 7:
            subList.append('START')
            rubsList.append(subList)
            subList=[]

            subList.append('Reps')
            subList.append(list[i][1])
            rubsList.append(subList)
            subList=[]

            subList.append('Random')
            if not isinstance(list[i][4], int):
                name1=changeNames(rubsList,list[i][4],'cant')
                subList.append(rubsList[name1][0])
            else:
                subList.append(list[i][4])

            if not isinstance(list[i][5], int):
                name2=changeNames(rubsList,list[i][5],'tiempo')
                subList.append(rubsList[name2][0])
            else:
                subList.append(list[i][5])
            rubsList.append(subList)
            subList=[]

        if list[i][0]==8:

            if not isinstance(list[i][3], int):
                name1=changeNames(rubsList,list[i][3],'palabra')
                subList.append(rubsList[name1][0])
            else:
                subList.append(list[i][3])

            if not isinstance(list[i][4], int):
                name2=changeNames(rubsList,list[i][4],'puntaje')
                subList.append(rubsList[name2][0])
            else:
                subList.append(list[i][4])

            if not isinstance(list[i][1], int):
                name3=changeNames(rubsList,list[i][1],'fila')
                subList.append(rubsList[name3][0])
            else:
                subList.append(list[i][1])

            if not isinstance(list[i][2], int):
                name4=changeNames(rubsList,list[i][2],'columna')
                subList.append(rubsList[name4][0])
            else:
                subList.append(list[i][2])

            # eraser=addParameters(subList,rubsList)
            #
            # rubsList.append(eraser[0])
            # rubsList.append(eraser[1])
            # rubsList.append(eraser[2])
            # rubsList.append(eraser[3])
            rubsList.append(subList)
            subList=[]


        if list[i][0] ==9:
            subList.append('TelaArana')
            subList.append(list[i][1])
            subList.append(list[i][2])
            rubsList.append(subList)
            subList=[]

        if list[i][0] ==10:
            subList.append('Object')
            if len(list[i])==5:
                subArray=[]
                if not isinstance(list[i][1], int):
                    name1=changeNames(rubsList,list[i][1],'altura')
                    subList.append(rubsList[name1][0])
                else:
                    subList.append(list[i][1])
                if not isinstance(list[i][2], int):
                    name2=changeNames(rubsList,list[i][2],'longitud')
                    subArray.append(rubsList[name2][0])
                else:
                    subArray.append(list[i][2])
                subArray.append(list[i][3])
                subList.append(subArray)
                if not isinstance(list[i][4], int):
                    name3=changeNames(rubsList,list[i][4],'second')
                    subList.append(rubsList[name3][0])
                else:
                    subList.append(list[i][4])
                rubsList.append(subList)
                subList=[]

            else:
                if not isinstance(list[i][1], int):
                    name1=changeNames(rubsList,list[i][1],'altura')
                    subList.append(rubsList[name1][0])
                else:
                    subList.append(list[i][1])

                if not isinstance(list[i][2], int):
                    name2=changeNames(rubsList,list[i][2],'longitud')
                    subList.append(rubsList[name2][0])
                else:
                    subList.append(list[i][2])

                if not isinstance(list[i][3], int):
                    name3=changeNames(rubsList,list[i][3],'second')
                    subList.append(rubsList[name3][0])
                else:
                    subList.append(list[i][3])
                rubsList.append(subList)
                subList=[]

        if list[i][0] ==11:
            subList.append('START')
            rubsList.append(subList)
            subList=[]
            subList.append('Reps')
            subList.append(list[i][2])
            subList.append(list[i][1])
            rubsList.append(subList)
            subList=[]

        if not isinstance(list[i][0],int):

            if list[i][0].encode('ascii','ignore') == "FOREND".encode('ascii','ignore'):
                subList.append('END')
                rubsList.append(subList)
                subList=[]

            if list[i][0].encode('ascii','ignore') == "ENDDO".encode('ascii','ignore'):
                subList.append('END')
                rubsList.append(subList)
                subList=[]

            if list[i][0].encode('ascii','ignore') == "game".encode('ascii','ignore'):
                rubsList.append("game")
                subList=[]
            if list[i][0].encode('ascii','ignore') == "END".encode('ascii','ignore'):
                rubsList.append("END")
                subList=[]

    print("inicia el perreo")
    print(rubsList)
    listamadre = rubsList
    return rubsList

def lookIntElems(varList,subList):
    for i in range(len(varList)):

        if not isinstance(varList[i],int):
            if varList[i].encode('ascii','ignore')==subList[0].encode('ascii','ignore'):
                if (len(varList)-1 )==i:
                    subList.append("")
                    return subList
                if i+3<=len(varList)-1:
                    if not isinstance(varList[i+3],int):
                        if varList[i+3].encode('ascii','ignore') != "ArrayPart".encode('ascii','ignore'):
                            subList.append("")
                            return subList
                if not isinstance(varList[i+1],int):
                    i=i+2
                else:
                    i=i+1
                cont=1

                while(True):
                    subList.append(varList[i])
                    if (len(varList)-1 )==i:
                        return subList
                    if i+3 <= len(varList)-1:
                        if not isinstance(varList[i+3],int):
                            if varList[i+3].encode('ascii','ignore') != "ArrayPart".encode('ascii','ignore'):
                                return subList
                    i=i+2
                    cont+=1
                return subList;
def lookTextElems(varList,subList,lenght ):
    for i in range(len(varList)):
        if not isinstance(varList[i],int):
            if varList[i].encode('ascii','ignore')==subList[0].encode('ascii','ignore'):
                if (len(varList)-1 )==i:
                    subList.append("")
                    return subList
                if i+2<=len(varList)-1:
                    if not isinstance(varList[i+2],int):
                        if varList[i+2].encode('ascii','ignore') != "ArrayPart".encode('ascii','ignore'):
                            return subList
                i=i+1
                cont=1
                while(cont<=lenght):
                    subList.append(varList[i])
                    if (len(varList)-1 )==i:
                        return subList
                    if i+3 <= len(varList)-1:
                        if not isinstance(varList[i+3],int):
                            if varList[i+3].encode('ascii','ignore') != "ArrayPart".encode('ascii','ignore'):
                                return subList
                    i=i+2
                    cont+=1
                return subList;

def decideIfArray(varList,subList):
    for i in range(len(varList)):
        if not isinstance(varList[i],int):
            if varList[i].encode('ascii','ignore')==subList[0].encode('ascii','ignore'):
                if not isinstance(varList[i],int):
                    if varList[i-1]!="Index":

                        return False
                else:
                    return True

def changeNames(rubsList,toChange,newName):
    for i in range(len(rubsList)):
        if rubsList[i][0]==toChange:
            rubsList[i][0]=newName
            return i

def addParameters(subList,rubsList):
    lista=[1,2,3,4]
    for i in range(len(rubsList)):

        if rubsList[i][0]==subList[0]:
            lista[0]=rubsList[i]

        if rubsList[i][0]==subList[1]:
            lista[1]=rubsList[i]

        if rubsList[i][0]==subList[2]:
            lista[2]=rubsList[i]

        if rubsList[i][0]==subList[3]:
            lista[3]=rubsList[i]

    return lista