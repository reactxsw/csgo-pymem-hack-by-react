import colorama, time, os, pymem, keyboard , re ,pymem.process , socket , subprocess ,math ,requests ,ctypes , psutil , urllib, configparser ,os , sys
from os import system
from math import sqrt , pi ,atan
from pypresence import Presence
from pathlib import Path
from colorama import Fore, init, Back, Style

#colour
CEND      = '\33[0m'
CGREEN2  = '\33[92m'
CBLUE   = '\33[34m'
CRED    = '\33[31m'
CYELLOW = '\33[33m'

current_machine_id = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()

os.system("title Unrealskill")
#hash-changer ทําให้ไฟล์ดูเเตกต่างควรเปลี่ยนบ่อยๆ เพื่อที่จะ undetect

def Spinner():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write('\r' + Style.BRIGHT + Fore.YELLOW + Back.BLACK +'[UNREAL] Loading... '+i)
		sys.stdout.flush()
		time.sleep(0.2)

def write_default_settings():
    global name
    name = input("USERNAME : ")

    with open("SETTING.ini", "w") as file:
        file.writelines(
            [
                "[DEFAULT]\n",
                "\n",
                f"usn = " + name + "\n",
                " \n",
                "tb = X\n",
                " \n",
                "ab = ALT\n",
                " \n",
                "wh = F1\n",
                " \n",
                "rh = F2\n",
                " \n",
                "nf = F4\n",
                "\n",
                "tpp = F6\n",
                "\n",
                "rcs = C\n",
                "\n",
                "abfov = 4\n",
                "\n",
                "rpc = True\n"
            ]
        )

def read_settings():
    if not Path("SETTING.ini").exists():
        write_default_settings()
    config = configparser.ConfigParser()
    config.read("SETTING.ini")
    return config["DEFAULT"]

settings = read_settings()

        
unreal = ("""
   __  __                      _______ __   _ ____
  / / / /___  ________  ____ _/ / ___// /__(_) / /
 / / / / __ \/ ___/ _ \/ __ `/ /\__ \/ //_/ / / / 
/ /_/ / / / / /  /  __/ /_/ / /___/ / ,< / / / /  
\____/_/ /_/_/   \___/\__,_/_//____/_/|_/_/_/_/ 
                                -By REACT#1120                                                   """)

logo = (CRED + unreal + CEND)

    
try:
    current_machine_id = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    r = requests.get('https://raw.githubusercontent.com/reactxsw/hwiddump/main/hwid.txt')
except:
    print(CBLUE + '[UNREAL] : Error : Internet connection' + CEND)
    b = input('')
    time.sleep(2)

def vacbypasser():

    dirname = os.path.dirname(os.path.abspath(__file__))
    vac = os.path.join(dirname, 'VAC.exe')
    subprocess.call(vac,shell=True)
    print(CGREEN2 + "[UNREAL] : VAC bypasser loaded" + CEND)

def check_for_vacbypasser():
    if Path("VAC.exe").exists():
        vacbypasser()
    
    else: 
        print(CBLUE + "[UNREAL] : VAC bypasser failed to load" + CEND)


def Authenticator():
    if not current_machine_id in r.text:
        check_for_vacbypasser()
        if len(sys.argv) < 2:  
            for char in logo:
                time.sleep(0.005)
                sys.stdout.write(char)
                sys.stdout.flush()
            time.sleep(0.01)
        Spinner()
        os.system("cls")
        print(CBLUE + '[UNREAL] : Error : HWID not in database' + CEND)
        print(CBLUE + '[UNREAL] : contact admin : REACT#1120 for permission' +CEND)
        print(CBLUE + f'[UNREAL] : Invalid HWID :' + current_machine_id + CEND)
        a = input('')
    else:
        Spinner()
        os.system("cls")
        print(CGREEN2 + "[UNREAL] : Permission granted !" + CEND)
        return True

Authenticator()

