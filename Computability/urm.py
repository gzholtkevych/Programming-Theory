isnat = lambda x : isinstance(x, int) and x >= 0


class Data:
    """
    """
    def __init__(self, *args):
        """creates a dataunit and initialize its values

        Raises:
        ----------
            ValueError if at least one argument is not a natural
                number
        """
        if args is None:
            self._memory = []
        elif not all(map(isnat, args)):
            raise ValueError("incorrect data")
        else:
            self._memory = list(args)

    def write(self, addr, val):
        """writes value 'val' at address 'addr'
        
        Assumptions (are not checked):
        ------------------------------
            addr and val are both natural numbers
        """
        offset = addr - len(self._memory)
        if offset >= 0:
            self._memory.extend((offset + 1) * [0])
        self._memory[addr] = val

    def read(self, addr):
        """returns value at address 'addr'
        
        Assumption (is not checked):
        ----------------------------
            addr is a natural number
        """
        if addr >= len(self._memory):
            return 0
        else:
            return self._memory[addr]


class Instruction:
    def __init__(self, *args):
        """creates URM-instruction

        Raises:
        -------
            ValueError if 'args' are incorrect
        """
        if args is None or not all(map(isnat, args)):
            raise ValueError("invalid instruction")
        if len(args) == 2 and args[0] <= 1:
            self._irator = args[0]
            self._irand1 = args[1]
        elif len(args) == 3 and args[0] == 2:
            self._irator = args[0]
            self._irand1 = args[1]
            self._irand2 = args[2]
        elif len(args) == 4 and args[0] == 3:
            self._irator = args[0]
            self._irand1 = args[1]
            self._irand2 = args[2]
            self._irand3 = args[3]
        else:
            raise ValueError("invalid instruction")

    def __str__(self):
        INAMES = ['Z', 'S', 'T', 'J']
        repr = INAMES[self._irator] + "(" + str(self._irand1)
        if self._irator >= 2:
            repr += (", " + str(self._irand2))
        if self._irator == 3:
            repr += (", " + str(self._irand3))
        repr += ")"
        return repr 


    def do(self, data):
        """executes the instruction 'self'

        Returns:
        --------
            None  if the next instruction is implicitly specified
            nat   if the next instruction is explicitly specified
        """
        if self._irator == 0:
            data.write(self.irand1, 0)
            return None
        elif self._irator == 1:
            data.write(self._irand1, data.read(self._irand1) + 1)
            return None
        elif self._irator == 2:
            data.write(data.read(self._irand1), self._irand2)
            return None
        elif (
            self._irator == 3 and
            data.read(self._irand1) == data.read(self._irand2)
        ):
            return self._irand3
        else:
            return None


is_program = lambda x : (
    isinstance(x, list) and
    all(map(lambda y: isinstance(y, Instruction), x))
)


def run(program, data, check=True):
    """URM simulator

    Arguments:
    ----------
        program  URM-program
        data     input data
        check    boolean flag for turning on/off argument
                    correctness checking
    Returns:
    --------
        the computation result
    """
    if check and not is_program(program):
        raise ValueError("invalid URM-program")
    if check and not isinstance(data, Data):
        raise ValueError("invalid data for URM-computation")
    ic = 0  # instruction counter
    lop = len(program)
    while ic < lop:
        inext = program[ic].do(data)
        if inext is None:
            ic += 1
        else:
            ic = inext
    return data.read(0)


def translate_instruction(line):
    """checks string 'line' is URM-instruction and translates it"""
    if not isinstance(line, str):
        raise ValueError("invalid instruction line")
    head, sep, tail = line.partition(":")
    if sep:
        line = tail
    line = line.strip()
    head, sep, tail = line.partition("(")
    if not sep:
        raise ValueError("invalid instruction line")
    icode = head.strip()
    line, sep, tail = tail.partition(")")
    if not sep:
        raise ValueError("invalid instruction line")
    words = line.split(",")
    try:
        args = list(map(int, words))
    except:
        raise ValueError("invalid instruction line")
    if icode == 'Z' and len(args) == 1:
        return Instruction(0, *args)
    elif icode == 'S' and len(args) == 1:
        return Instruction(1, *args)
    elif icode == 'T' and len(args) == 2:
        return Instruction(2, *args)
    elif icode == 'J' and len(args) == 3:
        return Instruction(3, *args)
    else:
        raise ValueError("invalid instruction line")

def compile(source):
    """
    """
    if isinstance(source, list):
        return [translate_instruction(line) for line in source]
    elif isinstance(source, str):
        try:
            file = open(source, 'r')
            program = []
            for line in file:
                program.append(translate_instruction(line))
        except IOError:
            raise Exception("file error")
        except: 
            raise ValueError("source problem")
        finally:
            try:
                file.close()
            except:
                pass
        return program
    else:
        raise ValueError("invalid source")

