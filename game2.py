def start ():
    print ''' Welcome to demo type 'Start' to begin '''
    print
    prompt_sta ()

def prompt_sta ():
    prompt_0 = raw_input ('Type a Command: ')
    try:
        if prompt_0 in ['Start','start']:
            print
            outside_gates ()
        elif prompt_0 == 'quit()':
            print
            quit()
        else:
            print 'Type Start, not that!'
            print
            prompt_sta ()
    except ValueError:
        print 'Type Start, not that!'
        print
        prompt_sta ()

def outside_gates ():
    print ' You are staring into the gates of a haunted house, the gate is locked and is surrounded by a spiked fence.'
    prompt_outside ()
def prompt_outside ():
    prompt_1 = raw_input ('Type a Command: ')
    try:
        if prompt_1 in ['View Inventory','view inventory']:
            print
            inventory ()
        elif prompt_1 == 'JUMP OVER THE FUCKING FENCE!!!':
            print
            inside_gate ()
        elif prompt_1 == 'quit()':
            print
            quit()
        else:
            print '...'
            print
            prompt_outside ()
    except ValueError:
        print '...'
        print
        prompt_outside ()

def inventory ():
    list1 = ['Flash Light', 'Bolt Cutters', 'Ghost Box']
    for l1 in sorted(set(list1)):
        print l1
        print
    prompt_i = raw_input ('Use: ')
    try:
        if prompt_i in ['Bolt Cutters','bolt cutters']:
            print
            cut_lock ()
        elif prompt_i in ['Flash Light','flash light']:
            print 'The moon is very bright at this hour, you dont need this right now.'
            print
            inventory ()
        elif prompt_i in ['Ghost Box','ghost box']:
            print
            ghost_box ()
        elif prompt_i in ['Exit','exit']:
            print
            outside_gates ()
        else:
            print '...'
            print
            inventory ()
    except ValueError:
        print '...'
        print
        inventory ()

def ghost_box ():
    print'          \\\\\\\\\\\\\\\\\\\\\                                                                      ///////////'
    print'       \                \                                                               /               /'
    print'     \                    \                                                           /                    /'
    print'    \                      \                 /^^^^^^^^^^^^^^^^^^^^^\                 /                      /'
    print'     \                    \       /\/\     /  /-------------------\  \     /\/\       /                    /'
    print'       \                 /      /\/\/\/\  /  /____|________________\  \  /\/\/\/\      \                 /'
    print'        /\/\/\/\/\/\/\/\/\ ___/\/\/\/\/\/\|___________________________|/\/\/\/\/\/\___ /\/\/\/\/\/\/\/\/\\'
    print'       ( -------------- ) /               \-(O)         O         (O) /               \ ( -------------- )'
    print'       ( -------------- )(          0      \        H       S        /      0          )( -------------- )'
    print'       ( ------------- ) ( |||  0  000  0   \   G       o       T   /   0  000  0  ||| ) ( ------------- )'
    print'        \ ----------- /  ( ||| 000 000 000   |      o  ooo  o      |   000 000 000 ||| )  \ ----------- /'
    print'         |  |  |  |  |   ( ||| 000 000 000   |  o  ooo *o  ooo  o  |   000 000 000 ||| )   |  |  |  |  |'
    print'         |  |  |  |  |   ( ||| 000 000 000   | ooo *o      *o  ooo |   000 000 000 ||| )   |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   | *o              *o  |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |    \    000 000 000   |                     |   000 000 000    /    |  |  |  |  |'
    print'         |  |  |  |  |     (   000 000 000   |                     |   000 000 000   )     |  |  |  |  |'
    print'         |  |  |  |  |    (    000 000 000   |   \  /\/\/\/\  /    |   000 000 000    )    |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   |  ( \/        \/ )   |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |  (      000 000 000   | (                )  |   000 000 000      )  |  |  |  |  |'
    print'         |  |  |  |  |  (      000 000 000   | (                )  |   000 000 000      )  |  |  |  |  |'
    print'         |  |  |  |  |  (      000 000 000   |  ( /\        /\ )   |   000 000 000      )  |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   |   /  \/\/\/\/  \    |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |    (    000 000 000   |                     |   000 000 000    )    |  |  |  |  |'
    print'         |  |  |  |  |     (   000 000 000   |      o       o      |   000 000 000   )     |  |  |  |  |'
    print'         |  |  |  |  |    /    000 000 000   |      o   o   o      |   000 000 000    \    |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   |     ooo  o  ooo     |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |   ( ||| 000 000 000   |      o  ooo  o      |   000 000 000 ||| )   |  |  |  |  |'
    print'        / ----------- \  ( ||| 000 000 000   |          o          |   000 000 000 ||| )  / ----------- \\'
    print'       ( ------------- ) ( ||| 000 000 000   |      B       X      |   000 000 000 ||| ) ( ------------- )'
    print'       ( -------------- )( |||  0  000  0   /           O           \   0  000  0  ||| )( -------------- )'
    print'       ( -------------- )(          0      /                         \      0          )( -------------- )'
    print'        \/\/\/\/\/\/\/\/\/\_______________/___________________________\_______________/\/\/\/\/\/\/\/\/\/'
    prompt_gb = raw_input ('Turn on Ghost Box? [Y/N]: ')
    try:
        if prompt_gb in ['Y','y']:
            print
            ghost_box_module ()
        elif prompt_gb in ['N','n']:
            print
            ghost_box_a ()
        else:
            print '...'
            print
            ghost_box ()
    except ValueError:
        print '...'
        print
        ghost_box ()

def ghost_box_a ():
    prompt_gb_a = raw_input ('Put ghost box away? [Y/N]: ')
    try:
        if prompt_gb_a in ['Y','y']:
            print
            inventory ()
        elif prompt_gb_a in ['N','n']:
            print
            ghost_box ()
        else:
            print '...'
            print
            ghost_box_a ()
    except ValueError:
        print '...'
        print
        ghost_box_a ()

