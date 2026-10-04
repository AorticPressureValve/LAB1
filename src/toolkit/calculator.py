import src.toolkit.errors as error

alphabet = '1234567890-+/*'

def tokenize_fsm(expression: str):
    tokens = []
    state = 'START' #state for searching characters on algorithm's start or new characters after adding a token
    current_token = ''
    

    for char in expression:
        
        if char in alphabet:

            if state == 'START':

                if char.isdigit():
                    state = 'NUMBER' # finding numbers
                    current_token = char

                elif char.isspace():
                    pass

                elif char in '+-*/':
                    current_token = char
                    tokens.append(('OPERATOR', str(current_token)))
                    current_token = '' #get operator token


            elif state == 'NUMBER': #if number is found

                if char.isdigit() or char == '.':
                    current_token += char      #getting whole number if longer than 1 digit
                
                else:
                    tokens.append(('NUMBER', float(current_token)))
                    current_token = ''
                    state = 'START'
                    if char in '+-*/':
                        current_token = char
                        tokens.append(('OPERATOR', str(current_token)))
                        current_token = ''
        
        elif len(expression) < 1:
            raise error.NothingError()
        else:
            raise error.NotSupportedCharacter(char)
        
    if state == 'NUMBER': 
        tokens.append(('NUMBER', float(current_token)))
        current_token = ''
        
    return tokens

tokens = []



def calc(tokens):
    tokens = tokenize_fsm(tokens)
    
                #       CAUTION 
    #            ENTERING IF ELSE FOREST
    #               MAP RECCOMENDED
    
    programm = 'first_route'
    acc = 0
    state = 'START'
    not_used_tokens = tokens[:] #dynamic list of operators for cycle
    current_tokens = tokens[:]
    SIGN_MULTIPLIER = 1

    while programm != 'FINISHED':

        if programm == 'first_route':

            for i in range(len(current_tokens)):
                current_definition = current_tokens[i][0]
                if state == 'START':
                    if current_definition == 'NUMBER':
                        acc += current_tokens[i][1]
                        state = 'CALC'
                    elif current_definition == 'OPERATOR':
                        if current_tokens[i][1] == '-':
                            state = 'NEGATIVE_START'
                            not_used_tokens[i] = (('OPERATOR', 'USED'))
                        else:
                            raise error.ZeroDisivionError()
                        
                elif state == 'NEGATIVE_START':
                    if current_definition == 'NUMBER':
                        acc = current_tokens[i][1] * (-1)
                        not_used_tokens[i] = (('NUMBER', acc))
                        state = 'CALC'
                
                elif state == 'CALC':
                    if current_definition == 'OPERATOR':
                        if current_tokens[i][1] == '*':
                            state = 'CALC_MULTIPLICATION'
                        elif current_tokens[i][1] == '/':
                            state = 'CALC_DIVISION'
                        else:
                            not_used_tokens[i-1] = (('NUMBER', acc))
                            not_used_tokens[i] = (('OPERATOR', current_tokens[i][1]))
                            acc = 0
                            state = 'START'
                    else:
                        state = 'error'
                        error = 'no operator'
                        exit()
                
                elif state == 'CALC_MULTIPLICATION' or state == 'CALC_DIVISION':
                    if current_definition == 'NUMBER':
                        if state == 'CALC_DIVISION':
                            acc = acc / current_tokens[i][1] * SIGN_MULTIPLIER
                            not_used_tokens[i] = (('NUMBER', acc))
                            not_used_tokens[i-1] = (('OPERATOR', 'USED'))
                            not_used_tokens[i-2] = (('NUMBER', 'USED'))
                            state = 'CALC'
                        elif state == 'CALC_MULTIPLICATION':
                            acc = acc * current_tokens[i][1] * SIGN_MULTIPLIER
                            SIGN_MULTIPLIER = 1
                            not_used_tokens[i] = (('NUMBER', acc))
                            not_used_tokens[i-1] = (('OPERATOR', 'USED'))
                            not_used_tokens[i-2] = (('NUMBER', 'USED'))
                            state = 'CALC'
                    elif current_definition == "OPERATOR" and current_tokens[i][1] == '-':
                        SIGN_MULTIPLIER = -1
                        not_used_tokens[i-2] = (('NUMBER', 'USED'))

            programm = 'second_route'
            current_tokens = not_used_tokens[:]
            state = 'START'
            acc = 0

        elif programm == 'second_route':
            for i in range(len(current_tokens)):
                current_definition = current_tokens[i][0]

                if current_tokens[i][1] == 'USED':
                    pass

                elif state == 'START':

                    if current_definition == 'NUMBER':
                        acc = current_tokens[i][1]
                        state = 'CALC'
                    elif current_definition == 'OPERATOR' and current_tokens[i][1] == '-':
                        SIGN_MULTIPLIER = SIGN_MULTIPLIER * -1
                        state = 'CALC'

                elif state == 'CALC':
                    if current_definition == 'OPERATOR':

                        if current_tokens[i][1] == '-':
                            SIGN_MULTIPLIER = SIGN_MULTIPLIER * -1
                        elif current_tokens[i][1] == '+':
                            pass
                    
                    elif current_definition == 'NUMBER':
                        acc = acc + (current_tokens[i][1] * SIGN_MULTIPLIER)

            programm = 'FINISHED'
    return acc
