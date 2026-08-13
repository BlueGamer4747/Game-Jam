import bge, bpy, sys
import mathutils
import math
from collections import OrderedDict


class player_Wrapper():

    def __init__(self, game_object, exec_cond="", startup=False):
        from uplogic import nodes, utils
        from uplogic.nodes.logictree import ULLogicTree
        from uplogic.utils import OPERATORS, LOGIC_OPERATORS
        from uplogic.nodes.parameters import ULVectorMath
        from uplogic.nodes.actions import ULApplyMovement
        from uplogic.nodes.parameters import ULMath
        from uplogic.nodes.parameters import ULVectorXYZ
        from uplogic.nodes.conditions import ULKeyboardActive
        from uplogic.nodes.actions import ULCharacterJump
        from uplogic.nodes.conditions import ULKeyPressed
        from uplogic.nodes.conditions import ULOrList
        from uplogic.nodes.actions import ULSetProperty
        from uplogic.nodes.conditions import ULNot

        self.condition = exec_cond
        owner = self.owner = game_object
        network = self.network = ULLogicTree()
        PAR0000 = ULVectorMath()
        ACT0001 = ULApplyMovement()
        PAR0002 = ULMath()
        PAR0003 = ULMath()
        PAR0004 = ULMath()
        PAR0005 = ULVectorXYZ()
        CON0006 = ULKeyboardActive()
        ACT0007 = ULCharacterJump()
        CON0008 = ULKeyPressed()
        CON0009 = ULKeyPressed()
        CON0010 = ULKeyPressed()
        CON0011 = ULKeyPressed()
        CON0012 = ULKeyPressed()
        CON0013 = ULKeyPressed()
        CON0014 = ULKeyPressed()
        CON0015 = ULKeyPressed()
        CON0016 = ULOrList()
        CON0017 = ULKeyPressed()
        ACT0018 = ULSetProperty()
        CON0019 = ULNot()
        CON0020 = ULNot()
        ACT0021 = ULSetProperty()
        ACT0022 = ULSetProperty()
        CON0023 = ULKeyPressed()
        ACT0024 = ULSetProperty()
        PAR0000.op = "normalize"
        PAR0000.vector = PAR0005.OUTV
        PAR0000.vector_2 = mathutils.Vector((0.0, 0.0, 0.0))
        PAR0000.factor = 1.0
        PAR0000.scale = 0.0
        PAR0000.vector_3 = mathutils.Vector((0.0, 0.0, 0.0))
        PAR0000.ior = 0.0
        ACT0001.local = True
        ACT0001.condition = CON0006
        ACT0001.game_object = "NLO:U_O"
        ACT0001.movement = PAR0004.OUT
        PAR0002.operator = OPERATORS.get("SUB")
        PAR0002.operand_a = CON0012
        PAR0002.operand_b = CON0011
        PAR0003.operator = OPERATORS.get("SUB")
        PAR0003.operand_a = CON0010
        PAR0003.operand_b = CON0009
        PAR0004.operator = OPERATORS.get("MUL")
        PAR0004.operand_a = PAR0000.OUT
        PAR0004.operand_b = 0.20000000298023224
        PAR0005.input_x = PAR0002.OUT
        PAR0005.input_y = PAR0003.OUT
        PAR0005.input_z = 0.0
        ACT0007.condition = CON0008
        ACT0007.game_object = "NLO:U_O"
        CON0008.pulse = False
        CON0008.key_code = bge.events.SPACEKEY
        CON0009.pulse = True
        CON0009.key_code = bge.events.SKEY
        CON0010.pulse = True
        CON0010.key_code = bge.events.WKEY
        CON0011.pulse = True
        CON0011.key_code = bge.events.AKEY
        CON0012.pulse = True
        CON0012.key_code = bge.events.DKEY
        CON0013.pulse = True
        CON0013.key_code = bge.events.AKEY
        CON0014.pulse = True
        CON0014.key_code = bge.events.DKEY
        CON0015.pulse = True
        CON0015.key_code = bge.events.WKEY
        CON0016.ca = CON0014
        CON0016.cb = CON0013
        CON0016.cc = CON0015
        CON0016.cd = CON0017
        CON0016.ce = None
        CON0016.cf = None
        CON0017.pulse = True
        CON0017.key_code = bge.events.SKEY
        ACT0018.mode = "GAME"
        ACT0018.condition = CON0016
        ACT0018.game_object = "NLO:Armature"
        ACT0018.property_name = "walk"
        ACT0018.property_value = True
        CON0019.condition = CON0016
        CON0020.condition = CON0023
        ACT0021.mode = "GAME"
        ACT0021.condition = CON0020.OUT
        ACT0021.game_object = "NLO:Armature"
        ACT0021.property_name = "jump"
        ACT0021.property_value = False
        ACT0022.mode = "GAME"
        ACT0022.condition = CON0019.OUT
        ACT0022.game_object = "NLO:Armature"
        ACT0022.property_name = "walk"
        ACT0022.property_value = False
        CON0023.pulse = True
        CON0023.key_code = bge.events.SPACEKEY
        ACT0024.mode = "GAME"
        ACT0024.condition = CON0023
        ACT0024.game_object = "NLO:Armature"
        ACT0024.property_name = "jump"
        ACT0024.property_value = True
        network.add_cell(CON0006)
        network.add_cell(CON0008)
        network.add_cell(CON0010)
        network.add_cell(CON0012)
        network.add_cell(CON0014)
        network.add_cell(CON0017)
        network.add_cell(CON0023)
        network.add_cell(ACT0007)
        network.add_cell(CON0011)
        network.add_cell(CON0015)
        network.add_cell(CON0020)
        network.add_cell(ACT0024)
        network.add_cell(PAR0002)
        network.add_cell(CON0009)
        network.add_cell(ACT0021)
        network.add_cell(PAR0003)
        network.add_cell(PAR0005)
        network.add_cell(PAR0000)
        network.add_cell(PAR0004)
        network.add_cell(ACT0001)
        network.add_cell(CON0013)
        network.add_cell(CON0016)
        network.add_cell(CON0019)
        network.add_cell(ACT0018)
        network.add_cell(ACT0022)

        owner["IGNLTree_player_"] = network
        network._owner = owner
        network.setup()
        network.stopped = not owner.get('NL__player_')
        self.consumed = startup

    def evaluate(self):
        if self.consumed:
            return
        owner = self.owner
        if self.condition:
            cond = owner[self.condition]
            if not cond: return
        network = self.network
        if network.stopped: return
        shutdown = network.evaluate()
        if shutdown is True:
            self.consumed = True


class player_(bge.types.KX_PythonComponent):
    args = OrderedDict([
        ("Only Run At Startup", False),
        ("Execution Condition", "")
    ])

    def start(self, args):
        self.logictree = player_Wrapper(
            self.object,
            exec_cond=args["Execution Condition"],
            startup=args["Only Run At Startup"]
        )
        self.logictree.evaluate()

    def update(self):
        if not self.logictree.consumed:
            self.logictree.evaluate()


def get_tree(obj):
    return player_Wrapper(obj)