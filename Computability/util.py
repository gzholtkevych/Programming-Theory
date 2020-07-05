"""Module contains some auxiliary functions used by URM model""" 

from numbers import Number


def nat(x) :
    """Smart constructor for naturals

    Arg
        x: any literal
    Returns:
        natural value
    Raises:
        ValueError if x cannot be converted into int
        or the result of this conversation is negative
    """
    try:
        n = int(x)
    except Exception as ex:
        raise ValueError("invalid literal for nat()")
    if n < 0:
        raise ValueError("invalid literal for nat()")
    return n


def isnat(x):  # 
    """Function checks whether x is a natural number"""
    return isinstance(x, int) and (x >= 0)


def statement(*args):
    """Smart constructor for URM-statement.

    Args:
        args: a sequence of naturals
    Raises
        ValueError if 'args' is incorrect for constructing
            URM-statement
    """
    try:
        if len(args) == 2 and (args[0] == 0 or args[0] == 1):
            return args  # statement Z(n) or S(n) has been created
        elif len(args) == 3 and args[0] == 2:
            return args  # statement T(n,m) has been created
        elif len(args) == 4 and args[0] == 3:
            return args  # statement J(n,m,k) has been created
        else:
            raise ValueError("invalid args for statement()")
    except:
        raise ValueError("invalid args for statement()")


def parse_line(line):
    """Parser of a line into a URM-statenet

    Args:
        line: string for parsing
    Returns
        URM-statement
    """
    stm_table = {'Z': 0, 'S': 1, 'T': 2, 'J': 3}
    aux1, _, aux2 = line.partition('(')
    code = aux1.strip()
    aux1, _, _ = aux2.partition(')')
    try:
        aux2 = list(map(nat, aux1.split(',')))
    except:
        raise ValueError(
            "invalid statement format: '{}'".format(line))
    code =  stm_table.get(code)
    if code is None:
        code = 10
    aux1 = [code] + aux2 
    return statement(*aux1)


def program(source):
    """Smart constructor for URM-program

    Args:
        source: list of statements or file name
    Raises
        ValueError if 'source' is invalid
    """
    if isinstance(source, str):  # source is a file
        fname = source; del source; source = []
        try:
            file = open(fname, "r")
            del source
            source = []
            for line in file:
                source.append(line)
        except:
            raise ValueError(
                "problem with file '{}' "
                "in program()".format(fname))
        finally:
            try:
                file.close()
            except:
                pass
    elif not isinstance(source, list):  #
        raise ValueError("invalid arguments for program()")
    # below 'source' is list of lines
    try:
        return list(map(parse_line, source))
    except Exception as ex:
        raise ex
