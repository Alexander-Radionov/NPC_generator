from enum import Enum


class Stats(Enum):
    STRENGTH = 1
    DEXTERITY = 2
    CONSTITUTION = 3
    INTELLIGENCE = 4
    WISDOM = 5
    CHARISMA = 6


class LooksFeatures(Enum):
    NOTABLE_JYWELERY = 1
    PIERCING = 2
    FLUFFY_OR_FOREIGN_CLOTHES = 3
    FORMAL_CLEAN_CLOTHES = 4
    FILTHY_TORN_CLOTHES = 5
    SCAR = 6
    MISSING_TEETH = 7
    MISSING_FINGER = 8
    UNUSUAL_EYE_COLOR = 9
    TATTOOS = 10
    MALL = 11
    UNUSUAL_SKIN_COLOR = 12
    BALD = 13
    PIGTAILS = 14
    UNUSUAL_HAIR_COLOR = 15
    NERVOUS_TIC = 16
    UNUSUAL_NOSE = 17
    UNUSUAL_POSTURE = 18
    SUPREME_BEAUTY = 19
    SUPREME_UGLINNESS = 20


class Gifts(Enum):
    PLAYING_MUSICAL_INSTRUMENT = 1
    SPEAKING_MULTIPLE_LANGUAGES = 2
    LUCKY = 3
    GREAT_MEMORY = 4
    ANIMAL_HANDLER = 5
    CHILDREN_HANDLER = 6
    PAZZLE_SOLVER = 7
    PRO_PLAYER = 8
    IMITATOR = 9
    GOOD_HANDWRITING = 10
    GOOD_ARTIST = 11
    GOOD_SINGER = 12
    GOOD_DRINKER = 13
    GREAT_CARPENTER = 14
    GREAT_COOK = 15
    DARTIST = 16
    JOGGLER = 17
    ACTOR = 18
    DANCER = 19
    THIEF_SPEKER = 20


class BehaviorQuirks(Enum):
    Noisy = 1
    Strange_speech = 2
    Unusual_volume = 3
    Speech_defect = 4
    Extreme_pronounciation = 5
    Complicated_words = 6
    Pompous = 7
    Joker = 8
    Nervous = 9
    Pessimist = 10
    Optimist = 11
    Condescending = 12


class Approaches(Enum):
    Friendly = 1
    Angry = 2
    Boring = 3
    Bragging = 4
    Arrogant = 5
    Suspicious = 6


class Ideals(Enum):
    Beauty = 1
    Charity = 2
    Higher_good = 3
    Respect = 4
    Self_sacrifice = 5
    Domination = 6
    Greed = 7 # greed can be sad. May be split needed
    Power = 8
    Honor = 9
    Society = 10
    Honesty = 11
    Logic = 12
    Responsibility = 13
    Tradition = 13
    Freedom = 14
    Balance = 15
    Knowledge = 16


class Bonds(Enum):
    Personal_goal = 1
    Family = 2
    Comrads = 3
    Patron = 4
    Romance = 5
    Place = 6
    Item = 7
    Sub = 8


class Flaws(Enum):
    Sentiment = 1
    Greed = 2
    Secret = 3
    Recklessness = 4
    Phobia = 5
    Fury = 6
    Lust = 7
    Gluttony = 8
    Envy = 9
    Laziness = 10


class Origins(Enum):
    Nobel = 1
    Wealthy = 2
    Mediocre = 3
    Poor = 4
    Homeless = 5


class WealthClasses(Enum):
    ExtremelyWealth = 1
    Wealthy = 2
    Mediocre = 3
    Poor = 4
    Broke = 5


class FamilyRelations(Enum):
    NoFamily = 1
    VeryBad = 2
    Bad = 3
    Neutral = 4
    Good = 5
    VeryGood = 6


class OrganizationContributionLevels(Enum):
    Nominal = 1
    Consumer = 2
    BalancedContributor = 3
    Provider = 4
    CriticalMember = 5


class OrganizationRelations(Enum):
    NoRelations = 1
    VeryBad = 2
    Bad = 3
    Neutral = 4
    Good = 5
    VeryGood = 6


class SelfEsteem(Enum):
    VeryHigh = 1
    High = 2
    Medium = 3
    Low = 4
    VeryLow = 5
    External = 6


class Goals(Enum):
    GetArtifactForLifeProlongation = 1
    BecomeGod = 2
    BecomeUndead = 3
    GetYongBody = 4
    StealPlanarEntity = 5
    ControlNatureResources = 6
    ControlTrade = 7
    MarryForMoney = 8
    PlunderRuins = 9
    Robbing = 10
    ConquerRegion = 11
    LeadOrganization = 12
    SecretLeadOrganization = 13
    EarnPowerPersonTrust = 14
    WinCompetition = 15
    GetRidOffSomebody = 16
    EarnPositionOrTitle = 17
    FullfillApocalypticProphecy = 18
    FullfillGodsWill = 19
    SpreadDisease = 20
    DethroneGovernment = 21
    CallNatureDisaster = 22
    DestroyClan = 23
    GetAncientArtifact = 24
    CreateMagicItem = 25
    FullfillGodWill = 26
    MakeSacrificeToGod = 27
    OpenGateToAnotherWorld = 28
    AvengeAnInsult = 29
    AvengeAnInjury = 30
    AvengeLoverDeath = 31
    AvengeStolenItem = 32
    ExtendLoverLife = 33
    ProveLove = 34
    ResurrectLover = 35
    DestroyCompetitors = 36


class Vulnerabilities(Enum):
    SoulInsideItem = 1
    LosesPowerIfSomethingVenged = 2
    WeakInPresenceOfSomething = 3
    VulnerableAgainstMaterialOrItem = 4
    DestroyedIfNameOrInfoPronounced = 5
    ProphecyOrPuzzleDescribesVulnerability = 6
    DiesIfForgiven = 7
    LosesPowerIfDealIsFullfilled = 8
    No = 9


class GeneralDegrees(Enum):
    No = 1
    VeryLow = 2
    Low = 3
    Medium = 4
    High = 5
    VeryHigh = 6
