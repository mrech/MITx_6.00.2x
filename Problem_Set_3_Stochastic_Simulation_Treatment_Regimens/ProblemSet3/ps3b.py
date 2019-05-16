# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics

import random
import pylab

'''
Begin helper code
'''


class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """


'''
End helper code
'''

#
# PROBLEM 1
#


class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """

    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.
        maxBirthProb: Maximum reproduction probability (a float between 0-1)
        clearProb: Maximum clearance probability (a float between 0-1).
        """

        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        return self.maxBirthProb

    def getClearProb(self):
        """
        Returns the clear probability.
        """
        return self.clearProb

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step.
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """
        # random.seed(0)

        return random.random() <= self.getClearProb()

    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.

        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """

        self.popDensity = popDensity

        # random.seed(0)
        # Raising Exceptions

        if random.random() > self.maxBirthProb * (1 - self.popDensity):
            raise NoChildException
        else:
            # Create a new instance of SimpleVirus
            return SimpleVirus(self.maxBirthProb, self.clearProb)


'''
# TEST SIMPLEVIRUS
random.seed(0)
maxBirthProb = random.random()
random.seed(0)
clearProb = random.random()
# Instantiate a list of viruses
viruses = []
viruses.append(SimpleVirus(maxBirthProb, clearProb))
viruses[0].getMaxBirthProb()
viruses[0].clearProb
viruses[0].getClearProb()
viruses[0].doesClear()
popDensity = 1/3
viruses[0].maxBirthProb * (1 - popDensity)
foo = []
foo.append(viruses[0].reproduce(popDensity))
'''


class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        """

        self.viruses = viruses
        self.maxPop = maxPop

    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """
        return self.viruses

    def getMaxPop(self):
        """
        Returns the max population.
        """
        return self.maxPop

    def getTotalPop(self):
        """
        Gets the size of the current total virus population.
        returns: The total virus population (an integer)
        """

        return len(self.viruses)

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:

        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.

        - The current population density is calculated. This population density
          value is used until the next call to update()

        - Based on this value of population density, determine whether each
          virus particle should reproduce and add offspring virus particles to
          the list of viruses in this patient.

        returns: The total virus population at the end of the update (an
        integer)
        """

        viruses_copy = self.viruses[:]

        # determine virus survival
        for virus in viruses_copy:
            if virus.doesClear():
                # remove the first matching value
                self.viruses.remove(virus)

        # calculate current pop density based on the surviving viruses
        self.popDensity = len(self.viruses)/self.maxPop

        # determine virus reproduction for the viruses left
        viruses_copy = self.viruses[:]

        for virus in viruses_copy:
            # Handling Exceptions
            try:
                self.viruses.append(virus.reproduce(self.popDensity))
            except NoChildException:
                pass

        return self.getTotalPop()


'''
# TEST PATIENT
# Raising Exception
def testing(bar):
    if bar > 10:
        return 10
    if bar <= 10:
        raise NoChildException
# Handling Exception
for i in [9, 10, 11]:
    try:
        foo.append(testing(i))
    except NoChildException:
        pass

Jhon = Patient(viruses, 3)
Jhon.viruses
Jhon.maxPop
Jhon.getViruses()
Jhon.getMaxPop()
Jhon.getTotalPop()
Jhon.viruses[0].doesClear()
Jhon.update()
Jhon.viruses

# Create a Patient with virus that is never cleared and always reproduces
virus = SimpleVirus(1.0, 0.0)
patient = Patient([virus], 100)
# Updating the patient for 100 trials...
for _ in range(100):
    print('Update #:', _)
    patient.update()

patient.getMaxPop()
patient.getTotalPop()
patient.getViruses()
'''

#
# PROBLEM 2
#