def ghost_box_module ():
    print'          \\\\\\\\\\\\\\\\\\\\\                                                                      ///////////'
    print'       \                \                                                               /               /'
    print'     \                    \                                                           /                    /'
    print'    \                      \                 /^^^^^^^^^^^^^^^^^^^^^\                 /                      /'
    print'     \                    \       /\/\     /  /-------------------\  \     /\/\       /                    /'
    print'       \                 /      /\/\/\/\  /  /____|________________\  \  /\/\/\/\      \                 /'
    print'        /\/\/\/\/\/\/\/\/\ ___/\/\/\/\/\/\|___________________________|/\/\/\/\/\/\___ /\/\/\/\/\/\/\/\/\\'
    print'       ( -------------- ) /               \ (O)-        O         (O) /               \ ( -------------- )'
    print'       ( -------------- )(          0      \        H       S        /      0          )( -------------- )'
    print'       ( ------------- ) ( |||  0  000  0   \   G       o       T   /   0  000  0  ||| ) ( ------------- )'
    print'        \ ----------- /  ( ||| 000 000 000   |      o  ooo  o      |   000 000 000 ||| )  \ ----------- /'
    print'         |  |  |  |  |   ( ||| 000 000 000   |  o  ooo *o  ooo  o  |   000 000 000 ||| )   |  |  |  |  |'
    print'         |  |  |  |  |   ( ||| 000 000 000   | ooo *o      *o  ooo |   000 000 000 ||| )   |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   | *o              *o  |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |    \    000 000 000   |                     |   000 000 000    /    |  |  |  |  |'
    print'         |  |  |  |  |     (   000 000 000   |                     |   000 000 000   )     |  |  |  |  |'
    print'         |  |  |  |  |    (    000 000 000   |   \  /\/\/\/\  /    |   000 000 000    )    |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   |  ( \/        \/ )   |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |  (      000 000 000   | ( |-||- |_ |_ () )  |   000 000 000      )  |  |  |  |  |'
    print'         |  |  |  |  |  (      000 000 000   | ( -------------- )  |   000 000 000      )  |  |  |  |  |'
    print'         |  |  |  |  |  (      000 000 000   |  ( /\        /\ )   |   000 000 000      )  |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   |   /  \/\/\/\/  \    |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |    (    000 000 000   |                     |   000 000 000    )    |  |  |  |  |'
    print'         |  |  |  |  |     (   000 000 000   |      o       o      |   000 000 000   )     |  |  |  |  |'
    print'         |  |  |  |  |    /    000 000 000   |      o   o   o      |   000 000 000    \    |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   |     ooo  o  ooo     |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |   ( ||| 000 000 000   |      o  ooo  o      |   000 000 000 ||| )   |  |  |  |  |'
    print'        / ----------- \  ( ||| 000 000 000   |          o          |   000 000 000 ||| )  / ----------- \\'
    print'       ( ------------- ) ( ||| 000 000 000   |      B       X      |   000 000 000 ||| ) ( ------------- )'
    print'       ( -------------- )( |||  0  000  0   /           O           \   0  000  0  ||| )( -------------- )'
    print'       ( -------------- )(          0      /                         \      0          )( -------------- )'
    print'        \/\/\/\/\/\/\/\/\/\_______________/___________________________\_______________/\/\/\/\/\/\/\/\/\/'
    module = ['OFF', 'GHOST', 'Bal', 'Options', 'X-terminate']
    for m in sorted(set(module)):
        print m
        print
    prompt_gbm = raw_input ('Select: ')
    try:
        if prompt_gbm in ['OFF','Off','off']:
            print
            ghost_box_a ()
        elif prompt_gbm in ['GHOST','Ghost','ghost','G','g']:
            print
            GHOST ()
        elif prompt_gbm in ['Bal','bal','Balance','balance','B','b']:
            print
            Bal ()
        elif prompt_gbm in ['Options','options','O','o']:
            print
            Options ()
        elif prompt_gbm in ['X-terminate','x-terminate','X','x']:
            print
            X-terminate ()
        else:
            print '...'
            print
            ghost_box_module ()
    except ValueError:
        print '...'
        print
        ghost_box_module ()

def GHOST ():
    print'          \\\\\\\\\\\\\\\\\\\\\                                                                      ///////////'
    print'       \                \                                                               /               /'
    print'     \                    \                                                           /                    /'
    print'    \                      \                 /^^^^^^^^^^^^^^^^^^^^^\                 /                      /'
    print'     \                    \       /\/\     /  /-------------------\  \     /\/\       /                    /'
    print'       \                 /      /\/\/\/\  /  /____|________________\  \  /\/\/\/\      \                 /'
    print'        /\/\/\/\/\/\/\/\/\ ___/\/\/\/\/\/\|___________________________|/\/\/\/\/\/\___ /\/\/\/\/\/\/\/\/\\'
    print'       ( -------------- ) /               \ (O)-        O         (O) /               \ ( -------------- )'
    print'       ( -------------- )(          0      \        H       S        /      0          )( -------------- )'
    print'       ( ------------- ) ( |||  0  000  0   \   G       o       T   /   0  000  0  ||| ) ( ------------- )'
    print'        \ ----------- /  ( ||| 000 000 000   |      o  ooo  o      |   000 000 000 ||| )  \ ----------- /'
    print'         |  |  |  |  |   ( ||| 000 000 000   |  o  ooo *o  ooo  o  |   000 000 000 ||| )   |  |  |  |  |'
    print'         |  |  |  |  |   ( ||| 000 000 000   | ooo *o      *o  ooo |   000 000 000 ||| )   |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   | *o              *o  |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |    \    000 000 000   |                     |   000 000 000    /    |  |  |  |  |'
    print'         |  |  |  |  |     (   000 000 000   |                     |   000 000 000   )     |  |  |  |  |'
    print'         |  |  |  |  |    (    000 000 000   |   \  /\/\/\/\  /    |   000 000 000    )    |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   |  ( \/        \/ )   |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |  (      000 000 000   | ( |-||- |_ |_ () )  |   000 000 000      )  |  |  |  |  |'
    print'         |  |  |  |  |  (      000 000 000   | ( -------------- )  |   000 000 000      )  |  |  |  |  |'
    print'         |  |  |  |  |  (      000 000 000   |  ( /\        /\ )   |   000 000 000      )  |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   |   /  \/\/\/\/  \    |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |    (    000 000 000   |                     |   000 000 000    )    |  |  |  |  |'
    print'         |  |  |  |  |     (   000 000 000   |      o       o      |   000 000 000   )     |  |  |  |  |'
    print'         |  |  |  |  |    /    000 000 000   |      o   o   o      |   000 000 000    \    |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   |     ooo  o  ooo     |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |   ( ||| 000 000 000   |      o  ooo  o      |   000 000 000 ||| )   |  |  |  |  |'
    print'        / ----------- \  ( ||| 000 000 000   |          o          |   000 000 000 ||| )  / ----------- \\'
    print'       ( ------------- ) ( ||| 000 000 000   |      B       X      |   000 000 000 ||| ) ( ------------- )'
    print'       ( -------------- )( |||  0  000  0   /           O           \   0  000  0  ||| )( -------------- )'
    print'       ( -------------- )(          0      /                         \      0          )( -------------- )'
    print'        \/\/\/\/\/\/\/\/\/\_______________/___________________________\_______________/\/\/\/\/\/\/\/\/\/'
    prompt_ghost = raw_input ('Turn each of the G, H, O, S, T knobs to desired value [5 numbers 1-7]: ')
    print ' There is no signal coming in at the moment.'
    print
    ghost_box_module ()

def cut_lock ():
    prompt_3 = raw_input ('Cut Lock? [Y/N]: ')
    try:
        if prompt_3 in ['Y','y']:
            print
            print 'You are now inside the gate, there is a trail leading up to the door of the house.'
            inside_gates ()
        elif prompt_3 in ['N','n']:
            print
            outside_gates ()
        else:
            print '...'
            print
            cut_lock ()
    except ValueError:
        print '...'
        print
        cut_lock ()

def inside_gates ():
    prompt_4 = raw_input ('Type a command: ')
    try:
        if prompt_4 in ['Walk North','walk north','WN','wn']:
            print
            print 'You are now at the door.'
            front_door ()
        elif prompt_4 in ['View Inventory','view inventory','V','v']:
            print
            inventory_p_4 ()
        elif prompt_4 == 'quit()':
            print
            quit()
        else:
            print '...'
            print
    except ValueError:
        print '...'
        print

def inventory_p_4 ():
    list1 = ['Flash Light', 'Bolt Cutters', 'Ghost Box']
    for l1 in sorted(set(list1)):
        print l1
        print
    prompt_i_1 = raw_input ('Use: ')
    try:
        if prompt_i_1 in ['Bolt Cutters','bolt cutters']:
            print " You don't need this right now."
            print
            inventory_p_4 ()
        elif prompt_i_1 in ['Flash Light','flash light']:
            print 'The moon is very bright at this hour, you dont need this right now.'
            print
            inventory_p_4 ()
        elif prompt_i_1 in ['Ghost Box','ghost box']:
            print
            ghost_box_1 ()
        elif prompt_i_1 in ['Exit','exit']:
            print
            inside_gates ()
        else:
            print '...'
            print
            inventory_p_4 ()
    except ValueError:
        print '...'
        print
        inventory_p_4 ()