def Check_for_update():
    r = requests.get('https://raw.githubusercontent.com/reactxsw/csgo-pymem-hack-by-react/main/update.txt')
    if not "ygQkZhGgA7k495PDxvX7BRdsV3NenBeDr9fyU8ma4CccZWVAXpCEwyBERzF6HJUL43gVtAXmYKeSZJdSQNKZ4CRb4TkQbjtKDsHLpU6dYSbgfN767hQaRHFmyu2qaS6T" in r.text:
        print(CBLUE + "[UNREAL] : update found" + CEND)
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, 'There is an update available' , 'Update is found', 0)
    else:
        print(CGREEN2 + "[UNREAL] : Client is up to date" + CEND)

Check_for_update()

def check4process(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def gamecheck():

    if check4process('csgo.exe'):
        return True
    else:
        vacbypasser()
        print(CBLUE + '[UNREAL] : ERROR : CSGO is not running' + CEND)
        print(CBLUE + '[UNREAL] : make sure csgo.exe is running' + CEND)
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, 'CSGO is not running', 'No process found (csgo.exe)', 0)
        gc = input('')

gamecheck()

def afterbypass():
    if Path("VAC.exe").exists():
        print(CGREEN2 + "[UNREAL] : VACbypasser loaded" + CEND)
    else:
        print(CBLUE + "[UNREAL] : VAC bypasser failed to load" + CEND)

afterbypass()

def disrpc():
    rpc = Presence("764516498899206224")
    rpc.connect()
    rpc.update(state="Hacking",details="Join Unrealskill for an unrealskill", join="https://discord.gg/XeTzykXvkcGtsHFES6z3F" ,large_image="rpcphoto",small_image="thai" ,start=time.time())    

os.system('color 08')
r = requests.get("https://raw.githubusercontent.com/reactxsw/hwiddump/main/csgo.h")
r = r.text

offsets = ["dwEntityList", "dwLocalPlayer","m_flFlashMaxAlpha", "m_iTeamNum", "dwGlowObjectManager", "m_iGlowIndex", "dwForceJump", "m_fFlags", "dwForceAttack", "m_iCrosshairId", "m_bSpotted", "m_iShotsFired", "m_aimPunchAngle", "dwClientState", "dwClientState_ViewAngles","m_iObserverMode","m_bIsDefusing","m_bGunGameImmunity","m_iHealth","m_dwBoneMatrix","m_vecOrigin","m_vecViewOffset","m_bDormant","dwbSendPackets","dwInput","clientstate_last_outgoing_command","clientstate_net_channel"]

d = {}
offs = []
for i in range(len(offsets)):
    if offsets[i] in r:
        search = re.findall(str(offsets[i]) + '\s'"= (.*);", r)
        offs += search

i = 0
while i <= len(offsets)-1:
    (key, val) = offsets[i], offs[i]
    d[key] = val
    i += 1

dwEntityList = int(d["dwEntityList"], base = 16)
dwLocalPlayer = int(d["dwLocalPlayer"], base = 16)
m_flFlashMaxAlpha = int(d["m_flFlashMaxAlpha"], base = 16)
m_iTeamNum = int(d["m_iTeamNum"], base = 16)
dwGlowObjectManager = int(d["dwGlowObjectManager"], base = 16)
m_iGlowIndex = int(d["m_iGlowIndex"], base = 16)
dwForceJump = int(d["dwForceJump"], base = 16)
m_fFlags = int(d["m_fFlags"], base = 16)
dwForceAttack = int(d["dwForceAttack"], base = 16)
m_iCrosshairId = int(d["m_iCrosshairId"], base = 16)
m_bSpotted = int(d["m_bSpotted"], base = 16)
m_iShotsFired = int(d["m_iShotsFired"], base = 16)
m_aimPunchAngle = int(d["m_aimPunchAngle"], base = 16)
dwClientState = int(d["dwClientState"], base = 16)
dwClientState_ViewAngles = int(d["dwClientState_ViewAngles"], base = 16)
m_iObserverMode = int(d["m_iObserverMode"], base = 16)
m_bIsDefusing = int(d["m_bIsDefusing"], base = 16)
m_iHealth = int(d["m_iHealth"], base = 16)
m_bGunGameImmunity = int(d["m_bGunGameImmunity"], base = 16)
m_iDefaultFOV = (0x332C)
m_totalHitsOnServer = (0xA3A8) 
m_dwBoneMatrix = int(d["m_dwBoneMatrix"], base = 16)
m_vecOrigin = int(d["m_vecOrigin"], base = 16)
m_vecViewOffset = int(d["m_vecViewOffset"], base = 16)
m_bDormant = int(d["m_bDormant"], base = 16)
dwbSendPackets = int(d["dwbSendPackets"], base = 16)
dwInput = int(d["dwInput"], base = 16)
clientstate_last_outgoing_command = int(d["clientstate_last_outgoing_command"], base = 16)
clientstate_net_channel = int(d["clientstate_net_channel"], base = 16)


