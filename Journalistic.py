import os

pos = [
    "good",
    "amazing",
    "well",
    "life",
    "living",
    "well-kept",
    "finished",
    "fishing",
    "boys",
    "girls",
    "men",
    "women",
    "drinks",
    "family",
    "friends",
    "happy",
    "bar",
    "congratulations",
    "congrats",
    "good",
    "fabulous",
    "best",
    "brilliant",
    "outstanding",
    "glad",
    "cheerful",
    "joyful",
    "joy",
    "gratitude",
    "thanks",
    "thank",
    "fun",
    "love",
    "cute",
    "loved",
    "loving",
    "enjoy",
    "enjoyment",
    "enjoyed",
    "enjoying",
    "understanding",
    "understood",
    "fantastic",
    "positive",
    "wealthy",
    "healthy",
    "dog",
    "cat",
    "cuteness",
    "pet",
    ]

neg = [
    "bad",
    "terrible",
    "none",
    "no",
    "negative",
    "worst",
    "unlikely",
    "uncapable",
    "sick",
    "tired",
    "unhealthy",
    "poor",
    "broke",
    "horrible",
    "left",
    "hate",
    "hateful",
    "hated",
    "hatred",
    "ungrateful",
    "traffic",
    "stuck",
    "unhabitable",
    "dread",
    "anger",
    "sad",
    "frustration",
    "unhappy",
    "unhappiness",
    "frown",
    "upside-down",
    "tippy",
    "agony",
    "agonizing",
    "pig",
    "wolf",
    "hungry",
    ]

neut = [
    "okay",
    "neutral",
    "manageable",
    "fine",
    "alright",
    "ok",
    "kay",
    "good-ish",
    ]

neut_ascii = [
    "(okay)",
    "(neutral)",
    "(manageable)",
    "(fine)",
    "(alright)",
    "(ok)",
    "(kay)",
    "(good-ish)",
    ]

ascii_list = [
    # 0 - 15
    '[NULL]', '[SOH]', '[STX]', '[ETX]', '[EOT]', '[ENQ]', '[ACK]', '[BELL]', 
    '[BACKSPACE]', '[TAB]', '[LINEFEED]', '[VTAB]', '[FORMFEED]', '[CR]', '[SO]', '[SI]',
    
    # 16 - 31
    '[DLE]', '[DC1]', '[DC2]', '[DC3]', '[DC4]', '[NAK]', '[SYN]', '[ETB]', 
    '[CAN]', '[EM]', '[SUB]', '[ESCAPE]', '[FS]', '[GS]', '[RS]', '[US]',
    
    # 32 - 47
    ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    
    # 48 - 63
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?',
    
    # 64 - 79
    '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    
    # 80 - 95
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_',
    
    # 96 - 111
    '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    
    # 112 - 122
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

fin = ["finished", "final", "finale", "end", "ending", "ended", "finally"]

cells = {}

def error(err):
    print(f"Something went wrong: {err}")

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def run(code, loop=False, date=""):
    global pos, neg, neut, fin, cell
    output = ""
    lines = code.split("\n")
    if not loop:
        date = lines[0].split("/")
    entry = " ".join(lines).replace("".join(lines[0]), "").split(" ")
    count = 0
    if len(date) != 3:
        error("I can't really imagine a date that doesn't have exactly 3 parameters, can you?")
        return output
    else:
        try:
            cell = int(date[0])
        except:
            error("Did they not teach you at school how to write!?")
            return output
        try:
            op = int(date[1])
        except:
            error("Why would you put something OTHER than a number for a month? Why?")
            return output
        try:
            base_val = int(date[2])
        except Exception as e:
            error("A non-integer for a year... What drove you to do this?")
            return output
        if cell > 31:
            error("Not a single month has more than 31 days. WHAT IS WRONG WITH YOU!?")
            return output
        if op > 12:
            error("Months don't go above 12, idiot.")
            return output
        if cell in cells:
            count = cells[cell]
        else:
            count = base_val
    for idx, i in enumerate(entry):
        iC = i.replace("!", "").replace("?", "").replace(",", "").replace(".", "").replace(":", "").replace(";", "").replace("\"", "").replace("'", "")
        if iC in pos:
            count +=1
        if iC in neg:
            count -=1
        if iC in ["same", "identical", "similar", "equal"] and entry[idx + 1] in ["as", "to"]:
            try:
                count = cells[int(entry[idx + 2].replace(".", ""))]
                cells[cell] = count
            except:
                error("That day didn't happen yet. What are you trying to say?")
                break
        if iC == "again" and not loop:
            try:
                if entry[idx + 1] in ["at", "to"]:
                    H = int(entry[idx + 2].strip().split(":")[0])
                    M = int(entry[idx + 2].strip().split(":")[1])
                    if is_prime(H) and H % 2 == 0:
                        opT = "!="
                        stment = cells[cell] != M
                    elif is_prime(H) and not H % 2 == 0:
                        opT = "="
                        stment = cells[cell] == M
                    elif not is_prime(H) and H % 2 == 0:
                        opT = ">"
                        stment = cells[cell] > M
                    elif not is_prime(H) and not H % 2 == 0:
                        opT = "<"
                        stment = cells[cell] < M
                    else:
                        error("What are you doing at this point... How did you even manage to get here?")
                        break
                else:
                    opT = "!="
                    stment = cells[cell] != 0
                while stment:
                    if opT == "!=":
                        stment = cells[cell] != M
                    elif opT == "=":
                        stment = cells[cell] == M
                    elif opT == ">":
                        stment = cells[cell] > M
                    elif opT == "<":
                        stment = cells[cell] < M
                    if cells[cell] <= -100:
                        error("Why are you so depressed? I'm calling a therapist for you.")
                        break
                    if cells[cell] >= 100:
                        error("Okay, we get it. You're happy. Stop it before you hurt yourself.")
                        break
                    run("".join(code.split(i)[1]).strip(), True, date)
            except:
                error("Did you really think that would work?")
                break
        if iC in ["remember", "remembers", "remembering", "remembered"]:
            in_count = input(">").strip()
            if not in_count == "":
                try:
                    count += int(in_count)
                except:
                    error("Give a number next time, bozo.")
                    break
            else:
                error("You really decided to give the silent treatment? Really?")
                break
        if i.count("!") != 0 or i.count("?") != 0:
            if not op % 2 == 0:
                count +=1
            else:
                count -=1
        cells[cell] = count
        if iC in neut:
            print(cells[cell])
        elif iC in neut_ascii:
            try:
                if 32 <= cells[cell]:
                    print(ascii_list[cells[cell]])
                else:
                    error("Nice ASCII character you got there. Very invisible.")
                    break
            except Exception as e:
                error("I'm struggling to understand how you can try to print an ASCII character that doesn't exist.")
                break
        if iC in fin:
            run("".join(code.split(i)[1]).strip())
            break

    return output

file = input("Execute file: ")
if not file.endswith(".txt"):
    file = f"{file}.txt"
try:
    with open(file, "r") as f:
        code = str(f.read()).lower()
    print(run(code))
except Exception as e:
    print(f"Cannot find path: {file}")
    print(f"Returned: {e}")
    
input("Press enter to continue...")
