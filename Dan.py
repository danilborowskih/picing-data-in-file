import pickle , os
import timeit

def sep_exe(func, num_of_members, num_of_failes):
        results_in_one_file = num_of_members // num_of_failes  # результ в одном файле
        iterator_for_start_value = 0  # указывает номер переменной с которой начнется func
        file_iterator = 0  # указывает номер файла
        try:
            while True: # проверка существования файла
                file_name = 'dan/data_'+str(file_iterator)+'.pkl'
                with open(file_name, 'rb') as f:
                    pickle.load(f)
                file_iterator+=1
                iterator_for_start_value+=results_in_one_file
        except:
            print("файлов с данными на момент начала записи ",file_iterator)
      
        while file_iterator < num_of_failes:
            file_name='dan/data_'+str(file_iterator)+'.pkl' # name for file we read

            res_list = [func_result for i, func_result in enumerate(func(iterator_for_start_value))
            if i < results_in_one_file or (file_iterator == num_of_failes - 1)]# здесь мы наполняем лист для записи его в файл

            print(res_list)
            with open(file_name, 'wb') as f:
                pickle.dump(res_list, f)  # записываем в файл
                f.close()
            
            # считаем сколько уже записанно элементов
            iterator_for_start_value += len(res_list)
            file_iterator += 1  # считаем уже заполненные файлы

    # могу не использовать количество файлов (как скажешь семпай)
def load_compl(a):
        try:
            file_iterator = 0 # number of files was read
            one_file_data_list = []
            data_list = []
            while a :
                file_name='dan/data_'+str(file_iterator)+'.pkl' 
                with open(file_name, 'rb') as f:                
                    one_file_data_list=(pickle.load(f))
                file_iterator += 1
                data_list.extend(one_file_data_list)
        except IndexError:  # ошибка чтения 
            print("ошибка при чтении")
        finally:
            print("всего файлов с данными", file_iterator)
            return data_list  # возвращаем данные