def ghost_box_1 ():
    print'          \\\\\\\\\\\\\\\\\\\\\                                                                      ///////////'
    print'       \                \                                                               /               /'
    print'     \                    \                                                           /                    /'
    print'    \                      \                 /^^^^^^^^^^^^^^^^^^^^^\                 /                      /'
    print'     \                    \       /\/\     /  /-------------------\  \     /\/\       /                    /'
    print'       \                 /      /\/\/\/\  /  /____|________________\  \  /\/\/\/\      \                 /'
    print'        /\/\/\/\/\/\/\/\/\ ___/\/\/\/\/\/\|___________________________|/\/\/\/\/\/\___ /\/\/\/\/\/\/\/\/\\'
    print'       ( -------------- ) /               \-(O)         O         (O) /               \ ( -------------- )'
    print'       ( -------------- )(          0      \        H       S        /      0          )( -------------- )'
    print'       ( ------------- ) ( |||  0  000  0   \   G       o       T   /   0  000  0  ||| ) ( ------------- )'
    print'        \ ----------- /  ( ||| 000 000 000   |      o  ooo  o      |   000 000 000 ||| )  \ ----------- /'
    print'         |  |  |  |  |   ( ||| 000 000 000   |  o  ooo *o  ooo  o  |   000 000 000 ||| )   |  |  |  |  |'
    print'         |  |  |  |  |   ( ||| 000 000 000   | ooo *o      *o  ooo |   000 000 000 ||| )   |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   | *o              *o  |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |    \    000 000 000   |                     |   000 000 000    /    |  |  |  |  |'
    print'         |  |  |  |  |     (   000 000 000   |                     |   000 000 000   )     |  |  |  |  |'
    print'         |  |  |  |  |    (    000 000 000   |   \  /\/\/\/\  /    |   000 000 000    )    |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   |  ( \/        \/ )   |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |  (      000 000 000   | (                )  |   000 000 000      )  |  |  |  |  |'
    print'         |  |  |  |  |  (      000 000 000   | (                )  |   000 000 000      )  |  |  |  |  |'
    print'         |  |  |  |  |  (      000 000 000   |  ( /\        /\ )   |   000 000 000      )  |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   |   /  \/\/\/\/  \    |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |    (    000 000 000   |                     |   000 000 000    )    |  |  |  |  |'
    print'         |  |  |  |  |     (   000 000 000   |      o       o      |   000 000 000   )     |  |  |  |  |'
    print'         |  |  |  |  |    /    000 000 000   |      o   o   o      |   000 000 000    \    |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   |     ooo  o  ooo     |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |   ( ||| 000 000 000   |      o  ooo  o      |   000 000 000 ||| )   |  |  |  |  |'
    print'        / ----------- \  ( ||| 000 000 000   |          o          |   000 000 000 ||| )  / ----------- \\'
    print'       ( ------------- ) ( ||| 000 000 000   |      B       X      |   000 000 000 ||| ) ( ------------- )'
    print'       ( -------------- )( |||  0  000  0   /           O           \   0  000  0  ||| )( -------------- )'
    print'       ( -------------- )(          0      /                         \      0          )( -------------- )'
    print'        \/\/\/\/\/\/\/\/\/\_______________/___________________________\_______________/\/\/\/\/\/\/\/\/\/'
    prompt_gb_1 = raw_input ('Turn on Ghost Box? [Y/N]: ')
    try:
        if prompt_gb_1 in ['Y','y']:
            print
            ghost_box_module_1 ()
        elif prompt_gb_1 in ['N','n']:
            print
            ghost_box_a_1 ()
        else:
            print '...'
            print
            ghost_box_1 ()
    except ValueError:
        print '...'
        print
        ghost_box_1 ()

def ghost_box_a_1 ():
    prompt_gb_a_1 = raw_input ('Put ghost box away? [Y/N]: ')
    try:
        if prompt_gb_a_1 in ['Y','y']:
            print
            inventory_p_4 ()
        elif prompt_gb_a_1 in ['N','n']:
            print
            ghost_box_1 ()
        else:
            print '...'
            print
            ghost_box_a_1 ()
    except ValueError:
        print '...'
        print
        ghost_box_a_1 ()

def ghost_box_module_1 ():
    print'          \\\\\\\\\\\\\\\\\\\\\                                                                      ///////////'
    print'       \                \                                                               /               /'
    print'     \                    \                                                           /                    /'
    print'    \                      \                 /^^^^^^^^^^^^^^^^^^^^^\                 /                      /'
    print'     \                    \       /\/\     /  /-------------------\  \     /\/\       /                    /'
    print'       \                 /      /\/\/\/\  /  /____|________________\  \  /\/\/\/\      \                 /'
    print'        /\/\/\/\/\/\/\/\/\ ___/\/\/\/\/\/\|___________________________|/\/\/\/\/\/\___ /\/\/\/\/\/\/\/\/\\'
    print'       ( -------------- ) /               \ (O)-        O         (O) /               \ ( -------------- )'
    print'       ( -------------- )(          0      \        H       S        /      0          )( -------------- )'
    print'       ( ------------- ) ( |||  0  000  0   \   G       o       T   /   0  000  0  ||| ) ( ------------- )'
    print'        \ ----------- /  ( ||| 000 000 000   |      o  ooo  o      |   000 000 000 ||| )  \ ----------- /'
    print'         |  |  |  |  |   ( ||| 000 000 000   |  o  ooo *o  ooo  o  |   000 000 000 ||| )   |  |  |  |  |'
    print'         |  |  |  |  |   ( ||| 000 000 000   | ooo *o      *o  ooo |   000 000 000 ||| )   |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   | *o              *o  |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |    \    000 000 000   |                     |   000 000 000    /    |  |  |  |  |'
    print'         |  |  |  |  |     (   000 000 000   |                     |   000 000 000   )     |  |  |  |  |'
    print'         |  |  |  |  |    (    000 000 000   |   \  /\/\/\/\  /    |   000 000 000    )    |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   |  ( \/        \/ )   |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |  (      000 000 000   | ( |-||- |_ |_ () )  |   000 000 000      )  |  |  |  |  |'
    print'         |  |  |  |  |  (      000 000 000   | ( -------------- )  |   000 000 000      )  |  |  |  |  |'
    print'         |  |  |  |  |  (      000 000 000   |  ( /\        /\ )   |   000 000 000      )  |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   |   /  \/\/\/\/  \    |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |    (    000 000 000   |                     |   000 000 000    )    |  |  |  |  |'
    print'         |  |  |  |  |     (   000 000 000   |      o       o      |   000 000 000   )     |  |  |  |  |'
    print'         |  |  |  |  |    /    000 000 000   |      o   o   o      |   000 000 000    \    |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   |     ooo  o  ooo     |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |   ( ||| 000 000 000   |      o  ooo  o      |   000 000 000 ||| )   |  |  |  |  |'
    print'        / ----------- \  ( ||| 000 000 000   |          o          |   000 000 000 ||| )  / ----------- \\'
    print'       ( ------------- ) ( ||| 000 000 000   |      B       X      |   000 000 000 ||| ) ( ------------- )'
    print'       ( -------------- )( |||  0  000  0   /           O           \   0  000  0  ||| )( -------------- )'
    print'       ( -------------- )(          0      /                         \      0          )( -------------- )'
    print'        \/\/\/\/\/\/\/\/\/\_______________/___________________________\_______________/\/\/\/\/\/\/\/\/\/'
    module = ['OFF', 'GHOST', 'Bal', 'Options', 'X-terminate']
    for m in sorted(set(module)):
        print m
        print
    prompt_gbm_1 = raw_input ('Select: ')
    try:
        if prompt_gbm_1 in ['OFF','Off','off']:
            print
            ghost_box_a_1 ()
        elif prompt_gbm_1 in ['GHOST','Ghost','ghost','G','g']:
            print
            GHOST_1 ()
        elif prompt_gbm_1 in ['Bal','bal','Balance','balance','B','b']:
            print
            Bal_1 ()
        elif prompt_gbm_1 in ['Options','options','O','o']:
            print
            Options_1 ()
        elif prompt_gbm_1 in ['X-terminate','x-terminate','X','x']:
            print
            X-terminate_1 ()
        else:
            print '...'
            print
            ghost_box_module_1 ()
    except ValueError:
        print '...'
        print
        ghost_box_module_1 ()