pm = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll

def normalizeAngles(viewAngleX, viewAngleY):
    if viewAngleX > 89:
        viewAngleX -= 360
    if viewAngleX < -89:
        viewAngleX += 360
    if viewAngleY > 180:
        viewAngleY -= 360
    if viewAngleY < -180:
        viewAngleY += 360
    return viewAngleX, viewAngleY

def checkangles(x, y):
    if x > 89:
        return False
    elif x < -89:
        return False
    elif y > 360:
        return False
    elif y < -360:
        return False
    else:
        return True

def nanchecker(first, second):
    if math.isnan(first) or math.isnan(second):
        return False
    else:
        return True

def calc_distance(current_x, current_y, new_x, new_y):
    distancex = new_x - current_x
    if distancex < -89:
        distancex += 360
    elif distancex > 89:
        distancex -= 360
    if distancex < 0.0:
        distancex = -distancex
    distancey = new_y - current_y
    if distancey < -180:
        distancey += 360
    elif distancey > 180:
        distancey -= 360
    if distancey < 0.0:
        distancey = -distancey
    return distancex, distancey

def calcangle(localpos1, localpos2, localpos3, enemypos1, enemypos2, enemypos3):
    try:
        delta_x = localpos1 - enemypos1
        delta_y = localpos2 - enemypos2
        delta_z = localpos3 - enemypos3
        hyp = sqrt(delta_x * delta_x + delta_y * delta_y + delta_z * delta_z)
        x = atan(delta_z / hyp) * 180 / pi
        y = atan(delta_y / delta_x) * 180 / pi
        if delta_x >= 0.0:
            y += 180.0
        return x, y
    except:
        pass        

#function ต่างๆของ hackอยู่ใน main(): 

