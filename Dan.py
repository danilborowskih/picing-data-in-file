import pickle , os
import timeit
#эта версия в функциях но без numpy
class MyClass:

    def __init__(self,func,num_of_res,num_of_blocks):
        self.func = func
        self.res_num = num_of_res
        self.dir_of_res = 'my_directory'
        self.path_arr = [os.path.join(self.dir_of_res, f'{i}') for i in range(num_of_blocks)]
        self.step = num_of_res // num_of_blocks  # результ в одном файле
        self.num_of_blocks = num_of_blocks

    def __len__(self):
        return self.len
    
    def Load(self, path) -> list:# возвращает список pickl
        with open(path, 'rb') as f:
            return pickle.load(f)

    def file_exist(self) -> int: # возвращает количество уже заполненных не поврежденных файлов
        if not os.path.exists(self.dir_of_res):
            os.mkdir(self.dir_of_res)
            return 0
        l = len(os.listdir(self.dir_of_res))
        n = 0 
        for i in range(l):
            try:
                with open(self.path_arr[i], 'rb') as f:
                    pickle.load(f)
                n+=1
            except:
                break
        return n
    
    def fill_results_in_list(self,file_iter)->list:
        return [func_result for i, func_result in enumerate(self.func(file_iter*self.step))
                if i < self.step or (file_iter == self.num_of_blocks - 1)]# здесь мы наполняем лист для записи его в файл
                
    def Dump(self,reslist,i):
        with open(self.path_arr[i],'wb') as f:
            pickle.dump(reslist,f)

    def sep_exe(self):
            file_iterator = MyClass.file_exist(self)  # указывает номер файла который будем заполнять
            iterator_for_start_value = file_iterator*self.step  # указывает номер переменной с которой начнется func
            print(file_iterator)
            while file_iterator < self.num_of_blocks:
                res_list = MyClass.fill_results_in_list(self,file_iterator)
                MyClass.Dump(self,res_list,file_iterator)  # записываем в файл
                file_iterator += 1  # считаем уже заполненные файлы
    
    def load_compl(self):
        file_iter = MyClass.file_exist(self)
        res_list=[]
        for i in range(file_iter) :
            res_list = MyClass.Load(self,self.path_arr[i])
            print(res_list)



def some_func(start):
    for i in range(start,33):
        yield i**2
if __name__=='__main__':
    test = MyClass(some_func,33,5)
    test.sep_exe()
    test.load_compl()