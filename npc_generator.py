import random
from dataclasses import dataclass
from npc_parameter_enums import Stats, LooksFeatures, Gifts, BehaviorQuirks, Approaches, Ideals, Bonds, Flaws,\
    Origins, WealthClasses, FamilyRelations, OrganizationRelations, OrganizationContributionLevels,\
    SelfEsteem, Goals, Vulnerabilities, GeneralDegrees

@dataclass
class NPC:
    looks: LooksFeatures = LooksFeatures.TATTOOS
    high_stat: Stats = Stats.STRENGTH
    low_stat: Stats = Stats.DEXTERITY
    gift: Gifts = Gifts.DARTIST
    behaviour_quirk: BehaviorQuirks = BehaviorQuirks.Nervous
    approach: Approaches = Approaches.Friendly
    #useful_knowledge: str = "Отсутствует"
    ideal: Ideals = Ideals.Balance
    bond: Bonds = Bonds.Comrads
    flaw: Flaws = Flaws.Gluttony
    secret: str = "Vampire"
    profession: str = "Archer"
    global_goal: Goals = Goals.EarnPositionOrTitle
    current_goal: str = "Pay debts"
    origin: Origins = Origins.Homeless
    wealth: WealthClasses = WealthClasses.Poor
    family_relations: FamilyRelations = FamilyRelations.Neutral
    organization_relations: OrganizationRelations = OrganizationRelations.Neutral
    self_esteem: SelfEsteem = SelfEsteem.Medium
    organization_contributions: OrganizationContributionLevels = OrganizationContributionLevels.Nominal
    vulnerability: Vulnerabilities = Vulnerabilities.No
    religiousness: GeneralDegrees = GeneralDegrees.Medium


    def get_fields_with_possible_values(self):
        fields = []
        for field in self.__dataclass_fields__.values():
            # print(field.type, field.type == type(""))
            values_list = [field.type(elem.value).name for elem in field.type] if field.type != type("") else [""]
            fields.append([field.name, values_list])
        return fields