def GHOST_1 ():
    print'          \\\\\\\\\\\\\\\\\\\\\                                                                      ///////////'
    print'       \                \                                                               /               /'
    print'     \                    \                                                           /                    /'
    print'    \                      \                 /^^^^^^^^^^^^^^^^^^^^^\                 /                      /'
    print'     \                    \       /\/\     /  /-------------------\  \     /\/\       /                    /'
    print'       \                 /      /\/\/\/\  /  /____|________________\  \  /\/\/\/\      \                 /'
    print'        /\/\/\/\/\/\/\/\/\ ___/\/\/\/\/\/\|___________________________|/\/\/\/\/\/\___ /\/\/\/\/\/\/\/\/\\'
    print'       ( -------------- ) /               \ (O)-        O         (O) /               \ ( -------------- )'
    print'       ( -------------- )(          0      \        H       S        /      0          )( -------------- )'
    print'       ( ------------- ) ( |||  0  000  0   \   G       o       T   /   0  000  0  ||| ) ( ------------- )'
    print'        \ ----------- /  ( ||| 000 000 000   |      o  ooo  o      |   000 000 000 ||| )  \ ----------- /'
    print'         |  |  |  |  |   ( ||| 000 000 000   |  o  ooo *o  ooo  o  |   000 000 000 ||| )   |  |  |  |  |'
    print'         |  |  |  |  |   ( ||| 000 000 000   | ooo *o      *o  ooo |   000 000 000 ||| )   |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   | *o              *o  |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |    \    000 000 000   |                     |   000 000 000    /    |  |  |  |  |'
    print'         |  |  |  |  |     (   000 000 000   |                     |   000 000 000   )     |  |  |  |  |'
    print'         |  |  |  |  |    (    000 000 000   |   \  /\/\/\/\  /    |   000 000 000    )    |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   |  ( \/        \/ )   |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |  (      000 000 000   | ( |-||- |_ |_ () )  |   000 000 000      )  |  |  |  |  |'
    print'         |  |  |  |  |  (      000 000 000   | ( -------------- )  |   000 000 000      )  |  |  |  |  |'
    print'         |  |  |  |  |  (      000 000 000   |  ( /\        /\ )   |   000 000 000      )  |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   |   /  \/\/\/\/  \    |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |    (    000 000 000   |                     |   000 000 000    )    |  |  |  |  |'
    print'         |  |  |  |  |     (   000 000 000   |      o       o      |   000 000 000   )     |  |  |  |  |'
    print'         |  |  |  |  |    /    000 000 000   |      o   o   o      |   000 000 000    \    |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   |     ooo  o  ooo     |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |   ( ||| 000 000 000   |      o  ooo  o      |   000 000 000 ||| )   |  |  |  |  |'
    print'        / ----------- \  ( ||| 000 000 000   |          o          |   000 000 000 ||| )  / ----------- \\'
    print'       ( ------------- ) ( ||| 000 000 000   |      B       X      |   000 000 000 ||| ) ( ------------- )'
    print'       ( -------------- )( |||  0  000  0   /           O           \   0  000  0  ||| )( -------------- )'
    print'       ( -------------- )(          0      /                         \      0          )( -------------- )'
    print'        \/\/\/\/\/\/\/\/\/\_______________/___________________________\_______________/\/\/\/\/\/\/\/\/\/'
    prompt_ghost_1 = raw_input ('Turn each of the G, H, O, S, T knobs to desired value [5 numbers 1-7]: ')
    print ' There is no signal coming in at the moment.'
    print
    ghost_box_module_1 ()

def front_door ():
    print 'The door just opened by itself.'
    prompt_4_1 = raw_input ('Continue? [Y/N]: ')
    try:
        if prompt_4_1 in ['Y','y']:
            print
            inside_house ()
        elif prompt_4_1 in ['N','n']:
            print
            quit()
        else:
            print '...'
            print
            front_door ()
    except ValueError:
        print '...'
        print
        front_door ()

def inside_house ():
    print "You are now inside the house, it's very cold even though its warm outside, and its too dark to see anything."
    prompt_5 = raw_input ('Type a command: ')
    try:
        if prompt_5 in ['View Inventory','view inventory','V','v']:
            print
            inventory_p_5 ()
        elif prompt_5 == 'quit()':
            print
            quit()
        else:
            print '...'
            print
            inside_house ()
    except ValueError:
        print '...'
        print
        inside_house ()

def inventory_p_5 ():
    list1 = ['Flash Light', 'Bolt Cutters', 'Ghost Box']
    for l1 in sorted(set(list1)):
        print l1
        print
    prompt_i_2 = raw_input ('Use: ')
    try:
        if prompt_i_2 in ['Bolt Cutters','bolt cutters']:
            print " You don't need this right now."
            print
            inventory_p_5 ()
        elif prompt_i_2 in ['Flash Light','flash light']:
            print 'The flash light has full battery, check the battery life often to see how much juice it has, you can check the life by typing [BL] or [bl]. When the battery is running low you can find more batteries by searching for them around the house.'
            print
            den ()
        elif prompt_i_2 in ['Ghost Box','ghost box']:
            print
            ghost_box_2 ()
        elif prompt_i_2 in ['Exit','exit']:
            print
            inside_house ()
        else:
            print '...'
            print
            inventory_p_5 ()
    except ValueError:
        print '...'
        print
        inventory_p_5 ()

def ghost_box_2 ():
    print'          \\\\\\\\\\\\\\\\\\\\\                                                                      ///////////'
    print'       \                \                                                               /               /'
    print'     \                    \                                                           /                    /'
    print'    \                      \                 /^^^^^^^^^^^^^^^^^^^^^\                 /                      /'
    print'     \                    \       /\/\     /  /-------------------\  \     /\/\       /                    /'
    print'       \                 /      /\/\/\/\  /  /____|________________\  \  /\/\/\/\      \                 /'
    print'        /\/\/\/\/\/\/\/\/\ ___/\/\/\/\/\/\|___________________________|/\/\/\/\/\/\___ /\/\/\/\/\/\/\/\/\\'
    print'       ( -------------- ) /               \-(O)         O         (O) /               \ ( -------------- )'
    print'       ( -------------- )(          0      \        H       S        /      0          )( -------------- )'
    print'       ( ------------- ) ( |||  0  000  0   \   G       o       T   /   0  000  0  ||| ) ( ------------- )'
    print'        \ ----------- /  ( ||| 000 000 000   |      o  ooo  o      |   000 000 000 ||| )  \ ----------- /'
    print'         |  |  |  |  |   ( ||| 000 000 000   |  o  ooo *o  ooo  o  |   000 000 000 ||| )   |  |  |  |  |'
    print'         |  |  |  |  |   ( ||| 000 000 000   | ooo *o      *o  ooo |   000 000 000 ||| )   |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   | *o              *o  |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |    \    000 000 000   |                     |   000 000 000    /    |  |  |  |  |'
    print'         |  |  |  |  |     (   000 000 000   |                     |   000 000 000   )     |  |  |  |  |'
    print'         |  |  |  |  |    (    000 000 000   |   \  /\/\/\/\  /    |   000 000 000    )    |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   |  ( \/        \/ )   |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |  (      000 000 000   | (                )  |   000 000 000      )  |  |  |  |  |'
    print'         |  |  |  |  |  (      000 000 000   | (                )  |   000 000 000      )  |  |  |  |  |'
    print'         |  |  |  |  |  (      000 000 000   |  ( /\        /\ )   |   000 000 000      )  |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   |   /  \/\/\/\/  \    |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |    (    000 000 000   |                     |   000 000 000    )    |  |  |  |  |'
    print'         |  |  |  |  |     (   000 000 000   |      o       o      |   000 000 000   )     |  |  |  |  |'
    print'         |  |  |  |  |    /    000 000 000   |      o   o   o      |   000 000 000    \    |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   |     ooo  o  ooo     |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |   ( ||| 000 000 000   |      o  ooo  o      |   000 000 000 ||| )   |  |  |  |  |'
    print'        / ----------- \  ( ||| 000 000 000   |          o          |   000 000 000 ||| )  / ----------- \\'
    print'       ( ------------- ) ( ||| 000 000 000   |      B       X      |   000 000 000 ||| ) ( ------------- )'
    print'       ( -------------- )( |||  0  000  0   /           O           \   0  000  0  ||| )( -------------- )'
    print'       ( -------------- )(          0      /                         \      0          )( -------------- )'
    print'        \/\/\/\/\/\/\/\/\/\_______________/___________________________\_______________/\/\/\/\/\/\/\/\/\/'
    prompt_gb_2 = raw_input ('Turn on Ghost Box? [Y/N]: ')
    try:
        if prompt_gb_2 in ['Y','y']:
            print
            ghost_box_module_2 ()
        elif prompt_gb_2 in ['N','n']:
            print
            ghost_box_a_2 ()
        else:
            print '...'
            print
            ghost_box_2 ()
    except ValueError:
        print '...'
        print
        ghost_box_2 ()

