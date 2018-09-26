####################################################
##
##    Kazuki Amakawa's Neural Network
##    main.py
##    Copyright(c) by Kazuki Amakawa, all right reserved
##
####################################################
import Init
import Setting 

SufixSet = Setting.DataClass
FileDir = Setting.InputFolder
ModelSave = Setting.ModelSave
OutputDir = Setting.OutputFolder
ModelDir = Setting.ModelFolder
TestDir = Setting.TestFolder
Iteration = Setting.iteration

def TrainMain(Presentation):
    import Train
    tem, Data, Result = Train.Pretreatment(FileDir, SufixSet, ModelSave)
    if tem:
        Error(tem)        
        return

    tem = Train.Train(Data, Result, ModelSave, Iteration, Presentation)
    if tem:
        Error(tem)
        return
    return
    


def TestMain(Presentation):
    import Test
    tem, TestData, FileNames = Test.Pretreatment(TestDir, SufixSet, ModelDir)
    if tem:
        Error(tem)
        return 
    
    tem = Test.Test(TestData, ModelDir, OutputDir, FileNames)
    if tem:
        Error(tem)
        return
    return



def Error(code):
    """
    All error will be treated in this funtion, it is necesasry to input error
    code into this function
    """
    print()
    print()
    code += 100
    print("Error " + str(code) + "\t:   ", end = "")
    if code - 100 == 1:
        print("No parameter, using `main help` to determine the parameter of program")
    elif code - 100 == 2:
        print("No folder")
    elif code - 100 == 3:
        print("sufix array is empty, please determine the kind of files will be used is folder")
    elif code - 100 == 4:
        print("yuv error, please using yuv2rgb before learning")
    elif code - 100 == 5:
        print("train data lacked, please have files in 0 and 1")
    elif code - 100 == 6:
        print("model saving folder is not exist")
    elif code - 100 == 7:
        print("test data is not be found")
    elif code - 100 == 8:
        print("make setting error, the parameter p only have 0 and 1 value")
    else:
        print("Unknown error, please connect the author and administrator")
    
    print("For more help, please using command `make help`")
    return


if __name__ == '__main__':
    import sys
    Init.StaClear()
    if len(sys.argv) != 3:
        Error(1)
    elif sys.argv[2] != "0" and sys.argv[2] != "1":
        Error(8)
    elif sys.argv[1] == "-l":
        TrainMain(int(sys.argv[2]))
    elif sys.argv[1] == "-t":
        TestMain(int(sys.argv[2]))
        
    





