import colorama, time, os, pymem, keyboard , re ,pymem.process , socket , subprocess ,math ,requests ,ctypes , psutil , urllib 
from os import system
from math import sqrt , pi ,atan
from pypresence import Presence
import tkinter as tk
from tkinter import Tk, ttk
from tkinter.ttk import *
from PIL import ImageTk, Image
from threading import Thread

#colour
CEND      = '\33[0m'
CRED    = '\33[31m'
current_machine_id = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()

root = Tk()

unreal = """
    __  __                      _______ __   _ ____
  / / / /___  ________  ____ _/ / ___// /__(_) / /
 / / / / __ \/ ___/ _ \/ __ `/ /\__ \/ //_/ / / / 
/ /_/ / / / / /  /  __/ /_/ / /___/ / ,< / / / /  
\____/_/ /_/_/   \___/\__,_/_//____/_/|_/_/_/_/                                                    
"""

def GUI():
    style = ttk.Style()
    style.configure('Style.TButton', font='TkFixedFont')
    root.geometry("400x325")
    root.title("UnrealSkillz")


    root.iconbitmap("C://Users//FIN//Documents//python//react_bot//discord bot//rpcphoto.ico")
    image = ImageTk.PhotoImage(Image.open("E:/unrealskilllogo.png"))

    myLabel1 = Label(root, text="made by React")
    myLabel2 = Label(image=image)
    myLabel3 = Label(root, text=f"Login as React    | Smilewin")
    myLabel4 = Label(root, text="================================")
    myLabel5 = Label(root, text=" Triggerbot     | 'X' (Hold)")
    myLabel6 = Label(root, text=" Aimbot         | 'ALT' (Hold)")
    myLabel7 = Label(root, text=" Bunnyhop       | 'SPACEBAR' (Hold)")
    myLabel8 = Label(root, text=" Wallhack       | 'F1' (Toggle)")
    myLabel9 = Label(root, text=" Thirdperson    | 'F6' (Toggle)")
    myLabel10 = Label(root, text=" RCS            | 'C' (Toggle)")
    myLabel11 = Label(root, text=" Off hack       | 'End' (Press)")
    myLabel12 = Label(root, text="================================")
    myLabel13 = Label(root, text=f'IP : ' + socket.gethostbyname(socket.gethostname()))
    myLabel14 = Label(root, text=f'HWID : ' + current_machine_id)

    myLabel1.grid(row=0, column=0)
    myLabel2.grid(row=1, column=0)
    myLabel3.grid(row=2, column=0)
    myLabel4.grid(row=3, column=0)
    myLabel5.grid(row=4, column=0)
    myLabel6.grid(row=5, column=0)
    myLabel7.grid(row=6, column=0)
    myLabel8.grid(row=7, column=0)
    myLabel9.grid(row=8, column=0)
    myLabel10.grid(row=9, column=0)
    myLabel11.grid(row=10, column=0)
    myLabel12.grid(row=11, column=0)
    myLabel13.grid(row=12, column=0)
    myLabel14.grid(row=13, column=0)

    myLabel1.place(relx= 0.0, rely=1.0, anchor="e")

    root.mainloop()
    

unreal = ("""
   __  __                      _______ __   _ ____
  / / / /___  ________  ____ _/ / ___// /__(_) / /
 / / / / __ \/ ___/ _ \/ __ `/ /\__ \/ //_/ / / / 
/ /_/ / / / / /  /  __/ /_/ / /___/ / ,< / / / /  
\____/_/ /_/_/   \___/\__,_/_//____/_/|_/_/_/_/                                                    
""")

def menu():
    print("Login as member | Smilewin")
    print("================================")
    print(" Triggerbot     | 'X' (Hold)")
    print(" Aimbot         | 'ALT' (Hold)")
    print(" Bunnyhop       | 'SPACEBAR' (Hold)")   
    print(" Wallhack       | 'F1' (Toggle)")
    print(" Radar          | 'F2' (Toggle)")
    print(" No flash       | 'F4' (Toggle)")
    print(" Thirdperson    | 'F6' (Toggle)") 
    print(" RCS            | 'C' (Toggle)")
    print(" Off hack       | 'End' (Press)")
    print("================================")
    print(f'IP : ' + socket.gethostbyname(socket.gethostname()))  
    print(f'HWID : ' + current_machine_id)

logo = (CRED + unreal + CEND)

def downloadvacbypasser():
    vacbypassurl = 'https://cdn-33.anonfiles.com/P0mcY6hdpc/9bff18b9-1603279833/VAC.exe'
    print(vacbypassurl)
    print('working on this function')

try:
    current_machine_id = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    r = requests.get('https://raw.githubusercontent.com/reactxsw/hwiddump/main/hwid.txt')
except:
    print('Error : Internet connection')
    b = input('')
    time.sleep(2)

def vacbypasser():
    dirname = os.path.dirname(os.path.abspath(__file__))
    vac = os.path.join(dirname, 'VAC.exe')
    subprocess.call(vac,shell=True)
    print("VAC bypasser loaded")

def Authenticator():
    if not current_machine_id in r.text:
        vacbypasser()
        print("VAC bypasser loaded")
        print('Error : HWID not in database')
        print(f'Invalid HWID :' + current_machine_id)
        a = input('')
        time.sleep(5)
        exit()
    else:
        print("Permission granted !")
        return True

Authenticator()