def ghost_box_a_2 ():
    prompt_gb_a_2 = raw_input ('Put ghost box away? [Y/N]: ')
    try:
        if prompt_gb_a_2 in ['Y','y']:
            print
            inventory_p_5 ()
        elif prompt_gb_a_2 in ['N','n']:
            print
            ghost_box_2 ()
        else:
            print '...'
            print
            ghost_box_a_2 ()
    except ValueError:
        print '...'
        print
        ghost_box_a_2 ()

def ghost_box_module_2 ():
    print'          \\\\\\\\\\\\\\\\\\\\\                                                                      ///////////'
    print'       \                \                                                               /               /'
    print'     \                    \                                                           /                    /'
    print'    \                      \                 /^^^^^^^^^^^^^^^^^^^^^\                 /                      /'
    print'     \                    \       /\/\     /  /-------------------\  \     /\/\       /                    /'
    print'       \                 /      /\/\/\/\  /  /____|________________\  \  /\/\/\/\      \                 /'
    print'        /\/\/\/\/\/\/\/\/\ ___/\/\/\/\/\/\|___________________________|/\/\/\/\/\/\___ /\/\/\/\/\/\/\/\/\\'
    print'       ( -------------- ) /               \ (O)-        O         (O) /               \ ( -------------- )'
    print'       ( -------------- )(          0      \        H       S        /      0          )( -------------- )'
    print'       ( ------------- ) ( |||  0  000  0   \   G       o       T   /   0  000  0  ||| ) ( ------------- )'
    print'        \ ----------- /  ( ||| 000 000 000   |      o  ooo  o      |   000 000 000 ||| )  \ ----------- /'
    print'         |  |  |  |  |   ( ||| 000 000 000   |  o  ooo *o  ooo  o  |   000 000 000 ||| )   |  |  |  |  |'
    print'         |  |  |  |  |   ( ||| 000 000 000   | ooo *o      *o  ooo |   000 000 000 ||| )   |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   | *o              *o  |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |    \    000 000 000   |                     |   000 000 000    /    |  |  |  |  |'
    print'         |  |  |  |  |     (   000 000 000   |                     |   000 000 000   )     |  |  |  |  |'
    print'         |  |  |  |  |    (    000 000 000   |   \  /\/\/\/\  /    |   000 000 000    )    |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   |  ( \/        \/ )   |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |  (      000 000 000   | ( |-||- |_ |_ () )  |   000 000 000      )  |  |  |  |  |'
    print'         |  |  |  |  |  (      000 000 000   | ( -------------- )  |   000 000 000      )  |  |  |  |  |'
    print'         |  |  |  |  |  (      000 000 000   |  ( /\        /\ )   |   000 000 000      )  |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   |   /  \/\/\/\/  \    |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |    (    000 000 000   |                     |   000 000 000    )    |  |  |  |  |'
    print'         |  |  |  |  |     (   000 000 000   |      o       o      |   000 000 000   )     |  |  |  |  |'
    print'         |  |  |  |  |    /    000 000 000   |      o   o   o      |   000 000 000    \    |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   |     ooo  o  ooo     |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |   ( ||| 000 000 000   |      o  ooo  o      |   000 000 000 ||| )   |  |  |  |  |'
    print'        / ----------- \  ( ||| 000 000 000   |          o          |   000 000 000 ||| )  / ----------- \\'
    print'       ( ------------- ) ( ||| 000 000 000   |      B       X      |   000 000 000 ||| ) ( ------------- )'
    print'       ( -------------- )( |||  0  000  0   /           O           \   0  000  0  ||| )( -------------- )'
    print'       ( -------------- )(          0      /                         \      0          )( -------------- )'
    print'        \/\/\/\/\/\/\/\/\/\_______________/___________________________\_______________/\/\/\/\/\/\/\/\/\/'
    module = ['OFF', 'GHOST', 'Bal', 'Options', 'X-terminate']
    for m in sorted(set(module)):
        print m
        print
    prompt_gbm_2 = raw_input ('Select: ')
    try:
        if prompt_gbm_2 in ['OFF','Off','off']:
            print
            ghost_box_a_2 ()
        elif prompt_gbm_2 in ['GHOST','Ghost','ghost','G','g']:
            print
            GHOST_2 ()
        elif prompt_gbm_2 in ['Bal','bal','Balance','balance','B','b']:
            print
            Bal_2 ()
        elif prompt_gbm_2 in ['Options','options','O','o']:
            print
            Options_2 ()
        elif prompt_gbm_2 in ['X-terminate','x-terminate','X','x']:
            print
            X-terminate_2 ()
        else:
            print '...'
            print
            ghost_box_module_2 ()
    except ValueError:
        print '...'
        print
        ghost_box_module_2 ()

