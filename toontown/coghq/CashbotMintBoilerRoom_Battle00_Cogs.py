# 2013.08.22 22:18:12 Pacific Daylight Time
# Embedded file name: toontown.coghq.CashbotMintBoilerRoom_Battle00_Cogs
from SpecImports import *
from toontown.toonbase import ToontownGlobals
CogParent = 10000
LowerCogParent = 10003
BattleParent = 10002
LowerBattleParent = 10005
FrontCogParent = 10013
CenterCogParent = 10040
BattleCellId = 0
LowerBattleCellId = 1
FrontBattleCellId = 2
CenterBattleCellId = 3
BattleCells = {BattleCellId: {'parentEntId': BattleParent,
                'pos': Point3(0, 0, 0)},
 LowerBattleCellId: {'parentEntId': LowerBattleParent,
                     'pos': Point3(0, 0, 0)},
 FrontBattleCellId: {'parentEntId': FrontCogParent,
                     'pos': Point3(0, 0, 0)},
 CenterBattleCellId: {'parentEntId': CenterCogParent,
                      'pos': Point3(0, 0, 0)}}
CogData = [{'parentEntId': CogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintSkelecogLevel,
  'battleCell': BattleCellId,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintSkelecogLevel,
  'battleCell': BattleCellId,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintSkelecogLevel,
  'battleCell': BattleCellId,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintSkelecogLevel,
  'battleCell': BattleCellId,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'parentEntId': LowerCogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintCogLevel,
  'battleCell': LowerBattleCellId,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': LowerCogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintSkelecogLevel,
  'battleCell': LowerBattleCellId,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'parentEntId': LowerCogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintSkelecogLevel,
  'battleCell': LowerBattleCellId,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'parentEntId': LowerCogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintCogLevel,
  'battleCell': LowerBattleCellId,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': FrontCogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintCogLevel,
  'battleCell': FrontBattleCellId,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': FrontCogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintCogLevel,
  'battleCell': FrontBattleCellId,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': FrontCogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintCogLevel,
  'battleCell': FrontBattleCellId,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': FrontCogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintCogLevel,
  'battleCell': FrontBattleCellId,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': CenterCogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintCogLevel,
  'battleCell': CenterBattleCellId,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': CenterCogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintSkelecogLevel,
  'battleCell': CenterBattleCellId,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'parentEntId': CenterCogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintSkelecogLevel,
  'battleCell': CenterBattleCellId,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'parentEntId': CenterCogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintCogLevel,
  'battleCell': CenterBattleCellId,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0}]
ReserveCogData = []
# okay decompyling C:\Users\Maverick\Documents\Visual Studio 2010\Projects\Unfreezer\py2\toontown\coghq\CashbotMintBoilerRoom_Battle00_Cogs.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.08.22 22:18:12 Pacific Daylight Time