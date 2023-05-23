#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.1),
    on Tue May 23 16:52:40 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.1'
expName = 'detectEmotion'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/pratikbhandari/projects/emotionCheck/emotion-test/emotionCheck_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1352,878], fullscr=False, screen=0, 
    winType='pyglet', allowStencil=True,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = True
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "welcome" ---
intro = visual.TextStim(win=win, name='intro',
    text="Let's reflect on your emotions",
    font='Arial',
    units='norm', pos=(0, 0), height=0.09, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
textNext = visual.TextStim(win=win, name='textNext',
    text='>>',
    font='Open Sans',
    units='norm', pos=(0.88, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
mouseNext = event.Mouse(win=win)
x, y = [None, None]
mouseNext.mouseClock = core.Clock()

# --- Initialize components for Routine "instruction" ---
emoWheelIntro = visual.TextStim(win=win, name='emoWheelIntro',
    text='Click the word that best describes how you are feeling right now',
    font='Arial',
    units='norm', pos=(0, 0), height=0.09, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
textEmoNext = visual.TextStim(win=win, name='textEmoNext',
    text='>>',
    font='Open Sans',
    units='norm', pos=(0.88, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
mouseEmoNext = event.Mouse(win=win)
x, y = [None, None]
mouseEmoNext.mouseClock = core.Clock()
ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

# --- Initialize components for Routine "emotions" ---
Anger = visual.TextStim(win=win, name='Anger',
    text='Anger',
    font='Arial',
    units='norm', pos=(-0.1,.68), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Interest = visual.TextStim(win=win, name='Interest',
    text='Interest',
    font='Arial',
    units='norm', pos=(0.1,0.68), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Hate = visual.TextStim(win=win, name='Hate',
    text='Hate',
    font='Arial',
    units='norm', pos=(-0.2,0.52), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Amusement = visual.TextStim(win=win, name='Amusement',
    text='Amusement',
    font='Arial',
    units='norm', pos=(0.255,0.52), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
Contempt = visual.TextStim(win=win, name='Contempt',
    text='Contempt',
    font='Arial',
    units='norm', pos=(-0.3,0.36), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
Pride = visual.TextStim(win=win, name='Pride',
    text='Pride',
    font='Arial',
    units='norm', pos=(0.3,0.36), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
Disgust = visual.TextStim(win=win, name='Disgust',
    text='Disgust',
    font='Arial',
    units='norm', pos=(-0.4,0.2), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
Joy = visual.TextStim(win=win, name='Joy',
    text='Joy',
    font='Arial',
    units='norm', pos=(0.35,0.2), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
Fear = visual.TextStim(win=win, name='Fear',
    text='Fear',
    font='Arial',
    units='norm', pos=(-0.5,0.04), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
Pleasure = visual.TextStim(win=win, name='Pleasure',
    text='Pleasure',
    font='Arial',
    units='norm', pos=(0.45,0.04), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
Disappointment = visual.TextStim(win=win, name='Disappointment',
    text='Disappointment',
    font='Arial',
    units='norm', pos=(-0.65,-0.12), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
Contentment = visual.TextStim(win=win, name='Contentment',
    text='Contentment',
    font='Arial',
    units='norm', pos=(0.58,-0.12), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
Shame = visual.TextStim(win=win, name='Shame',
    text='Shame',
    font='Arial',
    units='norm', pos=(-0.5,-0.28), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-12.0);
Admiration = visual.TextStim(win=win, name='Admiration',
    text='Admiration',
    font='Arial',
    units='norm', pos=(0.48,-0.28), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-13.0);
Regret = visual.TextStim(win=win, name='Regret',
    text='Regret',
    font='Arial',
    units='norm', pos=(-0.38,-0.44), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-14.0);
Love = visual.TextStim(win=win, name='Love',
    text='Love',
    font='Arial',
    units='norm', pos=(0.38,-0.44), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-15.0);
Guilt = visual.TextStim(win=win, name='Guilt',
    text='Guilt',
    font='Arial',
    units='norm', pos=(-0.28,-0.6), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-16.0);
Relief = visual.TextStim(win=win, name='Relief',
    text='Relief',
    font='Arial',
    units='norm', pos=(0.28,-0.6), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-17.0);
Sadness = visual.TextStim(win=win, name='Sadness',
    text='Sadness',
    font='Arial',
    units='norm', pos=(-0.15,-0.76), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-18.0);
Compassion = visual.TextStim(win=win, name='Compassion',
    text='Compassion',
    font='Arial',
    units='norm', pos=(0.15,-0.76), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-19.0);
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
ISI_2 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_2')

# --- Initialize components for Routine "notes" ---
textNote = visual.TextBox2(
     win, text=None, placeholder='What makes you feel that way?', font='Arial',
     pos=(0, 0),units='norm',     letterHeight=0.0666,
     size=(1, 0.5), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0, speechPoint=None,
     padding=0.0, alignment='center',
     anchor='center', overflow='visible',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textNote',
     depth=0, autoLog=True,
)
textExit = visual.TextStim(win=win, name='textExit',
    text='>>',
    font='Open Sans',
    units='norm', pos=(0.88,0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
mouseExit = event.Mouse(win=win)
x, y = [None, None]
mouseExit.mouseClock = core.Clock()
ISI_3 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_3')

# --- Initialize components for Routine "bye" ---
text = visual.TextStim(win=win, name='text',
    text='Thank you for reflecting on your emotions',
    font='Open Sans',
    units='norm', pos=(0, 0), height=0.066, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "welcome" ---
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouseNext
    mouseNext.x = []
    mouseNext.y = []
    mouseNext.leftButton = []
    mouseNext.midButton = []
    mouseNext.rightButton = []
    mouseNext.time = []
    mouseNext.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    welcomeComponents = [intro, textNext, mouseNext]
    for thisComponent in welcomeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "welcome" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *intro* updates
        
        # if intro is starting this frame...
        if intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            intro.frameNStart = frameN  # exact frame index
            intro.tStart = t  # local t and not account for scr refresh
            intro.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(intro, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'intro.started')
            # update status
            intro.status = STARTED
            intro.setAutoDraw(True)
        
        # if intro is active this frame...
        if intro.status == STARTED:
            # update params
            pass
        
        # *textNext* updates
        
        # if textNext is starting this frame...
        if textNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textNext.frameNStart = frameN  # exact frame index
            textNext.tStart = t  # local t and not account for scr refresh
            textNext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textNext, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textNext.started')
            # update status
            textNext.status = STARTED
            textNext.setAutoDraw(True)
        
        # if textNext is active this frame...
        if textNext.status == STARTED:
            # update params
            pass
        # *mouseNext* updates
        
        # if mouseNext is starting this frame...
        if mouseNext.status == NOT_STARTED and t >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            mouseNext.frameNStart = frameN  # exact frame index
            mouseNext.tStart = t  # local t and not account for scr refresh
            mouseNext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouseNext, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouseNext.started', t)
            # update status
            mouseNext.status = STARTED
            mouseNext.mouseClock.reset()
            prevButtonState = mouseNext.getPressed()  # if button is down already this ISN'T a new click
        if mouseNext.status == STARTED:  # only update if started and not finished!
            buttons = mouseNext.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = core.getFromNames(textNext, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouseNext):
                            gotValidClick = True
                            mouseNext.clicked_name.append(obj.name)
                    if gotValidClick:
                        x, y = mouseNext.getPos()
                        mouseNext.x.append(x)
                        mouseNext.y.append(y)
                        buttons = mouseNext.getPressed()
                        mouseNext.leftButton.append(buttons[0])
                        mouseNext.midButton.append(buttons[1])
                        mouseNext.rightButton.append(buttons[2])
                        mouseNext.time.append(mouseNext.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in welcomeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "welcome" ---
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('mouseNext.x', mouseNext.x)
    trials.addData('mouseNext.y', mouseNext.y)
    trials.addData('mouseNext.leftButton', mouseNext.leftButton)
    trials.addData('mouseNext.midButton', mouseNext.midButton)
    trials.addData('mouseNext.rightButton', mouseNext.rightButton)
    trials.addData('mouseNext.time', mouseNext.time)
    trials.addData('mouseNext.clicked_name', mouseNext.clicked_name)
    # the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instruction" ---
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouseEmoNext
    mouseEmoNext.x = []
    mouseEmoNext.y = []
    mouseEmoNext.leftButton = []
    mouseEmoNext.midButton = []
    mouseEmoNext.rightButton = []
    mouseEmoNext.time = []
    mouseEmoNext.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    instructionComponents = [emoWheelIntro, textEmoNext, mouseEmoNext, ISI]
    for thisComponent in instructionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instruction" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *emoWheelIntro* updates
        
        # if emoWheelIntro is starting this frame...
        if emoWheelIntro.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            emoWheelIntro.frameNStart = frameN  # exact frame index
            emoWheelIntro.tStart = t  # local t and not account for scr refresh
            emoWheelIntro.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(emoWheelIntro, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'emoWheelIntro.started')
            # update status
            emoWheelIntro.status = STARTED
            emoWheelIntro.setAutoDraw(True)
        
        # if emoWheelIntro is active this frame...
        if emoWheelIntro.status == STARTED:
            # update params
            pass
        
        # *textEmoNext* updates
        
        # if textEmoNext is starting this frame...
        if textEmoNext.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            textEmoNext.frameNStart = frameN  # exact frame index
            textEmoNext.tStart = t  # local t and not account for scr refresh
            textEmoNext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textEmoNext, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textEmoNext.started')
            # update status
            textEmoNext.status = STARTED
            textEmoNext.setAutoDraw(True)
        
        # if textEmoNext is active this frame...
        if textEmoNext.status == STARTED:
            # update params
            pass
        # *mouseEmoNext* updates
        
        # if mouseEmoNext is starting this frame...
        if mouseEmoNext.status == NOT_STARTED and t >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            mouseEmoNext.frameNStart = frameN  # exact frame index
            mouseEmoNext.tStart = t  # local t and not account for scr refresh
            mouseEmoNext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouseEmoNext, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouseEmoNext.started', t)
            # update status
            mouseEmoNext.status = STARTED
            mouseEmoNext.mouseClock.reset()
            prevButtonState = mouseEmoNext.getPressed()  # if button is down already this ISN'T a new click
        if mouseEmoNext.status == STARTED:  # only update if started and not finished!
            buttons = mouseEmoNext.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = core.getFromNames(textEmoNext, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouseEmoNext):
                            gotValidClick = True
                            mouseEmoNext.clicked_name.append(obj.name)
                    if gotValidClick:
                        x, y = mouseEmoNext.getPos()
                        mouseEmoNext.x.append(x)
                        mouseEmoNext.y.append(y)
                        buttons = mouseEmoNext.getPressed()
                        mouseEmoNext.leftButton.append(buttons[0])
                        mouseEmoNext.midButton.append(buttons[1])
                        mouseEmoNext.rightButton.append(buttons[2])
                        mouseEmoNext.time.append(mouseEmoNext.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        # *ISI* period
        
        # if ISI is starting this frame...
        if ISI.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI.frameNStart = frameN  # exact frame index
            ISI.tStart = t  # local t and not account for scr refresh
            ISI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
            # update status
            ISI.status = STARTED
            ISI.start(0.2)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            ISI.complete()  # finish the static period
            ISI.tStop = ISI.tStart + 0.2  # record stop time
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instruction" ---
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('mouseEmoNext.x', mouseEmoNext.x)
    trials.addData('mouseEmoNext.y', mouseEmoNext.y)
    trials.addData('mouseEmoNext.leftButton', mouseEmoNext.leftButton)
    trials.addData('mouseEmoNext.midButton', mouseEmoNext.midButton)
    trials.addData('mouseEmoNext.rightButton', mouseEmoNext.rightButton)
    trials.addData('mouseEmoNext.time', mouseEmoNext.time)
    trials.addData('mouseEmoNext.clicked_name', mouseEmoNext.clicked_name)
    # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "emotions" ---
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    emotionsComponents = [Anger, Interest, Hate, Amusement, Contempt, Pride, Disgust, Joy, Fear, Pleasure, Disappointment, Contentment, Shame, Admiration, Regret, Love, Guilt, Relief, Sadness, Compassion, mouse, ISI_2]
    for thisComponent in emotionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "emotions" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Anger* updates
        
        # if Anger is starting this frame...
        if Anger.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            Anger.frameNStart = frameN  # exact frame index
            Anger.tStart = t  # local t and not account for scr refresh
            Anger.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Anger, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Anger.started')
            # update status
            Anger.status = STARTED
            Anger.setAutoDraw(True)
        
        # if Anger is active this frame...
        if Anger.status == STARTED:
            # update params
            pass
        
        # *Interest* updates
        
        # if Interest is starting this frame...
        if Interest.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            Interest.frameNStart = frameN  # exact frame index
            Interest.tStart = t  # local t and not account for scr refresh
            Interest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Interest, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Interest.started')
            # update status
            Interest.status = STARTED
            Interest.setAutoDraw(True)
        
        # if Interest is active this frame...
        if Interest.status == STARTED:
            # update params
            pass
        
        # *Hate* updates
        
        # if Hate is starting this frame...
        if Hate.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            Hate.frameNStart = frameN  # exact frame index
            Hate.tStart = t  # local t and not account for scr refresh
            Hate.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Hate, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Hate.started')
            # update status
            Hate.status = STARTED
            Hate.setAutoDraw(True)
        
        # if Hate is active this frame...
        if Hate.status == STARTED:
            # update params
            pass
        
        # *Amusement* updates
        
        # if Amusement is starting this frame...
        if Amusement.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            Amusement.frameNStart = frameN  # exact frame index
            Amusement.tStart = t  # local t and not account for scr refresh
            Amusement.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Amusement, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Amusement.started')
            # update status
            Amusement.status = STARTED
            Amusement.setAutoDraw(True)
        
        # if Amusement is active this frame...
        if Amusement.status == STARTED:
            # update params
            pass
        
        # *Contempt* updates
        
        # if Contempt is starting this frame...
        if Contempt.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            Contempt.frameNStart = frameN  # exact frame index
            Contempt.tStart = t  # local t and not account for scr refresh
            Contempt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Contempt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Contempt.started')
            # update status
            Contempt.status = STARTED
            Contempt.setAutoDraw(True)
        
        # if Contempt is active this frame...
        if Contempt.status == STARTED:
            # update params
            pass
        
        # *Pride* updates
        
        # if Pride is starting this frame...
        if Pride.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            Pride.frameNStart = frameN  # exact frame index
            Pride.tStart = t  # local t and not account for scr refresh
            Pride.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pride, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Pride.started')
            # update status
            Pride.status = STARTED
            Pride.setAutoDraw(True)
        
        # if Pride is active this frame...
        if Pride.status == STARTED:
            # update params
            pass
        
        # *Disgust* updates
        
        # if Disgust is starting this frame...
        if Disgust.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            Disgust.frameNStart = frameN  # exact frame index
            Disgust.tStart = t  # local t and not account for scr refresh
            Disgust.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Disgust, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Disgust.started')
            # update status
            Disgust.status = STARTED
            Disgust.setAutoDraw(True)
        
        # if Disgust is active this frame...
        if Disgust.status == STARTED:
            # update params
            pass
        
        # *Joy* updates
        
        # if Joy is starting this frame...
        if Joy.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            Joy.frameNStart = frameN  # exact frame index
            Joy.tStart = t  # local t and not account for scr refresh
            Joy.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Joy, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Joy.started')
            # update status
            Joy.status = STARTED
            Joy.setAutoDraw(True)
        
        # if Joy is active this frame...
        if Joy.status == STARTED:
            # update params
            pass
        
        # *Fear* updates
        
        # if Fear is starting this frame...
        if Fear.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            Fear.frameNStart = frameN  # exact frame index
            Fear.tStart = t  # local t and not account for scr refresh
            Fear.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fear, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Fear.started')
            # update status
            Fear.status = STARTED
            Fear.setAutoDraw(True)
        
        # if Fear is active this frame...
        if Fear.status == STARTED:
            # update params
            pass
        
        # *Pleasure* updates
        
        # if Pleasure is starting this frame...
        if Pleasure.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            Pleasure.frameNStart = frameN  # exact frame index
            Pleasure.tStart = t  # local t and not account for scr refresh
            Pleasure.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pleasure, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Pleasure.started')
            # update status
            Pleasure.status = STARTED
            Pleasure.setAutoDraw(True)
        
        # if Pleasure is active this frame...
        if Pleasure.status == STARTED:
            # update params
            pass
        
        # *Disappointment* updates
        
        # if Disappointment is starting this frame...
        if Disappointment.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            Disappointment.frameNStart = frameN  # exact frame index
            Disappointment.tStart = t  # local t and not account for scr refresh
            Disappointment.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Disappointment, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Disappointment.started')
            # update status
            Disappointment.status = STARTED
            Disappointment.setAutoDraw(True)
        
        # if Disappointment is active this frame...
        if Disappointment.status == STARTED:
            # update params
            pass
        
        # *Contentment* updates
        
        # if Contentment is starting this frame...
        if Contentment.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            Contentment.frameNStart = frameN  # exact frame index
            Contentment.tStart = t  # local t and not account for scr refresh
            Contentment.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Contentment, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Contentment.started')
            # update status
            Contentment.status = STARTED
            Contentment.setAutoDraw(True)
        
        # if Contentment is active this frame...
        if Contentment.status == STARTED:
            # update params
            pass
        
        # *Shame* updates
        
        # if Shame is starting this frame...
        if Shame.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            Shame.frameNStart = frameN  # exact frame index
            Shame.tStart = t  # local t and not account for scr refresh
            Shame.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Shame, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Shame.started')
            # update status
            Shame.status = STARTED
            Shame.setAutoDraw(True)
        
        # if Shame is active this frame...
        if Shame.status == STARTED:
            # update params
            pass
        
        # *Admiration* updates
        
        # if Admiration is starting this frame...
        if Admiration.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            Admiration.frameNStart = frameN  # exact frame index
            Admiration.tStart = t  # local t and not account for scr refresh
            Admiration.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Admiration, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Admiration.started')
            # update status
            Admiration.status = STARTED
            Admiration.setAutoDraw(True)
        
        # if Admiration is active this frame...
        if Admiration.status == STARTED:
            # update params
            pass
        
        # *Regret* updates
        
        # if Regret is starting this frame...
        if Regret.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            Regret.frameNStart = frameN  # exact frame index
            Regret.tStart = t  # local t and not account for scr refresh
            Regret.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Regret, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Regret.started')
            # update status
            Regret.status = STARTED
            Regret.setAutoDraw(True)
        
        # if Regret is active this frame...
        if Regret.status == STARTED:
            # update params
            pass
        
        # *Love* updates
        
        # if Love is starting this frame...
        if Love.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            Love.frameNStart = frameN  # exact frame index
            Love.tStart = t  # local t and not account for scr refresh
            Love.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Love, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Love.started')
            # update status
            Love.status = STARTED
            Love.setAutoDraw(True)
        
        # if Love is active this frame...
        if Love.status == STARTED:
            # update params
            pass
        
        # *Guilt* updates
        
        # if Guilt is starting this frame...
        if Guilt.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            Guilt.frameNStart = frameN  # exact frame index
            Guilt.tStart = t  # local t and not account for scr refresh
            Guilt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Guilt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Guilt.started')
            # update status
            Guilt.status = STARTED
            Guilt.setAutoDraw(True)
        
        # if Guilt is active this frame...
        if Guilt.status == STARTED:
            # update params
            pass
        
        # *Relief* updates
        
        # if Relief is starting this frame...
        if Relief.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            Relief.frameNStart = frameN  # exact frame index
            Relief.tStart = t  # local t and not account for scr refresh
            Relief.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Relief, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Relief.started')
            # update status
            Relief.status = STARTED
            Relief.setAutoDraw(True)
        
        # if Relief is active this frame...
        if Relief.status == STARTED:
            # update params
            pass
        
        # *Sadness* updates
        
        # if Sadness is starting this frame...
        if Sadness.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            Sadness.frameNStart = frameN  # exact frame index
            Sadness.tStart = t  # local t and not account for scr refresh
            Sadness.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Sadness, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Sadness.started')
            # update status
            Sadness.status = STARTED
            Sadness.setAutoDraw(True)
        
        # if Sadness is active this frame...
        if Sadness.status == STARTED:
            # update params
            pass
        
        # *Compassion* updates
        
        # if Compassion is starting this frame...
        if Compassion.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            Compassion.frameNStart = frameN  # exact frame index
            Compassion.tStart = t  # local t and not account for scr refresh
            Compassion.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Compassion, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Compassion.started')
            # update status
            Compassion.status = STARTED
            Compassion.setAutoDraw(True)
        
        # if Compassion is active this frame...
        if Compassion.status == STARTED:
            # update params
            pass
        # *mouse* updates
        
        # if mouse is starting this frame...
        if mouse.status == NOT_STARTED and t >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse.started', t)
            # update status
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = core.getFromNames([Hate, Interest, Anger, Amusement, Contempt, Pride, Disgust, Joy, Fear, Pleasure, Disappointment, Contentment, Shame, Admiration, Regret, Love, Guilt, Relief, Sadness, Compassion], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    if gotValidClick:
                        x, y = mouse.getPos()
                        mouse.x.append(x)
                        mouse.y.append(y)
                        buttons = mouse.getPressed()
                        mouse.leftButton.append(buttons[0])
                        mouse.midButton.append(buttons[1])
                        mouse.rightButton.append(buttons[2])
                        mouse.time.append(mouse.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        # *ISI_2* period
        
        # if ISI_2 is starting this frame...
        if ISI_2.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            ISI_2.frameNStart = frameN  # exact frame index
            ISI_2.tStart = t  # local t and not account for scr refresh
            ISI_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            ISI_2.status = STARTED
            ISI_2.start(0.2)
        elif ISI_2.status == STARTED:  # one frame should pass before updating params and completing
            ISI_2.complete()  # finish the static period
            ISI_2.tStop = ISI_2.tStart + 0.2  # record stop time
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in emotionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "emotions" ---
    for thisComponent in emotionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('mouse.x', mouse.x)
    trials.addData('mouse.y', mouse.y)
    trials.addData('mouse.leftButton', mouse.leftButton)
    trials.addData('mouse.midButton', mouse.midButton)
    trials.addData('mouse.rightButton', mouse.rightButton)
    trials.addData('mouse.time', mouse.time)
    trials.addData('mouse.clicked_name', mouse.clicked_name)
    # the Routine "emotions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "notes" ---
    continueRoutine = True
    # update component parameters for each repeat
    textNote.reset()
    # setup some python lists for storing info about the mouseExit
    mouseExit.x = []
    mouseExit.y = []
    mouseExit.leftButton = []
    mouseExit.midButton = []
    mouseExit.rightButton = []
    mouseExit.time = []
    mouseExit.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    notesComponents = [textNote, textExit, mouseExit, ISI_3]
    for thisComponent in notesComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "notes" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textNote* updates
        
        # if textNote is starting this frame...
        if textNote.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            textNote.frameNStart = frameN  # exact frame index
            textNote.tStart = t  # local t and not account for scr refresh
            textNote.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textNote, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textNote.started')
            # update status
            textNote.status = STARTED
            textNote.setAutoDraw(True)
        
        # if textNote is active this frame...
        if textNote.status == STARTED:
            # update params
            pass
        
        # *textExit* updates
        
        # if textExit is starting this frame...
        if textExit.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            textExit.frameNStart = frameN  # exact frame index
            textExit.tStart = t  # local t and not account for scr refresh
            textExit.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textExit, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textExit.started')
            # update status
            textExit.status = STARTED
            textExit.setAutoDraw(True)
        
        # if textExit is active this frame...
        if textExit.status == STARTED:
            # update params
            pass
        # *mouseExit* updates
        
        # if mouseExit is starting this frame...
        if mouseExit.status == NOT_STARTED and t >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            mouseExit.frameNStart = frameN  # exact frame index
            mouseExit.tStart = t  # local t and not account for scr refresh
            mouseExit.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouseExit, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouseExit.started', t)
            # update status
            mouseExit.status = STARTED
            mouseExit.mouseClock.reset()
            prevButtonState = mouseExit.getPressed()  # if button is down already this ISN'T a new click
        if mouseExit.status == STARTED:  # only update if started and not finished!
            buttons = mouseExit.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = core.getFromNames(textExit, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouseExit):
                            gotValidClick = True
                            mouseExit.clicked_name.append(obj.name)
                    if gotValidClick:
                        x, y = mouseExit.getPos()
                        mouseExit.x.append(x)
                        mouseExit.y.append(y)
                        buttons = mouseExit.getPressed()
                        mouseExit.leftButton.append(buttons[0])
                        mouseExit.midButton.append(buttons[1])
                        mouseExit.rightButton.append(buttons[2])
                        mouseExit.time.append(mouseExit.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        # *ISI_3* period
        
        # if ISI_3 is starting this frame...
        if ISI_3.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            ISI_3.frameNStart = frameN  # exact frame index
            ISI_3.tStart = t  # local t and not account for scr refresh
            ISI_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            ISI_3.status = STARTED
            ISI_3.start(0.2)
        elif ISI_3.status == STARTED:  # one frame should pass before updating params and completing
            ISI_3.complete()  # finish the static period
            ISI_3.tStop = ISI_3.tStart + 0.2  # record stop time
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in notesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "notes" ---
    for thisComponent in notesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('textNote.text',textNote.text)
    # store data for trials (TrialHandler)
    trials.addData('mouseExit.x', mouseExit.x)
    trials.addData('mouseExit.y', mouseExit.y)
    trials.addData('mouseExit.leftButton', mouseExit.leftButton)
    trials.addData('mouseExit.midButton', mouseExit.midButton)
    trials.addData('mouseExit.rightButton', mouseExit.rightButton)
    trials.addData('mouseExit.time', mouseExit.time)
    trials.addData('mouseExit.clicked_name', mouseExit.clicked_name)
    # the Routine "notes" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "bye" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    byeComponents = [text]
    for thisComponent in byeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "bye" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 4.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # if text is stopping this frame...
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.stopped')
                # update status
                text.status = FINISHED
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in byeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "bye" ---
    for thisComponent in byeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-4.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