def GHOST_2 ():
    print'          \\\\\\\\\\\\\\\\\\\\\                                                                      ///////////'
    print'       \                \                                                               /               /'
    print'     \                    \                                                           /                    /'
    print'    \                      \                 /^^^^^^^^^^^^^^^^^^^^^\                 /                      /'
    print'     \                    \       /\/\     /  /-------------------\  \     /\/\       /                    /'
    print'       \                 /      /\/\/\/\  /  /____|________________\  \  /\/\/\/\      \                 /'
    print'        /\/\/\/\/\/\/\/\/\ ___/\/\/\/\/\/\|___________________________|/\/\/\/\/\/\___ /\/\/\/\/\/\/\/\/\\'
    print'       ( -------------- ) /               \ (O)-        O         (O) /               \ ( -------------- )'
    print'       ( -------------- )(          0      \        H       S        /      0          )( -------------- )'
    print'       ( ------------- ) ( |||  0  000  0   \   G       o       T   /   0  000  0  ||| ) ( ------------- )'
    print'        \ ----------- /  ( ||| 000 000 000   |      o  ooo  o      |   000 000 000 ||| )  \ ----------- /'
    print'         |  |  |  |  |   ( ||| 000 000 000   |  o  ooo *o  ooo  o  |   000 000 000 ||| )   |  |  |  |  |'
    print'         |  |  |  |  |   ( ||| 000 000 000   | ooo *o      *o  ooo |   000 000 000 ||| )   |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   | *o              *o  |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |    \    000 000 000   |                     |   000 000 000    /    |  |  |  |  |'
    print'         |  |  |  |  |     (   000 000 000   |                     |   000 000 000   )     |  |  |  |  |'
    print'         |  |  |  |  |    (    000 000 000   |   \  /\/\/\/\  /    |   000 000 000    )    |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   |  ( \/        \/ )   |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |  (      000 000 000   | ( |-||- |_ |_ () )  |   000 000 000      )  |  |  |  |  |'
    print'         |  |  |  |  |  (      000 000 000   | ( -------------- )  |   000 000 000      )  |  |  |  |  |'
    print'         |  |  |  |  |  (      000 000 000   |  ( /\        /\ )   |   000 000 000      )  |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   |   /  \/\/\/\/  \    |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |    (    000 000 000   |                     |   000 000 000    )    |  |  |  |  |'
    print'         |  |  |  |  |     (   000 000 000   |      o       o      |   000 000 000   )     |  |  |  |  |'
    print'         |  |  |  |  |    /    000 000 000   |      o   o   o      |   000 000 000    \    |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   |     ooo  o  ooo     |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |   ( ||| 000 000 000   |      o  ooo  o      |   000 000 000 ||| )   |  |  |  |  |'
    print'        / ----------- \  ( ||| 000 000 000   |          o          |   000 000 000 ||| )  / ----------- \\'
    print'       ( ------------- ) ( ||| 000 000 000   |      B       X      |   000 000 000 ||| ) ( ------------- )'
    print'       ( -------------- )( |||  0  000  0   /           O           \   0  000  0  ||| )( -------------- )'
    print'       ( -------------- )(          0      /                         \      0          )( -------------- )'
    print'        \/\/\/\/\/\/\/\/\/\_______________/___________________________\_______________/\/\/\/\/\/\/\/\/\/'
    prompt_ghost_2 = raw_input ('Turn each of the G, H, O, S, T knobs to desired value [5 numbers 1-7]: ')
    print ' There is no signal coming in at the moment.'
    print
    ghost_box_module_2 ()

def den ():
    prompt_6 = raw_input ('Type a command: ')
    try:
        if prompt_6 in ['BL','bl']:
            print '{||||}'
            print
            den ()
        elif prompt_6 in ['View Inventory','view inventory']:
            print
            inventory_p_6 ()
        elif prompt_6 == 'quit()':
            print
            quit()
        elif prompt_6 in ['LN','ln']:
            print "There's a door."
            print
            den ()
        elif prompt_6 in ['LE','le']:
            print "There's a door."
            print
            den ()
        elif prompt_6 in ['LS','ls']:
            print "That's the front door."
            print
            den ()
        elif prompt_6 in ['LW','lw']:
            print "There's a chair."
            print
            den ()
        elif prompt_6 in ['LNE','lne']:
            print "There's a stair case with a crawl space under it."
            print
            den ()
        elif prompt_6 in ['LNW','lnw']:
            print "There's a couch."
            print
            den ()
        elif prompt_6 in ['LSE','lse']:
            print "There's a window."
            print
            den ()
        elif prompt_6 in ['LSW','lsw']:
            print "There's an old crt TV with a window behind it."
            print
            den ()
        elif prompt_6 in ['WN','wn']:
            print
            den_n ()
        elif prompt_6 in ['WE','we']:
            print
            den_e ()
        elif prompt_6 in ['WS','ws']:
            print
            den_s ()
        elif prompt_6 in ['WW','ww']:
            print
            den_w ()
        elif prompt_6 in ['WNE','wne']:
            print
            den_ne ()
        elif prompt_6 in ['WNW','wnw']:
            print
            den_nw ()
        elif prompt_6 in ['WSE','wse']:
            print
            den_se ()
        elif prompt_6 in ['WSW','wsw']:
            print
            den_sw ()
        else:
            print '...'
            print
            den ()
    except ValueError:
        print '...'
        print
        den ()

def inventory_p_6 ():
    list1 = ['Flash Light', 'Bolt Cutters', 'Ghost Box']
    for l1 in sorted(set(list1)):
        print l1
        print
    prompt_i_3 = raw_input ('Use: ')
    try:
        if prompt_i_3 in ['Bolt Cutters','bolt cutters']:
            print " You don't need this right now."
            print
            inventory_p_6 ()
        elif prompt_7_1 in ['Flash Light','flash light']:
            print 'In Use'
            print
            den ()
        elif prompt_i_3 in ['Ghost Box','ghost box']:
            print
            ghost_box_3 ()
        elif prompt_i_3 in ['Exit','exit']:
            print
            den ()
        else:
            print '...'
            print
            inventory_p_6 ()
    except ValueError:
        print '...'
        print
        inventory_p_6 ()

def ghost_box_3 ():
    print'          \\\\\\\\\\\\\\\\\\\\\                                                                      ///////////'
    print'       \                \                                                               /               /'
    print'     \                    \                                                           /                    /'
    print'    \                      \                 /^^^^^^^^^^^^^^^^^^^^^\                 /                      /'
    print'     \                    \       /\/\     /  /-------------------\  \     /\/\       /                    /'
    print'       \                 /      /\/\/\/\  /  /____|________________\  \  /\/\/\/\      \                 /'
    print'        /\/\/\/\/\/\/\/\/\ ___/\/\/\/\/\/\|___________________________|/\/\/\/\/\/\___ /\/\/\/\/\/\/\/\/\\'
    print'       ( -------------- ) /               \-(O)         O         (O) /               \ ( -------------- )'
    print'       ( -------------- )(          0      \        H       S        /      0          )( -------------- )'
    print'       ( ------------- ) ( |||  0  000  0   \   G       o       T   /   0  000  0  ||| ) ( ------------- )'
    print'        \ ----------- /  ( ||| 000 000 000   |      o  ooo  o      |   000 000 000 ||| )  \ ----------- /'
    print'         |  |  |  |  |   ( ||| 000 000 000   |  o  ooo *o  ooo  o  |   000 000 000 ||| )   |  |  |  |  |'
    print'         |  |  |  |  |   ( ||| 000 000 000   | ooo *o      *o  ooo |   000 000 000 ||| )   |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   | *o              *o  |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |    \    000 000 000   |                     |   000 000 000    /    |  |  |  |  |'
    print'         |  |  |  |  |     (   000 000 000   |                     |   000 000 000   )     |  |  |  |  |'
    print'         |  |  |  |  |    (    000 000 000   |   \  /\/\/\/\  /    |   000 000 000    )    |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   |  ( \/        \/ )   |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |  (      000 000 000   | (                )  |   000 000 000      )  |  |  |  |  |'
    print'         |  |  |  |  |  (      000 000 000   | (                )  |   000 000 000      )  |  |  |  |  |'
    print'         |  |  |  |  |  (      000 000 000   |  ( /\        /\ )   |   000 000 000      )  |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   |   /  \/\/\/\/  \    |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |    (    000 000 000   |                     |   000 000 000    )    |  |  |  |  |'
    print'         |  |  |  |  |     (   000 000 000   |      o       o      |   000 000 000   )     |  |  |  |  |'
    print'         |  |  |  |  |    /    000 000 000   |      o   o   o      |   000 000 000    \    |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   |     ooo  o  ooo     |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |   ( ||| 000 000 000   |      o  ooo  o      |   000 000 000 ||| )   |  |  |  |  |'
    print'        / ----------- \  ( ||| 000 000 000   |          o          |   000 000 000 ||| )  / ----------- \\'
    print'       ( ------------- ) ( ||| 000 000 000   |      B       X      |   000 000 000 ||| ) ( ------------- )'
    print'       ( -------------- )( |||  0  000  0   /           O           \   0  000  0  ||| )( -------------- )'
    print'       ( -------------- )(          0      /                         \      0          )( -------------- )'
    print'        \/\/\/\/\/\/\/\/\/\_______________/___________________________\_______________/\/\/\/\/\/\/\/\/\/'
    prompt_gb_3 = raw_input ('Turn on Ghost Box? [Y/N]: ')
    try:
        if prompt_gb_3 in ['Y','y']:
            print
            ghost_box_module_3 ()
        elif prompt_gb_3 in ['N','n']:
            print
            ghost_box_a_3 ()
        else:
            print '...'
            print
            ghost_box_3 ()
    except ValueError:
        print '...'
        print
        ghost_box_3 ()

