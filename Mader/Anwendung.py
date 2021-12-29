import numpy as np
import matplotlib.pyplot as plt
import shapely.geometry as sha
from tkinter import *


def plotLactate(VO2max, VLamax, RunningEco, Ks, Kss, VolRel):
    # Generate oxygen steady-states
    VO2ss = np.arange(1, VO2max, 0.01)

    # potentiate constants
    Ks = Ks ** 2
    Kss = Kss ** 3

    # calculate ADP corresponding to VO2ss (eq. 4b)
    ADP = np.sqrt((Ks * VO2ss) / (VO2max - VO2ss))

    # calculate steady state gross lactic acid (pyruvate) formation rate (eq. 3)
    dladtss = 60 * VLamax / (1 + (Kss / ADP ** 3))

    # calculate lactate combustion (eq. 6)
    La_comb = (0.01576 / VolRel) * VO2ss

    # calculate net lactate formation
    dladtnet = abs(dladtss - La_comb)

    # calculate the crossing point between gross lactate production and combustion
    line_1 = sha.LineString(np.column_stack((dladtss, VO2ss)))
    line_2 = sha.LineString(np.column_stack((La_comb, VO2ss)))
    intersection = line_1.intersection(line_2)

    # speed at anaerobic threshold
    sAT = intersection.y / RunningEco

    # percentage of VO2max
    pcVO2maxAT = intersection.y / VO2max

    # print to console
    #print(f'AT is at {round(sAT, 2)} m/s, {round(pcVO2maxAT * 100, 1)}% of VO2max')

    # convert VO2ss into velocity (m/s)
    v = VO2ss / RunningEco

    # plot all lactate curves
    fig, ax = plt.subplots()
    plt.plot(v, dladtnet, color='green')
    plt.plot(v, dladtss, color='red')
    plt.plot(v, La_comb, color='blue')

    plt.legend(['Lack of Pyruvate + Lactate acummulation',
                'Gross Lactate Formation',
                'Potential Lactate Removal'])

    # set limits for interactive visualisation
    plt.ylim(0, 8)
    plt.xlim(0, 6)

    ## highlight the crossing point in red
    # plt.plot(round(intersection.y,1),round(intersection.x,1), 'ro')
    # plt.plot(intersection.y,intersection.x, 'ro')

    # vertical line at AT

    plt.axvline(x=sAT, linestyle='dotted', color='black')
    ax.set_xlabel('speed in [m/s]')
    ax.set_ylabel('mmol/l/min')
    plt.legend(['Lack of Pyruvate + Lactate acummulation',
                'Gross Lactate Formation',
                'Potential Lactate Removal', 'AT'])
    plt.title(f'AT is at {round(sAT, 2)} m/s, {round(pcVO2maxAT * 100, 1)}% of VO2max')
    plt.show()

def plotClass(VO2max, VLamax, Running_Eco, Ks, Kss, VolRel, Kel):
    Kel = Kel
    Kss = Kss ** 3
    Ks = Ks ** 2
    VO2max = float(VO2max)
    VLamax = float(VLamax)
    VolRel = float(VolRel)
    VO2ss = np.arange(1, VO2max, 0.01)
    A = Ks * VO2ss
    B = VO2max - VO2ss
    C = ((A / B) ** (1.5))
    laktat = VLamax * 60
    Class = np.sqrt((VLamax * Kel * 60) / (((0.01576 / VolRel) * VO2ss) * (1 + (Kss / ((Ks * VO2ss) / (VO2max - VO2ss)) ** (3 / 2))) - laktat))
    v = VO2ss / float(Running_Eco)
    plt.ylim(0, 10)
    plt.title('Lactate steady state concentration')
    plt.plot(v, Class)
    plt.show()

