"""
This module contain FSM class.
"""

from prime import prime

class FSM:
    """
    This class represents finite-state machine.

    Attributes:
    -----------
        states:
            self.q1: sleep
            self.q2: eat
            self.q3: relax
            self.q4: work out
            self.q5: study
            self.q6: procrastinate
            self.q7: terminal state
            self.q0: initial state
        self.hours: int
        self.stopped: bool
            indicates when to go to the terminal state

    Methods:
    --------
    send(self, probability):
        The function sends the current input to the current state.
        It captures the StopIteration exception and marks the stopped flag.

    _create_start(self):
        initial state
        immediatly goes to sleep (q1) state

    _sleep(self):
        state of sleep

    _eat(self):
        to-eat state

    _relax(self):
        state of relax
    
    _work_out(self):
        work-out state

    _study(self):
        study state

    _procrastinate(self):
        procrastination state

    _finita_la_commedia(self):
        terminal state
    """
    def __init__(self):
        """
        Constructs all necessary attributes\
        for finite-state machine.

        Attributes:
        -----------
        states:
            self.q1: sleep
            self.q2: eat
            self.q3: relax
            self.q4: work out
            self.q5: study
            self.q6: procrastinate
            self.q7: terminal state
            self.q0: initial state
        self.hours: int
        self.stopped: bool
            indicates when to go to the terminal state
        """
        self.q1 = self._sleep()
        self.q2 = self._eat()
        self.q3 = self._relax()
        self.q4 = self._work_out()
        self.q5 = self._study()
        self.q6 = self._procrastinate()
        self.q7 = self._finita_la_commedia()
        self.q0 = self._create_start()
        self.hours = 0
        self.stopped = False

    def send(self, probability):
        """
        The function sends the current input to the current state.
        It captures the StopIteration exception and marks the stopped flag.
        """
        try:
            self.current_state.send(probability)
        except StopIteration:
            self.stopped = True

    def _create_start(self):
        """
        Initial state.
        Immediatly goes to sleep (q1) state.
        """
        self.current_state = self.q1

    @prime
    def _sleep(self):
        """
        State of sleep.
        """
        while True:
            probability = yield
            probability = yield
            if (self.hours + 3) >= 24:
                print("24 o'clock")
                print("it's time to go to bed!!")
                self.current_state = self.q7
            else:
                if self.hours == 0:
                    if probability <= 0.1:
                        self.hours += 5
                        print(f"{self.hours} o'clock")
                        print("[air raid sirens] not again... tupa rusnya.")
                        self.current_state = self.q1
                    elif probability >= 0.4:
                        self.hours += 7
                        print(f"{self.hours} o'clock")
                        print("[an alarm] another beautiful day :)) and i'm hungry")
                        self.current_state = self.q2
                    elif 0.1 < probability <= 0.2:
                        self.hours += 10
                        print(f"{self.hours} o'clock")
                        print("shit, how could i not hear the alarm")
                        self.current_state = self.q2
                    else:
                        self.hours += 8
                        print(f"{self.hours} o'clock")
                        print("oh no, i have a test in 30 minutes!!")
                        self.current_state = self.q5
                else:
                    self.hours += 3
                    print(f"{self.hours} o'clock")
                    print("[waking up] oh no, have i fallen asleep?")
                    self.current_state = self.q5

    @prime
    def _eat(self):
        """
        To-eat state.
        """
        while True:
            probability = yield
            if (self.hours + 1) >= 24:
                print("24 o'clock")
                print("finishing my day with perfect dinner")
                self.current_state = self.q7
            else:
                if 0 <= self.hours + 1 < 10:
                    self.hours += 1
                    print(f"{self.hours} o'clock")
                    print("[nice breakfast at trapezna]")
                    if probability <= 0.3:
                        self.current_state = self.q5
                    elif 0.3 < probability <= 0.6:
                        self.current_state = self.q3
                    else:
                        self.current_state = self.q4
                elif 10 <= self.hours + 1 < 20:
                    self.hours += 1
                    print(f"{self.hours} o'clock")
                    print("[nice dinner at trapezna]")
                    if probability <= 0.3:
                        self.current_state = self.q5
                    elif 0.3 < probability <= 0.6:
                        self.current_state = self.q3
                    else:
                        self.current_state = self.q4
                else:
                    self.hours += 1
                    print(f"{self.hours} o'clock")
                    print("[me standing in front of trapezna] damn it, it is closed :/")
                    if probability <= 0.3:
                        self.current_state = self.q5
                    elif 0.3 < probability <= 0.6:
                        self.current_state = self.q3
                    else:
                        self.current_state = self.q4

    @prime
    def _relax(self):
        """
        State of relax.
        """
        while True:
            probability = yield
            if (probability >= 0.5 and (self.hours + 2) >= 24) or (self.hours + 1) >= 24:
                print("24 o'clock")
                print("finally i can relax")
                self.current_state = self.q7
            else:
                if probability >= 0.3:
                    if self.hours > 20:
                        self.hours += 2
                        print(f"{self.hours} o'clock")
                        print("[relax time] and it's almost night... why don't i go to bed?")
                        self.current_state = self.q1
                    else:
                        self.hours += 2
                        print(f"{self.hours} o'clock")
                        print("[relax time] now i have energy to study")
                        self.current_state = self.q5
                else:
                    self.hours += 1
                    print(f"{self.hours} o'clock")
                    print("[relax time] seems like relax is becoming procrastination :(")
                    self.current_state = self.q6

    @prime
    def _work_out(self):
        """
        Work-out state.
        """
        while True:
            probability = yield
            if (probability >= 0.75 and (self.hours + 2) >= 24) or (0.5 <= probability < 0.75 and (self.hours + 2) >= 24) or (0.3 <= probability <= 0.5 and (self.hours + 2) >= 24) or (self.hours) >= 24:
                print("24 o'clock")
                print("a perfect way to end a day -- with workout")
                self.current_state = self.q7
            else:
                if probability >= 0.75:
                    self.hours += 2
                    print(f"{self.hours} o'clock")
                    print("[work out time]")
                    self.current_state = self.q3
                elif 0.5 <= probability < 0.75:
                    self.hours += 2
                    print(f"{self.hours} o'clock")
                    print("[work out time]")
                    self.current_state = self.q6
                elif 0.3 <= probability <= 0.5:
                    self.hours += 2
                    print(f"{self.hours} o'clock")
                    print("[work out time] so tired after run. why don't i close my eyes for a few minutes?")
                    self.current_state = self.q1
                else:
                    print(f"{self.hours} o'clock")
                    print("[work out time] of course i could work out... but i'd rather procrastinate")
                    self.current_state = self.q6

    @prime
    def _study(self):
        """
        Study state.
        """
        while True:
            probability = yield
            if (probability >= 0.6 and (self.hours + 5) >= 24) or (0.3 <= probability < 0.6 and (self.hours + 2) >= 24) or (self.hours + 1) >= 24:
                print("24 o'clock")
                print("as true cs student i've decided to end my day with studies")
                self.current_state = self.q7
            else:
                if probability >= 0.6:
                    self.hours += 5
                    print(f"{self.hours} o'clock")
                    print("[study time] wow, i've spend a very productive five hours")
                    self.current_state = self.q3
                elif 0.3 <= probability < 0.6:
                    self.hours += 2
                    print(f"{self.hours} o'clock")
                    print("[study time] i've spend two hours studying and now i'm hungry")
                    self.current_state = self.q2
                else:
                    self.hours += 1
                    print(f"{self.hours} o'clock")
                    print("[study time] now i feel sleepy after reading history")
                    self.current_state = self.q1

    @prime
    def _procrastinate(self):
        """
        Procrastination state.
        """
        while True:
            probability = yield
            if (probability <= 0.7 and (self.hours + 1) >= 24) or (probability > 0.7 and (self.hours + 3) >= 24):
                print("24 o'clock")
                print("for some reason i've decided to end this day with procrastination")
                self.current_state = self.q7
            else:
                if probability <= 0.3:
                    self.hours += 1
                    print(f"{self.hours} o'clock")
                    print("[procrastination] no-no-no i should study! but do i? i'd better go to trapezna!!")
                    self.current_state = self.q2
                elif 0.3 < probability <= 0.7:
                    self.hours += 1
                    print(f"{self.hours} o'clock")
                    print("[procrastination] no-no-no i should do some workout!")
                    self.current_state = self.q4
                else:
                    self.hours += 3
                    print(f"{self.hours} o'clock")
                    print("[procrastination] i've spent 3 unproductive hours and now i have to study")
                    self.current_state = self.q5

    @prime
    def _finita_la_commedia(self):
        """
        Terminal state.
        """
        probability = yield
        print("finita la commedia")
        self.stopped = True