def ghost_box_a_3 ():
    prompt_gb_a_3 = raw_input ('Put ghost box away? [Y/N]: ')
    try:
        if prompt_gb_a_3 in ['Y','y']:
            print
            inventory_p_6 ()
        elif prompt_gb_a_3 in ['N','n']:
            print
            ghost_box_3 ()
        else:
            print '...'
            print
            ghost_box_a_3 ()
    except ValueError:
        print '...'
        print
        ghost_box_a_3 ()

def ghost_box_module_3 ():
    print'          \\\\\\\\\\\\\\\\\\\\\                                                                      ///////////'
    print'       \                \                                                               /               /'
    print'     \                    \                                                           /                    /'
    print'    \                      \                 /^^^^^^^^^^^^^^^^^^^^^\                 /                      /'
    print'     \                    \       /\/\     /  /-------------------\  \     /\/\       /                    /'
    print'       \                 /      /\/\/\/\  /  /____|________________\  \  /\/\/\/\      \                 /'
    print'        /\/\/\/\/\/\/\/\/\ ___/\/\/\/\/\/\|___________________________|/\/\/\/\/\/\___ /\/\/\/\/\/\/\/\/\\'
    print'       ( -------------- ) /               \ (O)-        O         (O) /               \ ( -------------- )'
    print'       ( -------------- )(          0      \        H       S        /      0          )( -------------- )'
    print'       ( ------------- ) ( |||  0  000  0   \   G       o       T   /   0  000  0  ||| ) ( ------------- )'
    print'        \ ----------- /  ( ||| 000 000 000   |      o  ooo  o      |   000 000 000 ||| )  \ ----------- /'
    print'         |  |  |  |  |   ( ||| 000 000 000   |  o  ooo *o  ooo  o  |   000 000 000 ||| )   |  |  |  |  |'
    print'         |  |  |  |  |   ( ||| 000 000 000   | ooo *o      *o  ooo |   000 000 000 ||| )   |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   | *o              *o  |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |    \    000 000 000   |                     |   000 000 000    /    |  |  |  |  |'
    print'         |  |  |  |  |     (   000 000 000   |                     |   000 000 000   )     |  |  |  |  |'
    print'         |  |  |  |  |    (    000 000 000   |   \  /\/\/\/\  /    |   000 000 000    )    |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   |  ( \/        \/ )   |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |  (      000 000 000   | ( |-||- |_ |_ () )  |   000 000 000      )  |  |  |  |  |'
    print'         |  |  |  |  |  (      000 000 000   | ( -------------- )  |   000 000 000      )  |  |  |  |  |'
    print'         |  |  |  |  |  (      000 000 000   |  ( /\        /\ )   |   000 000 000      )  |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   |   /  \/\/\/\/  \    |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |    (    000 000 000   |                     |   000 000 000    )    |  |  |  |  |'
    print'         |  |  |  |  |     (   000 000 000   |      o       o      |   000 000 000   )     |  |  |  |  |'
    print'         |  |  |  |  |    /    000 000 000   |      o   o   o      |   000 000 000    \    |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   |     ooo  o  ooo     |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |   ( ||| 000 000 000   |      o  ooo  o      |   000 000 000 ||| )   |  |  |  |  |'
    print'        / ----------- \  ( ||| 000 000 000   |          o          |   000 000 000 ||| )  / ----------- \\'
    print'       ( ------------- ) ( ||| 000 000 000   |      B       X      |   000 000 000 ||| ) ( ------------- )'
    print'       ( -------------- )( |||  0  000  0   /           O           \   0  000  0  ||| )( -------------- )'
    print'       ( -------------- )(          0      /                         \      0          )( -------------- )'
    print'        \/\/\/\/\/\/\/\/\/\_______________/___________________________\_______________/\/\/\/\/\/\/\/\/\/'
    module = ['OFF', 'GHOST', 'Bal', 'Options', 'X-terminate']
    for m in sorted(set(module)):
        print m
        print
    prompt_gbm_3 = raw_input ('Select: ')
    try:
        if prompt_gbm_3 in ['OFF','Off','off']:
            print
            ghost_box_a_3 ()
        elif prompt_gbm_3 in ['GHOST','Ghost','ghost','G','g']:
            print
            GHOST_3 ()
        elif prompt_gbm_3 in ['Bal','bal','Balance','balance','B','b']:
            print
            Bal_3 ()
        elif prompt_gbm_3 in ['Options','options','O','o']:
            print
            Options_3 ()
        elif prompt_gbm_3 in ['X-terminate','x-terminate','X','x']:
            print
            X-terminate_3 ()
        else:
            print '...'
            print
            ghost_box_module_3 ()
    except ValueError:
        print '...'
        print
        ghost_box_module_3 ()

def GHOST_3 ():
    print'          \\\\\\\\\\\\\\\\\\\\\                                                                      ///////////'
    print'       \                \                                                               /               /'
    print'     \                    \                                                           /                    /'
    print'    \                      \                 /^^^^^^^^^^^^^^^^^^^^^\                 /                      /'
    print'     \                    \       /\/\     /  /-------------------\  \     /\/\       /                    /'
    print'       \                 /      /\/\/\/\  /  /____|________________\  \  /\/\/\/\      \                 /'
    print'        /\/\/\/\/\/\/\/\/\ ___/\/\/\/\/\/\|___________________________|/\/\/\/\/\/\___ /\/\/\/\/\/\/\/\/\\'
    print'       ( -------------- ) /               \ (O)-        O         (O) /               \ ( -------------- )'
    print'       ( -------------- )(          0      \        H       S        /      0          )( -------------- )'
    print'       ( ------------- ) ( |||  0  000  0   \   G       o       T   /   0  000  0  ||| ) ( ------------- )'
    print'        \ ----------- /  ( ||| 000 000 000   |      o  ooo  o      |   000 000 000 ||| )  \ ----------- /'
    print'         |  |  |  |  |   ( ||| 000 000 000   |  o  ooo *o  ooo  o  |   000 000 000 ||| )   |  |  |  |  |'
    print'         |  |  |  |  |   ( ||| 000 000 000   | ooo *o      *o  ooo |   000 000 000 ||| )   |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   | *o              *o  |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |    \    000 000 000   |                     |   000 000 000    /    |  |  |  |  |'
    print'         |  |  |  |  |     (   000 000 000   |                     |   000 000 000   )     |  |  |  |  |'
    print'         |  |  |  |  |    (    000 000 000   |   \  /\/\/\/\  /    |   000 000 000    )    |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   |  ( \/        \/ )   |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |  (      000 000 000   | ( |-||- |_ |_ () )  |   000 000 000      )  |  |  |  |  |'
    print'         |  |  |  |  |  (      000 000 000   | ( -------------- )  |   000 000 000      )  |  |  |  |  |'
    print'         |  |  |  |  |  (      000 000 000   |  ( /\        /\ )   |   000 000 000      )  |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   |   /  \/\/\/\/  \    |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |    (    000 000 000   |                     |   000 000 000    )    |  |  |  |  |'
    print'         |  |  |  |  |     (   000 000 000   |      o       o      |   000 000 000   )     |  |  |  |  |'
    print'         |  |  |  |  |    /    000 000 000   |      o   o   o      |   000 000 000    \    |  |  |  |  |'
    print'         |  |  |  |  |   (     000 000 000   |     ooo  o  ooo     |   000 000 000     )   |  |  |  |  |'
    print'         |  |  |  |  |   ( ||| 000 000 000   |      o  ooo  o      |   000 000 000 ||| )   |  |  |  |  |'
    print'        / ----------- \  ( ||| 000 000 000   |          o          |   000 000 000 ||| )  / ----------- \\'
    print'       ( ------------- ) ( ||| 000 000 000   |      B       X      |   000 000 000 ||| ) ( ------------- )'
    print'       ( -------------- )( |||  0  000  0   /           O           \   0  000  0  ||| )( -------------- )'
    print'       ( -------------- )(          0      /                         \      0          )( -------------- )'
    print'        \/\/\/\/\/\/\/\/\/\_______________/___________________________\_______________/\/\/\/\/\/\/\/\/\/'
    prompt_ghost_3 = raw_input ('Turn each of the G, H, O, S, T knobs to desired value [5 numbers 1-7]: ')
    print ' There is no signal coming in at the moment.'
    print
    ghost_box_module_3 ()