def main():
    Spinner()
    os.system("cls")
    try:
        Username = settings["usn"]
        Triggerbot = settings["tb"]
        Radarhack = settings["rh"]
        Aimbot = settings["ab"]
        Wallhack = settings["wh"]
        Noflash = settings["nf"]
        Thirdperson = settings["tpp"]
        RecoilScript = settings["rcs"]
        Aimbotfov = settings["abfov"]
        discordrpc = settings["rpc"]
        Discordrichpresence = bool(discordrpc)
        aimfov = int(Aimbotfov)
        
    except:
        print(CBLUE + "[UNREAL] : config failed to load." + CEND)
        print(CBLUE + "[UNREAL] : Delete SETTING.ini to reinstall config" + CEND)
    
    if Discordrichpresence == True:
        disrpc()
        drpc = "ON"
    
    else:
        return True
        drpc = "OFF"
    
    print(logo)
    print(Style.BRIGHT + f" Login as " + Username + " | Smilewin")
    print(Style.BRIGHT + "===================================")
    print(Style.BRIGHT + " Triggerbot     | "+ Triggerbot + " (Hold)")
    print(Style.BRIGHT + " Aimbot         | "+ Aimbot + " (Hold)")
    print(Style.BRIGHT + " Bunnyhop       | 'SPACEBAR' (Hold)")   
    print(Style.BRIGHT + " Wallhack       | "+ Wallhack + " (Toggle)")
    print(Style.BRIGHT + " Radarhack      | "+ Radarhack + " (Toggle)")
    print(Style.BRIGHT + " No flash       | "+ Noflash + " (Toggle")
    print(Style.BRIGHT + " Thirdperson    | "+ Thirdperson + " (Toggle)") 
    print(Style.BRIGHT + " RCS            | "+ RecoilScript + " (Toggle)")
    print(Style.BRIGHT + " Off hack       | 'End' (Press)")
    print(Style.BRIGHT + " aimbotfov = " + Aimbotfov + "  |" ) 
    print(Style.BRIGHT + " Discord RPC = " + drpc)
    print(Style.BRIGHT + "===================================")
    print(Style.BRIGHT + f'IP : ' + socket.gethostbyname(socket.gethostname()))  
    print(Style.BRIGHT + f'HWID : ' + current_machine_id)
    
    EnableGlowESP = False #เปิดปิด wallhack
    Enablethird = False #เปิดปิด third person
    switch = 0 # flashbang
    EnableRCS = False#เปิดปิด rcs
    Enableradar = False
    oldpunchx = 0.0
    oldpunchy = 0.0
    while True:
        if keyboard.is_pressed("end"):
            print(CBLUE + "[UNREAL] : Closing...")
            time.sleep(1)
            exit()
        # ทําทุกอย่างให้พร้อม เช่นอ่านค่าต่างๆ เเละบวกค่า
        #reduce rpm/wpm     
        localPlayer = pm.read_int(client + dwLocalPlayer)
        player = pm.read_int(client + dwLocalPlayer)
        engine_pointer = pm.read_int(engine + dwClientState)
        Localteam = pm.read_int(player + m_iTeamNum)
        crosshairID = pm.read_int(localPlayer + m_iCrosshairId) 
        flash_value = localPlayer + m_flFlashMaxAlpha
        getTeam = pm.read_int(client + dwEntityList + (crosshairID-1)* 0x10)
        crosshairTeam = pm.read_int(getTeam + m_iTeamNum)

        time.sleep(0.01)
        if keyboard.is_pressed(RecoilScript):
            EnableRCS = not EnableRCS
            time.sleep(0.2)
            
        if EnableRCS is True: 
            if pm.read_int(localPlayer + m_iShotsFired) > 2:
                rcs_x = pm.read_float(engine_pointer + dwClientState_ViewAngles)
                rcs_y = pm.read_float(engine_pointer + dwClientState_ViewAngles + 0x4)
                punchx = pm.read_float(localPlayer + m_aimPunchAngle)
                punchy = pm.read_float(localPlayer + m_aimPunchAngle + 0x4)
                newrcsx = rcs_x - (punchx - oldpunchx) * 2
                newrcsy = rcs_y - (punchy - oldpunchy) * 2
                newrcs, newrcy = normalizeAngles(newrcsx, newrcsy)
                oldpunchx = punchx
                oldpunchy = punchy
                if nanchecker(newrcsx, newrcsy) and checkangles(newrcsx, newrcsy):
                    pm.write_float(engine_pointer + dwClientState_ViewAngles, newrcsx)
                    pm.write_float(engine_pointer + dwClientState_ViewAngles + 0x4, newrcsy)
            else:
                oldpunchx = 0.0
                oldpunchy = 0.0
                newrcsx = 0.0
                newrcsy = 0.0
          
        target = None
        olddistx = 111111111111
        olddisty = 111111111111
        for i in range(1,32):
            entity = pm.read_int(client + dwEntityList + i * 0x10)
            if entity:
                try:
                    entity_team_id = pm.read_int(entity + m_iTeamNum)
                    entity_hp = pm.read_int(entity + m_iHealth)
                    entity_dormant = pm.read_int(entity + m_bDormant)
                except:
                    print(CBLUE + "[UNREAL] : Can't load player info" + CEND)
                if Localteam != entity_team_id and entity_hp > 0:
                    entity_bones = pm.read_int(entity + m_dwBoneMatrix)
                    localpos_x_angles = pm.read_float(engine_pointer + dwClientState_ViewAngles)
                    localpos_y_angles = pm.read_float(engine_pointer + dwClientState_ViewAngles + 0x4)
                    localpos1 = pm.read_float(player + m_vecOrigin)
                    localpos2 = pm.read_float(player + m_vecOrigin + 4)
                    localpos_z_angles = pm.read_float(player + m_vecViewOffset + 0x8)
                    localpos3 = pm.read_float(player + m_vecOrigin + 8) + localpos_z_angles
                    try:
                        entitypos_x = pm.read_float(entity_bones + 0x30 * 8 + 0xC)
                        entitypos_y = pm.read_float(entity_bones + 0x30 * 8 + 0x1C)
                        entitypos_z = pm.read_float(entity_bones + 0x30 * 8 + 0x2C)
                    except:
                        continue
                    X, Y = calcangle(localpos1, localpos2, localpos3, entitypos_x, entitypos_y, entitypos_z)
                    newdist_x, newdist_y = calc_distance(localpos_x_angles, localpos_y_angles, X, Y)
                    if newdist_x < olddistx and newdist_y < olddisty and newdist_x <= aimfov and newdist_y <= aimfov:
                        olddistx, olddisty = newdist_x, newdist_y
                        target, target_hp, target_dormant = entity, entity_hp, entity_dormant
                        target_x, target_y, target_z = entitypos_x, entitypos_y, entitypos_z
                if keyboard.is_pressed(Aimbot) and player:
                        if target and target_hp > 0 and not target_dormant:
                            x, y = calcangle(localpos1, localpos2, localpos3, target_x, target_y, target_z)
                            normalize_x, normalize_y = normalizeAngles(x, y)
                            pm.write_float(engine_pointer + dwClientState_ViewAngles, normalize_x)
                            pm.write_float(engine_pointer + dwClientState_ViewAngles + 0x4, normalize_y)
                
                if keyboard.is_pressed(Radarhack):
                    Enableradar = not Enableradar
                    time.sleep(0.2)

                if Enableradar == True:
                    pm.write_int(entity + m_bSpotted, 1)   
        
        if keyboard.is_pressed(Wallhack):
            EnableGlowESP = not EnableGlowESP
            time.sleep(0.2)         
        
        glow_manager = pm.read_int(client + dwGlowObjectManager)
        for i in range(1,32):
            entity = pm.read_int(client + dwEntityList + i *0x10)
            if EnableGlowESP and entity:
                entity_team_id = pm.read_int(entity + m_iTeamNum)
                entity_glow = pm.read_int(entity + m_iGlowIndex)
                if entity_team_id == 2: #โจร glow
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(1))#R
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))#G
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))#B
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1))#alpha
                    pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1) 
                elif entity_team_id == 3: #ตํารวจ ct glow
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(0))#R
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))#G
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(1))#B
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1))#alpha
                    pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)
                   
        if keyboard.is_pressed("space"):
            force_jump = client + dwForceJump
            on_ground = pm.read_int(player + m_fFlags)
        
            if player and on_ground and on_ground == 257:
                pm.write_int(force_jump, 5)
                time.sleep(0.08)
                pm.write_int(force_jump, 4) 
       
        if keyboard.is_pressed(Noflash) and switch == 0:
            pm.write_float(flash_value, float(0))
            switch = 1
            time.sleep(0.2)
        elif keyboard.is_pressed(Noflash) and switch == 1:
            pm.write_float(flash_value, float(255))
            switch = 0
            time.sleep(0.2)

        if keyboard.is_pressed(Triggerbot) and switch == 0:
            if crosshairID>0 and crosshairID<32 and Localteam != crosshairTeam:
                pm.write_int(client + dwForceAttack,6)
        if keyboard.is_pressed(Triggerbot) and switch == 1:
            if crosshairID>0 and crosshairID<32 and Localteam != crosshairTeam:
                pm.write_int(client + dwForceAttack,6)         
        
        if keyboard.is_pressed(Thirdperson):
            Enablethird = not Enablethird
            time.sleep(0.5)
            if Enablethird:
                pm.write_int(localPlayer + m_iObserverMode,1)
            else:
                pm.write_int(localPlayer + m_iObserverMode,0)

#เเก้บัค
def function():
    os.system("cls")
    while True:                                                     
        time.sleep(3)
        try:
            try:
                os.system("cls")
                main()
            finally:
                main()
        except:
            os.system("cls")
            if len(sys.argv) < 2:
 
                for char in logo:
                    time.sleep(0.0075)
                    sys.stdout.write(char)
                    sys.stdout.flush()
                time.sleep(0.5)
            print("")
            print("")
            print(CBLUE + "[UNREAL] : The Cheat failed to load / in- lobby" + CEND)
            print(CBLUE + "[UNREAL] : Retrying..." + CEND)

if __name__ == '__main__':
    function()
 


 
    

    