def timecurve(VO2max, VLamax, Running_Eco):
    def acceptLa0button():
        global La_0, Körpergewicht, Muskelmasse, Geschwindigkeit
        La_0 = float(z1.get())
        Körpergewicht = float(z3.get())
        Muskelmasse = float(z2.get())
        Geschwindigkeit = float(z4.get())
        root.destroy()
        return (La_0, Körpergewicht, Muskelmasse, Geschwindigkeit)
    root = Tk()
    root.title("Angaben")
    z1 = Entry(root)
    z1.grid(row=0, column=0, padx=100)
    z1.insert(0, "La_pre")
    z2 = Entry(root)
    z2.grid(row=1, column=0, padx=100)
    z2.insert(0, "Muskelmasse")
    z3 = Entry(root)
    z3.grid(row=2, column=0, padx=100)
    z3.insert(0, "Körpergewicht")
    z4 = Entry(root)
    z4.grid(row=3, column=0, padx=100)
    z4.insert(0, "Geschwindigkeit [m/s]")
    accept = Button(root, text="Show", command=acceptLa0button).grid()
    root.mainloop()

    Kss = 0.15 ** 3
    Kla02 = 0.01475
    VolRel = 0.75  # nicht 0.44 weil es im 1 Kompartment modell ist
    K_el_ox = 1.885 ** 2
    Ks = 0.035 ** 2
    La0 = La_0
    t_max = 30
    La_max = 20
    vlamax = (60 * VLamax * (Muskelmasse * 0.75 + 5)) / Muskelmasse
    VO2max = (VO2max * Körpergewicht) / Muskelmasse
    VO2sst = np.array([(Geschwindigkeit * Running_Eco) * Körpergewicht / Muskelmasse])
    La_t = np.arange(0, 20, 0.001)

    for VO2ss in VO2sst:
        T = np.array([])
        for La in La_t:
            VLaomax = 0.01475 * VO2ss
            b = VLaomax
            a = vlamax / (1 + Kss * (((VO2max - VO2ss) / (Ks * VO2ss)) ** 1.5))
            if a < b:
                C = (La - La0) * np.sqrt((b - a) / (a * K_el_ox)) / (1 - La * La0 * (b - a) / (a * K_el_ox))
                if abs(C) >= 1:
                    T = np.append(T, -1)
                else:
                    artanh = np.log((1 + C) / (1 - C)) / 2
                    TvonLa = (La - La0 - b * np.sqrt(K_el_ox / (a * (b - a))) * artanh) / (a - b)
                    T = np.append(T, TvonLa)
            else:
                C = (La - La0) * np.sqrt((a - b) / (a * K_el_ox)) / (1 + La * La0 * (a - b) / (a * K_el_ox))
                arctan = np.arctan(C)
                TvonLa = (La - La0 - b * np.sqrt(K_el_ox / (a * (a - b))) * arctan) / (a - b)
                T = np.append(T, TvonLa)
        plt.xlim(0, 30)
        plt.plot(T, La_t)
    plt.show()

def showbutton():
    global VO2max, Vlamax, Running_Eco, VolRel
    VO2max = g1.get()
    Vlamax = g2.get()
    Running_Eco = g3.get()
    VolRel = g4.get()
    root.destroy()
    return(VO2max, Vlamax, Running_Eco, VolRel)


a = 2
while a == 2:
    root = Tk()
    root.title("Setting Constants")
    g1 = Entry(root)
    g1.grid(row=0, column=0, padx=100)
    g1.insert(0, "VO2max")
    g2 = Entry(root)
    g2.grid(row=0, column=1, padx=100)
    g2.insert(0, "Vlamax")
    g3 = Entry(root)
    g3.grid(row=1, column=0, padx=100)
    g3.insert(0, "Running Economy")
    g4 = Entry(root)
    g4.grid(row=1, column=1, padx=100)
    g4.insert(0, "VolRel")
    Show = Button(root, text="Show", command=showbutton).grid()
    root.mainloop()

    root = Tk()
    root.geometry('300x280')
    root.title("Fahrrad oder Laufen?")


    def buttonAT():
        global auswahl
        auswahl = 1
        root.destroy()


    def buttonCLass():
        global auswahl
        auswahl = 2
        root.destroy()

    def buttonTime():
        global auswahl
        auswahl = 3
        root.destroy()
    buttontime = Button(root, text="Timecurve", command=buttonTime, padx=100, pady=30).grid()
    buttonclass = Button(root, text="CLass", command=buttonCLass, padx=100, pady=30).grid()
    buttonat = Button(root, text="AT", command=buttonAT, padx=100, pady=30).grid()
    root.mainloop()

    while auswahl == 1:
        plotLactate(float(VO2max), float(Vlamax), float(Running_Eco), 0.25, 1.2, float(VolRel))
        auswahl = 5
    while auswahl == 2:
        plotClass(float(VO2max), float(Vlamax), float(Running_Eco), 0.25, 1.2, float(VolRel), 9)
        auswahl = 5
    while auswahl == 3:
        timecurve(float(VO2max), float(Vlamax), float(Running_Eco))
        auswahl = 5

    a = 3
    root = Tk()
    def yesbutton():
        global a
        a = 2
        root.destroy()

    def nobutton():
        global a
        a = 3
        root.destroy()

    root.title('New Try?')
    root.geometry('300x200')
    yes = Button(root, text="Yes", command=yesbutton, padx=100, pady=30).grid()
    no = Button(root, text="No", command=nobutton, padx=100, pady=30).grid()
    root.mainloop()



