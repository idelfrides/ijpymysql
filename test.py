from textwrap import dedent
from managers import DataFromTerminal


def data_from_terminal():
    
    data = DataFromTerminal()

    print(dedent("""
        ---------------------------------
            INFORMING DATA FOR ONE DEV
        ---------------------------------
            """)
        )
    
    ind = 0
    dev_data = list()
    attr_type = [
        'alpha',
        'alpha',
        'numeric',
        'alpha',
        'alphanum'
    ]
     
    for attr in ['name', 'company', 'salary', 'role', 'adress']:
        try:
            print('\n Getting a value to attribute {}'
                .format(attr))
            attr_value = input('\n Enter the value:  ')
        except KeyboardInterrupt as kbi_exc:
            print('\n Program interrupted by user \n {}'
                .format(kbi_exc)
            )
            exit(0)
        else:
            if not data.attrib_validation(attr_value, attr_type[ind]):
                data.show_warning(attr)
                data_from_terminal()
        dev_data.append(attr_value.strip())
        ind += 1
        
    #        name, company, salary, role, adress
    # return name, company, salary, role, adress
    return dev_data


def data_from_terminal_many():

    data = DataFromTerminal()

    print(dedent("""
        ------------------------------------
            INFORMING DATA FOR MANY DEV
        ------------------------------------

        """)
    )
        
    records = data.define_records_number() 

    all_dev_data = list()
        
    for ind in range(records):
        print(dedent("""
            --------------------------------
                    DATA FOR DEV {}
            --------------------------------
            
            """.format(ind+1))
        )
            
        one_dev_data = data_from_terminal()
        all_dev_data.append(one_dev_data)

    return all_dev_data



if __name__ == "__main__":
    d = data_from_terminal_many()
    print('\n\n\n DATA:  ', d)
    print('\n\n')