def den_n ():
    prompt_dn = raw_input ('You are at the door. Type a command: ')
    try:
        if prompt_dn in ['Open Door','open door']:
            print 'The door is locked.'
            print
            den_n ()
        elif prompt_dn in ['BL','bl']:
            print '{||||}'
            print
            den_n ()
        elif prompt_dn in ['WE','we']:
            print
            crawl_space ()
        elif prompt_dn in ['WW','ww']:
            print
            den_nw ()
        elif prompt_dn in ['WS','ws']:
            print
            den ()
        elif prompt_dn == 'quit()':
            print
            quit()
        else:
            print '...'
            print
            den_n ()
    except ValueError:
        print '...'
        print
        den_n ()

def den_e ():
    prompt_de = raw_input ('You are at the door. Type a command.')
    try:
        if prompt_de in ['Open Door','open door']:
            print
            print
        elif prompt_de in ['BL','bl']:
            print '{||||}'
            print
            den_e ()
        elif prompt_de in ['WN','wn']:
            print
            den_ne ()
        elif prompt_de in ['WW','ww']:
            print
            den ()
        elif prompt_de == 'quit()':
            print
            quit()
        else:
            print '...'
            print
            den_e ()
    except ValueError:
        print '...'
        print
        den_e ()

def den_s ():
    prompt_ds = raw_input ('Exit house? [Y/N]: ')
    try:
        if prompt_ds in ['Y','y']:
            print "That's weird, the front door seems to be locked from the inside."
            print
            den ()
        elif prompt_ds in ['N','n']:
            print
            den ()
        else:
            print '...'
            print
            den_s ()
    except ValueError:
        print '...'
        print
        den_s ()

def den_w ():
    prompt_dw = raw_input ('Type a command: ')
    try:
        if prompt_dw in ['Examine Area','examine area']:
            print
            print
        elif prompt_dw in ['BL','bl']:
            print '{||||}'
            print
            den_w ()
        elif prompt_dw in ['WNW','wnw']:
            print
            den_w_nw ()
        elif prompt_dw in ['WN','wn']:
            print
            den_nw ()
        elif prompt_dw in ['WS','ws']:
            print
            den_sw ()
        elif prompt_dw in ['WE','we']:
            print
            den ()
        elif prompt_dw == 'quit()':
            print
            quit()
        else:
            print '...'
            print
            den_w ()
    except ValueError:
        print '...'
        print
        den_w ()

def den_ne ():
    prompt_dne = ('Go up stairs [Y/N]: ')
    try:
        if prompt_dne in ['Y','y']:
            print
            w_upstairs ()
        elif prompt_dne in ['N','n']:
            print
            den ()
        elif prompt_dne == 'quit()':
            print
            quit()
        else:
            print '...'
            print
            den_ne ()
    except ValueError:
        print '...'
        print
        den_ne ()

def den_nw ():
    prompt_dnw = ('Type a command: ')
    try:
        if prompt_dnw in ['Examine Area','examine area']:
            print
            print
        elif prompt_dnw in ['BL','bl']:
            print '{||||}'
            print
            den_nw ()
        elif prompt_dnw in ['WNW','wnw']:
            print
            den_w_nw ()
        elif prompt_dnw in ['WSW','wsw']:
            print
            den_w ()
        elif prompt_dnw in ['WS','ws']:
            print
            den_sw ()
        elif prompt_dnw in ['WE','we']:
            print
            den_n ()
        elif prompt_dnw in ['WSE','wse']:
            print
            den ()
        elif prompt_dnw == 'quit()':
            print
            quit()
        else:
            print '...'
            print
            den_nw ()
    except ValueError:
        print '...'
        print
        den_nw ()

def den_se ():
    prompt_dse = ('Type a command: ')
    try:
        if prompt_dse in ['Examine Area','examine area']:
            print
            print
        elif prompt_dse in ['LOW','low']:
            print
            print
        elif prompt_dse in ['BL','bl']:
            print '{||||}'
            print
            den_se ()
        elif prompt_dse in ['WN','wn']:
            print
            den_ne ()
        elif prompt_dse in ['WNE','wne']:
            print
            den_e ()
        elif prompt_dse == 'quit()':
            print
            quit()
        else:
            print '...'
            print
            den_se ()
    except ValueError:
        print '...'
        print
        den_se ()

def den_sw ():
    prompt_dsw = ('Type a command: ')
    try:
        if prompt_dsw in ['Examine Area','examine area']:
            print
            print
        elif prompt_dsw in ['LOW','low']:
            print
            print
        elif prompt_dsw in ['BL','bl']:
            print '{||||}'
            print
            den_sw ()
        elif prompt_dsw in ['WW','ww']:
            print
            den_w_sw ()
        elif prompt_dsw in ['WN','wn']:
            print
            den_nw ()
        elif prompt_dsw in ['WNW','wnw']:
            print
            den_w ()
        elif prompt_dsw in ['WNE','wne']:
            print
            den ()
        elif prompt_dsw == 'quit()':
            print
            quit()
        else:
            print '...'
            print
            den_sw ()
    except ValueError:
        print '...'
        print
        den_sw ()

def den_w_nw ():
    prompt_dw_nw = ('Type a command: ')
    try:
        if prompt_dw_nw in ['Open Door','open door']:
            print
            kitchen ()
        elif prompt_dw_nw in ['BL','bl']:
            print '{||||}'
            print
            den_w_nw ()
        elif prompt_dw_nw in ['WSE','wse']:
            print
            den_nw ()
        else:
            print '...'
            print
            den_w_nw ()
    except ValueError:
        print '...'
        print
        den_w_nw ()

def den_w_sw ():
    prompt_dw_sw = raw_input ('Type a command: ')
    try:
        if prompt_dw_sw in ['Open Door','open door']:
            print
            print
        elif prompt_dw_sw in ['BL','bl']:
            print '{||||}'
            print
            den_w_sw ()
        elif prompt_dw_sw in ['WNE','wne']:
            print
            den_w ()
        elif prompt_dw_sw in ['WE','we']:
            print
            den_sw ()
        elif prompt_dw_sw == 'quit()':
            print
            quit()
        else:
            print '...'
            print
            den_w_sw ()
    except ValueError:
        print '...'
        print
        den_w_sw ()

def kitchen ():
    prompt_k = ('You are now in the kitchen. Type a command: ')
    try:

start ()