def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    viruses = []

    # Create number of SimpleVirus for patient
    for _ in range(numViruses):
        viruses.append(SimpleVirus(maxBirthProb, clearProb))

    # Instantiate a Patient
    patient = Patient(viruses, maxPop)

    population = [0] * 300

    # Updating the patient for numTrials..
    for _ in range(numTrials):
        # Simulates changes to the virus pop for 300 time steps
        for i in range(300):
            population[i] += patient.update()

    # Calculate average population (divide every elements by number of trials)
    AvgPop = [elem/numTrials for elem in population]  # y-axis

    pylab.plot(AvgPop, label="SimpleVirus")
    pylab.title("SimpleVirus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend(loc="best")
    pylab.show()


'''
# TESTING
# Normal scenario
simulationWithoutDrug(100, 1000, 0.1, 0.05, 100)
# Rapidly increase scenario
simulationWithoutDrug(100, 1000, 0.99, 0.05, 100)
# Rapidly decreasing scenario
simulationWithoutDrug(100, 1000, 0.01, 0.99, 100)
'''

#
# PROBLEM 3
#


class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """
        # Inheritated attributes
        SimpleVirus.__init__(self, maxBirthProb, clearProb)

        # New Attributes
        self.resistances = resistances
        self.mutProb = mutProb

    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        return self.resistances

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        return self.mutProb

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.

        drug: The drug (a string)

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        # Adjust for drugs not in resistances
        # usign get method default value
        return self.resistances.get(drug, False)

    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.

        A virus particle will only reproduce if it is resistant to ALL the drugs
        in the activeDrugs list. For example, if there are 2 drugs in the
        activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        then it will NOT reproduce.

        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:

        self.maxBirthProb * (1 - popDensity).

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.

        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mutProb is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """

        # attributes
        self.popDensity = popDensity
        self.activeDrugs = activeDrugs

        # add new introduced drugs to the dictionary of resistances
        for drug in self.activeDrugs:
            if drug not in list(self.resistances.keys()):
                self.resistances[drug] = False

        # Status of current active drugs
        status_activeDrugs = {k: self.resistances[k] for k in self.activeDrugs}

        # virus resistant to all the drugs
        if all(value == True for value in status_activeDrugs.values()):
            # it reproduces
            # random.seed(0)
            # Raising Exceptions
            if random.random() > self.maxBirthProb * (1 - self.popDensity):
                raise NoChildException
            else:
                # Create a new instance of ResistantVirus
                # Update offspring's resistance trait
                new_resistances = self.resistances.copy()
                for i in self.resistances:
                    # switch resistance's trait
                    if random.random() <= self.mutProb:
                        new_resistances[i] = not new_resistances[i]

                return ResistantVirus(self.maxBirthProb, self.clearProb,
                                      new_resistances, self.mutProb)
        else:
            raise NoChildException


'''
# TESTING RESISTANTVIRUS
random.seed(0)
maxBirthProb = random.random()
random.seed(0)
clearProb = random.random()
resistances = {'guttagonol': False, 'srinol': False}
random.seed(0)
mutProb = random.random()
virus_resistant = ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)
virus_resistant.maxBirthProb
virus_resistant.clearProb
virus_resistant.mutProb
virus_resistant.getResistances()
virus_resistant.getMutProb()
virus_resistant.isResistantTo('srinol')
# Test for virus resistances
virus = ResistantVirus(0.0, 1.0, {"drug1": True, "drug2": False}, 0.0)
# Running virus.reproduce(0, []) to make sure that resistances are not changed.
virus.reproduce(0, [])
virus.isResistantTo('drug3')
'''


class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        """

        # Inheritated attribute
        Patient.__init__(self, viruses, maxPop)

        # attribute for the new class
        #self.viruses = viruses

        # Initializes the list of drugs being administered
        self.administered_drugs = []

    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """
        self.newDrug = newDrug

        # if not in the list add it
        if self.newDrug not in self.administered_drugs:
            self.administered_drugs.append(self.newDrug)

        return self.administered_drugs

    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """

        return self.administered_drugs

    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """

        self.drugResist = drugResist
        resist_pop = 0

        for virus in self.viruses:
            out = []
            for drug in self.drugResist:
                out.append(virus.isResistantTo(drug))
            if all(elem == True for elem in out):
                resist_pop += 1

        return resist_pop

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each
          virus particle should reproduce and add offspring virus particles to
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        """

        viruses_copy = self.viruses[:]

        # determine virus survival
        for virus in viruses_copy:
            if virus.doesClear():
                # remove the first matching value
                self.viruses.remove(virus)

        # calculate current pop density based on the surviving viruses
        self.popDensity = len(self.viruses)/self.maxPop

        if len(self.viruses) > 0:
            for virus in viruses_copy:
                try:
                    self.viruses.append(virus.reproduce(
                        self.popDensity, self.administered_drugs))
                except NoChildException:
                    pass

        return self.getTotalPop()


'''
## Test treated patient
virus = []
virus.append(ResistantVirus(0.1, 0.05,{'guttagonol': True}, 0))
treatedPatient = TreatedPatient(virus, 1)
treatedPatient.viruses
treatedPatient.getPrescriptions()
treatedPatient.addPrescription('drug1')
treatedPatient.getResistPop(['guttagonol', 'drug1'])
treatedPatient.update()

# Create a TreatedPatient with virus that is always cleared and always reproduces.
virus = ResistantVirus(1.0, 1.0, {}, 0.0)
patient = TreatedPatient([virus], 100)
patient.update()
patient.viruses[0].clearProb

patient.viruses[0].doesClear()
patient.viruses.remove(patient.viruses[0])
len(patient.viruses)
for virus in patient.viruses:
    print(virus)
patient.viruses.append(patient.viruses[0](0, []))

# Test of getting TreatedPatient's resistant pop
virus1 = ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0)
virus2 = ResistantVirus(1.0, 0.0, {"drug1": False, "drug2": True}, 0.0)
virus3 = ResistantVirus(1.0, 0.0, {"drug1": True, "drug2": True}, 0.0)
patient = TreatedPatient([virus1, virus2, virus3], 100)
patient.getResistPop(['drug1'])
patient.getResistPop(['drug2'])
patient.getResistPop(['drug1', 'drug2'])
patient.getResistPop(['drug3'])
patient.getResistPop(['drug1', 'drug3'])
patient.getResistPop(['drug1','drug2', 'drug3'])
'''


#
# PROBLEM 4
#


def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1).
    numTrials: number of simulation runs to execute (an integer)

    """

    # TODO