def check4process(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

def gamecheck():
    if check4process('csgo.exe'):
        return True
    else:
        vacbypasser()
        print('ERROR : CSGO is not running')
        print('make sure csgo.exe is running')
        gc = input('')

gamecheck()

def afterbypass():
    print("VACbypasser loaded")

afterbypass()

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
m_iDefaultFOV = (0x332C) # Welp not on Hazedumper (Special Offset)
m_totalHitsOnServer = (0xA3A8) # Welp not on Hazedumper (Special Offset)
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

#aimbot angle ยิ่งน้อยยิ่งเนียน 120 = ที่เห็นข้างหน้า 360 = รอบตัว
aimfov = 4

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

def main():
    EnableGlowESP = False #เปิดปิด wallhack
    Enablethird = False #เปิดปิด third person
    switch = 0 # flashbang
    EnableRCS = False#เปิดปิด rcs
    Enableradar = False#เปิดปิด radar
    os.system("cls")
    print(logo)
    menu()
    global amount
    oldpunchx = 0.0
    oldpunchy = 0.0
    while True:
        time.sleep(0.01)

        if keyboard.is_pressed("C"):
            EnableRCS = not EnableRCS
            time.sleep(0.2)
            
        if EnableRCS is True: 
            rcslocalplayer = pm.read_int(client + dwLocalPlayer)
            rcsengine = pm.read_int(engine + dwClientState)
            if pm.read_int(rcslocalplayer + m_iShotsFired) > 2:
                rcs_x = pm.read_float(rcsengine + dwClientState_ViewAngles)
                rcs_y = pm.read_float(rcsengine + dwClientState_ViewAngles + 0x4)
                punchx = pm.read_float(rcslocalplayer + m_aimPunchAngle)
                punchy = pm.read_float(rcslocalplayer + m_aimPunchAngle + 0x4)
                newrcsx = rcs_x - (punchx - oldpunchx) * 2
                newrcsy = rcs_y - (punchy - oldpunchy) * 2
                newrcs, newrcy = normalizeAngles(newrcsx, newrcsy)
                oldpunchx = punchx
                oldpunchy = punchy
                if nanchecker(newrcsx, newrcsy) and checkangles(newrcsx, newrcsy):
                    pm.write_float(rcsengine + dwClientState_ViewAngles, newrcsx)
                    pm.write_float(rcsengine + dwClientState_ViewAngles + 0x4, newrcsy)
            else:
                oldpunchx = 0.0
                oldpunchy = 0.0
                newrcsx = 0.0
                newrcsy = 0.0
        localPlayer = pm.read_int(client + dwLocalPlayer)
        player = pm.read_int(client + dwLocalPlayer)
        engine_pointer = pm.read_int(engine + dwClientState)
        Localteam = pm.read_int(player + m_iTeamNum)
        crosshairID = pm.read_int(localPlayer + m_iCrosshairId) 
        flash_value = localPlayer + m_flFlashMaxAlpha
        getTeam = pm.read_int(client + dwEntityList + (crosshairID-1)* 0x10)
        crosshairTeam = pm.read_int(getTeam + m_iTeamNum)
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
                    print("Can't load player info")
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
                if keyboard.is_pressed("alt") and player:
                        if target and target_hp > 0 and not target_dormant:
                            x, y = calcangle(localpos1, localpos2, localpos3, target_x, target_y, target_z)
                            normalize_x, normalize_y = normalizeAngles(x, y)
                            pm.write_float(engine_pointer + dwClientState_ViewAngles, normalize_x)
                            pm.write_float(engine_pointer + dwClientState_ViewAngles + 0x4, normalize_y)   
        
        if keyboard.is_pressed("F1"):
            EnableGlowESP = not EnableGlowESP
            time.sleep(0.2)         
        
        glow_manager = pm.read_int(client + dwGlowObjectManager)
        for i in range(1,32):
            entity = pm.read_int(client + dwEntityList + i *0x10)
            if EnableGlowESP and entity:
                entity_team_id = pm.read_int(entity + m_iTeamNum)
                entity_glow = pm.read_int(entity + m_iGlowIndex)
                if entity_team_id == 2: #โจร glow
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(1)) 
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0)) 
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0)) 
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1)) 
                    pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1) 
                elif entity_team_id == 3: #ตํารวจ ct glow
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(0)) 
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0)) 
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(1)) 
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1)) 
                    pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)
             
        if keyboard.is_pressed("F2"):
            Enableradar = not Enableradar
            time.sleep(0.5)
            if Enablethird:
                pm.write_int(entity + m_bSpotted, 1)
            else:
                pm.write_int(entity + m_bSpotted, 0)
        
        if keyboard.is_pressed("space"):
            force_jump = client + dwForceJump
            on_ground = pm.read_int(player + m_fFlags)
        
            if player and on_ground and on_ground == 257:
                pm.write_int(force_jump, 5)
                time.sleep(0.08)
                pm.write_int(force_jump, 4) 
       
        if keyboard.is_pressed("F4") and switch == 0:
            pm.write_float(flash_value, float(0))
            switch = 1
            time.sleep(0.2)
        elif keyboard.is_pressed("F4") and switch == 1:
            pm.write_float(flash_value, float(255))
            switch = 0
            time.sleep(0.2)

        if keyboard.is_pressed("X") and switch == 0:
            if crosshairID>0 and crosshairID<32 and Localteam != crosshairTeam:
                pm.write_int(client + dwForceAttack,6)
        if keyboard.is_pressed("x") and switch == 1:
            if crosshairID>0 and crosshairID<32 and Localteam != crosshairTeam:
                pm.write_int(client + dwForceAttack,6)         
        
        if keyboard.is_pressed("F6"):
            Enablethird = not Enablethird
            time.sleep(0.5)
            if Enablethird:
                pm.write_int(localPlayer + m_iObserverMode,1)
            else:
                pm.write_int(localPlayer + m_iObserverMode,0) 
                       
        if keyboard.is_pressed("end"):
            exit(0) 
 
         
if __name__ == '__main__':
    main()
 
    

    







