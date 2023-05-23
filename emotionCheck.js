/********************* 
 * Emotioncheck Test *
 *********************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2023.1.1.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'emotionCheck';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: false,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2023.1.1';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);


  return Scheduler.Event.NEXT;
}


var welcomeClock;
var intro;
var textNext;
var mouseNext;
var instructionClock;
var emoWheelIntro;
var textEmoNext;
var mouseEmoNext;
var ISI;
var emotionsClock;
var Anger;
var Interest;
var Hate;
var Amusement;
var Contempt;
var Pride;
var Disgust;
var Joy;
var Fear;
var Pleasure;
var Disappointment;
var Contentment;
var Shame;
var Admiration;
var Regret;
var Love;
var Guilt;
var Relief;
var Sadness;
var Compassion;
var mouse;
var ISI_2;
var notesClock;
var textNote;
var textExit;
var mouseExit;
var ISI_3;
var byeClock;
var text;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "welcome"
  welcomeClock = new util.Clock();
  intro = new visual.TextStim({
    win: psychoJS.window,
    name: 'intro',
    text: "Let's reflect on your emotions",
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.09,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  textNext = new visual.TextStim({
    win: psychoJS.window,
    name: 'textNext',
    text: '>>',
    font: 'Open Sans',
    units: 'norm', 
    pos: [0.88, 0], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  mouseNext = new core.Mouse({
    win: psychoJS.window,
  });
  mouseNext.mouseClock = new util.Clock();
  // Initialize components for Routine "instruction"
  instructionClock = new util.Clock();
  emoWheelIntro = new visual.TextStim({
    win: psychoJS.window,
    name: 'emoWheelIntro',
    text: 'Click the word that best describes how you are feeling right now',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.09,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  textEmoNext = new visual.TextStim({
    win: psychoJS.window,
    name: 'textEmoNext',
    text: '>>',
    font: 'Open Sans',
    units: 'norm', 
    pos: [0.88, 0], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  mouseEmoNext = new core.Mouse({
    win: psychoJS.window,
  });
  mouseEmoNext.mouseClock = new util.Clock();
  ISI = new core.MinimalStim({
    name: "ISI", 
    win: psychoJS.window,
    autoDraw: false, 
    autoLog: true, 
  });
  // Initialize components for Routine "emotions"
  emotionsClock = new util.Clock();
  Anger = new visual.TextStim({
    win: psychoJS.window,
    name: 'Anger',
    text: 'Anger',
    font: 'Arial',
    units: 'norm', 
    pos: [(- 0.1), 0.68], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Interest = new visual.TextStim({
    win: psychoJS.window,
    name: 'Interest',
    text: 'Interest',
    font: 'Arial',
    units: 'norm', 
    pos: [0.1, 0.68], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  Hate = new visual.TextStim({
    win: psychoJS.window,
    name: 'Hate',
    text: 'Hate',
    font: 'Arial',
    units: 'norm', 
    pos: [(- 0.2), 0.52], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  Amusement = new visual.TextStim({
    win: psychoJS.window,
    name: 'Amusement',
    text: 'Amusement',
    font: 'Arial',
    units: 'norm', 
    pos: [0.255, 0.52], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  Contempt = new visual.TextStim({
    win: psychoJS.window,
    name: 'Contempt',
    text: 'Contempt',
    font: 'Arial',
    units: 'norm', 
    pos: [(- 0.3), 0.36], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  Pride = new visual.TextStim({
    win: psychoJS.window,
    name: 'Pride',
    text: 'Pride',
    font: 'Arial',
    units: 'norm', 
    pos: [0.3, 0.36], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -5.0 
  });
  
  Disgust = new visual.TextStim({
    win: psychoJS.window,
    name: 'Disgust',
    text: 'Disgust',
    font: 'Arial',
    units: 'norm', 
    pos: [(- 0.4), 0.2], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -6.0 
  });
  
  Joy = new visual.TextStim({
    win: psychoJS.window,
    name: 'Joy',
    text: 'Joy',
    font: 'Arial',
    units: 'norm', 
    pos: [0.35, 0.2], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -7.0 
  });
  
  Fear = new visual.TextStim({
    win: psychoJS.window,
    name: 'Fear',
    text: 'Fear',
    font: 'Arial',
    units: 'norm', 
    pos: [(- 0.5), 0.04], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -8.0 
  });
  
  Pleasure = new visual.TextStim({
    win: psychoJS.window,
    name: 'Pleasure',
    text: 'Pleasure',
    font: 'Arial',
    units: 'norm', 
    pos: [0.45, 0.04], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -9.0 
  });
  
  Disappointment = new visual.TextStim({
    win: psychoJS.window,
    name: 'Disappointment',
    text: 'Disappointment',
    font: 'Arial',
    units: 'norm', 
    pos: [(- 0.65), (- 0.12)], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -10.0 
  });
  
  Contentment = new visual.TextStim({
    win: psychoJS.window,
    name: 'Contentment',
    text: 'Contentment',
    font: 'Arial',
    units: 'norm', 
    pos: [0.58, (- 0.12)], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -11.0 
  });
  
  Shame = new visual.TextStim({
    win: psychoJS.window,
    name: 'Shame',
    text: 'Shame',
    font: 'Arial',
    units: 'norm', 
    pos: [(- 0.5), (- 0.28)], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -12.0 
  });
  
  Admiration = new visual.TextStim({
    win: psychoJS.window,
    name: 'Admiration',
    text: 'Admiration',
    font: 'Arial',
    units: 'norm', 
    pos: [0.48, (- 0.28)], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -13.0 
  });
  
  Regret = new visual.TextStim({
    win: psychoJS.window,
    name: 'Regret',
    text: 'Regret',
    font: 'Arial',
    units: 'norm', 
    pos: [(- 0.38), (- 0.44)], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -14.0 
  });
  
  Love = new visual.TextStim({
    win: psychoJS.window,
    name: 'Love',
    text: 'Love',
    font: 'Arial',
    units: 'norm', 
    pos: [0.38, (- 0.44)], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -15.0 
  });
  
  Guilt = new visual.TextStim({
    win: psychoJS.window,
    name: 'Guilt',
    text: 'Guilt',
    font: 'Arial',
    units: 'norm', 
    pos: [(- 0.28), (- 0.6)], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -16.0 
  });
  
  Relief = new visual.TextStim({
    win: psychoJS.window,
    name: 'Relief',
    text: 'Relief',
    font: 'Arial',
    units: 'norm', 
    pos: [0.28, (- 0.6)], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -17.0 
  });
  
  Sadness = new visual.TextStim({
    win: psychoJS.window,
    name: 'Sadness',
    text: 'Sadness',
    font: 'Arial',
    units: 'norm', 
    pos: [(- 0.15), (- 0.76)], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -18.0 
  });
  
  Compassion = new visual.TextStim({
    win: psychoJS.window,
    name: 'Compassion',
    text: 'Compassion',
    font: 'Arial',
    units: 'norm', 
    pos: [0.15, (- 0.76)], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -19.0 
  });
  
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  ISI_2 = new core.MinimalStim({
    name: "ISI_2", 
    win: psychoJS.window,
    autoDraw: false, 
    autoLog: true, 
  });
  // Initialize components for Routine "notes"
  notesClock = new util.Clock();
  textNote = new visual.TextBox({
    win: psychoJS.window,
    name: 'textNote',
    text: '',
    placeholder: 'What makes you feel that way?',
    font: 'Arial',
    pos: [0, 0], 
    letterHeight: 0.0666,
    lineSpacing: 1.0,
    size: [1, 0.5],  units: 'norm', 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  textExit = new visual.TextStim({
    win: psychoJS.window,
    name: 'textExit',
    text: '>>',
    font: 'Open Sans',
    units: 'norm', 
    pos: [0.88, 0], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  mouseExit = new core.Mouse({
    win: psychoJS.window,
  });
  mouseExit.mouseClock = new util.Clock();
  ISI_3 = new core.MinimalStim({
    name: "ISI_3", 
    win: psychoJS.window,
    autoDraw: false, 
    autoLog: true, 
  });
  // Initialize components for Routine "bye"
  byeClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Thank you for reflecting on your emotions',
    font: 'Open Sans',
    units: 'norm', 
    pos: [0, 0], height: 0.066,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(welcomeRoutineBegin(snapshot));
      trialsLoopScheduler.add(welcomeRoutineEachFrame());
      trialsLoopScheduler.add(welcomeRoutineEnd(snapshot));
      trialsLoopScheduler.add(instructionRoutineBegin(snapshot));
      trialsLoopScheduler.add(instructionRoutineEachFrame());
      trialsLoopScheduler.add(instructionRoutineEnd(snapshot));
      trialsLoopScheduler.add(emotionsRoutineBegin(snapshot));
      trialsLoopScheduler.add(emotionsRoutineEachFrame());
      trialsLoopScheduler.add(emotionsRoutineEnd(snapshot));
      trialsLoopScheduler.add(notesRoutineBegin(snapshot));
      trialsLoopScheduler.add(notesRoutineEachFrame());
      trialsLoopScheduler.add(notesRoutineEnd(snapshot));
      trialsLoopScheduler.add(byeRoutineBegin(snapshot));
      trialsLoopScheduler.add(byeRoutineEachFrame());
      trialsLoopScheduler.add(byeRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var t;
var frameN;
var continueRoutine;
var gotValidClick;
var welcomeComponents;
function welcomeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'welcome' ---
    t = 0;
    welcomeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouseNext
    // current position of the mouse:
    mouseNext.x = [];
    mouseNext.y = [];
    mouseNext.leftButton = [];
    mouseNext.midButton = [];
    mouseNext.rightButton = [];
    mouseNext.time = [];
    mouseNext.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    welcomeComponents = [];
    welcomeComponents.push(intro);
    welcomeComponents.push(textNext);
    welcomeComponents.push(mouseNext);
    
    for (const thisComponent of welcomeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var prevButtonState;
var _mouseButtons;
var _mouseXYs;
function welcomeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'welcome' ---
    // get current time
    t = welcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *intro* updates
    if (t >= 0.0 && intro.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      intro.tStart = t;  // (not accounting for frame time here)
      intro.frameNStart = frameN;  // exact frame index
      
      intro.setAutoDraw(true);
    }

    
    // *textNext* updates
    if (t >= 0.0 && textNext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textNext.tStart = t;  // (not accounting for frame time here)
      textNext.frameNStart = frameN;  // exact frame index
      
      textNext.setAutoDraw(true);
    }

    // *mouseNext* updates
    if (t >= 0.5 && mouseNext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouseNext.tStart = t;  // (not accounting for frame time here)
      mouseNext.frameNStart = frameN;  // exact frame index
      
      mouseNext.status = PsychoJS.Status.STARTED;
      mouseNext.mouseClock.reset();
      prevButtonState = mouseNext.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouseNext.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouseNext.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [textNext]) {
            if (obj.contains(mouseNext)) {
              gotValidClick = true;
              mouseNext.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { 
            _mouseXYs = mouseNext.getPos();
            mouseNext.x.push(_mouseXYs[0]);
            mouseNext.y.push(_mouseXYs[1]);
            mouseNext.leftButton.push(_mouseButtons[0]);
            mouseNext.midButton.push(_mouseButtons[1]);
            mouseNext.rightButton.push(_mouseButtons[2]);
            mouseNext.time.push(mouseNext.mouseClock.getTime());
          }
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of welcomeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function welcomeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'welcome' ---
    for (const thisComponent of welcomeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouseNext.x) {  psychoJS.experiment.addData('mouseNext.x', mouseNext.x[0])};
    if (mouseNext.y) {  psychoJS.experiment.addData('mouseNext.y', mouseNext.y[0])};
    if (mouseNext.leftButton) {  psychoJS.experiment.addData('mouseNext.leftButton', mouseNext.leftButton[0])};
    if (mouseNext.midButton) {  psychoJS.experiment.addData('mouseNext.midButton', mouseNext.midButton[0])};
    if (mouseNext.rightButton) {  psychoJS.experiment.addData('mouseNext.rightButton', mouseNext.rightButton[0])};
    if (mouseNext.time) {  psychoJS.experiment.addData('mouseNext.time', mouseNext.time[0])};
    if (mouseNext.clicked_name) {  psychoJS.experiment.addData('mouseNext.clicked_name', mouseNext.clicked_name[0])};
    
    // the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var instructionComponents;
function instructionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instruction' ---
    t = 0;
    instructionClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouseEmoNext
    // current position of the mouse:
    mouseEmoNext.x = [];
    mouseEmoNext.y = [];
    mouseEmoNext.leftButton = [];
    mouseEmoNext.midButton = [];
    mouseEmoNext.rightButton = [];
    mouseEmoNext.time = [];
    mouseEmoNext.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    instructionComponents = [];
    instructionComponents.push(emoWheelIntro);
    instructionComponents.push(textEmoNext);
    instructionComponents.push(mouseEmoNext);
    instructionComponents.push(ISI);
    
    for (const thisComponent of instructionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function instructionRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instruction' ---
    // get current time
    t = instructionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *emoWheelIntro* updates
    if (t >= 0.2 && emoWheelIntro.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      emoWheelIntro.tStart = t;  // (not accounting for frame time here)
      emoWheelIntro.frameNStart = frameN;  // exact frame index
      
      emoWheelIntro.setAutoDraw(true);
    }

    
    // *textEmoNext* updates
    if (t >= 0.2 && textEmoNext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textEmoNext.tStart = t;  // (not accounting for frame time here)
      textEmoNext.frameNStart = frameN;  // exact frame index
      
      textEmoNext.setAutoDraw(true);
    }

    // *mouseEmoNext* updates
    if (t >= 0.5 && mouseEmoNext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouseEmoNext.tStart = t;  // (not accounting for frame time here)
      mouseEmoNext.frameNStart = frameN;  // exact frame index
      
      mouseEmoNext.status = PsychoJS.Status.STARTED;
      mouseEmoNext.mouseClock.reset();
      prevButtonState = mouseEmoNext.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouseEmoNext.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouseEmoNext.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [textEmoNext]) {
            if (obj.contains(mouseEmoNext)) {
              gotValidClick = true;
              mouseEmoNext.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { 
            _mouseXYs = mouseEmoNext.getPos();
            mouseEmoNext.x.push(_mouseXYs[0]);
            mouseEmoNext.y.push(_mouseXYs[1]);
            mouseEmoNext.leftButton.push(_mouseButtons[0]);
            mouseEmoNext.midButton.push(_mouseButtons[1]);
            mouseEmoNext.rightButton.push(_mouseButtons[2]);
            mouseEmoNext.time.push(mouseEmoNext.mouseClock.getTime());
          }
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    if (t >= 0.0 && ISI.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ISI.tStart = t;  // (not accounting for frame time here)
      ISI.frameNStart = frameN;  // exact frame index
      
      ISI.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 0.0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (ISI.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      ISI.status = PsychoJS.Status.FINISHED;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instructionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructionRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instruction' ---
    for (const thisComponent of instructionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouseEmoNext.x) {  psychoJS.experiment.addData('mouseEmoNext.x', mouseEmoNext.x[0])};
    if (mouseEmoNext.y) {  psychoJS.experiment.addData('mouseEmoNext.y', mouseEmoNext.y[0])};
    if (mouseEmoNext.leftButton) {  psychoJS.experiment.addData('mouseEmoNext.leftButton', mouseEmoNext.leftButton[0])};
    if (mouseEmoNext.midButton) {  psychoJS.experiment.addData('mouseEmoNext.midButton', mouseEmoNext.midButton[0])};
    if (mouseEmoNext.rightButton) {  psychoJS.experiment.addData('mouseEmoNext.rightButton', mouseEmoNext.rightButton[0])};
    if (mouseEmoNext.time) {  psychoJS.experiment.addData('mouseEmoNext.time', mouseEmoNext.time[0])};
    if (mouseEmoNext.clicked_name) {  psychoJS.experiment.addData('mouseEmoNext.clicked_name', mouseEmoNext.clicked_name[0])};
    
    // the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var emotionsComponents;
function emotionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'emotions' ---
    t = 0;
    emotionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse
    // current position of the mouse:
    mouse.x = [];
    mouse.y = [];
    mouse.leftButton = [];
    mouse.midButton = [];
    mouse.rightButton = [];
    mouse.time = [];
    mouse.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    emotionsComponents = [];
    emotionsComponents.push(Anger);
    emotionsComponents.push(Interest);
    emotionsComponents.push(Hate);
    emotionsComponents.push(Amusement);
    emotionsComponents.push(Contempt);
    emotionsComponents.push(Pride);
    emotionsComponents.push(Disgust);
    emotionsComponents.push(Joy);
    emotionsComponents.push(Fear);
    emotionsComponents.push(Pleasure);
    emotionsComponents.push(Disappointment);
    emotionsComponents.push(Contentment);
    emotionsComponents.push(Shame);
    emotionsComponents.push(Admiration);
    emotionsComponents.push(Regret);
    emotionsComponents.push(Love);
    emotionsComponents.push(Guilt);
    emotionsComponents.push(Relief);
    emotionsComponents.push(Sadness);
    emotionsComponents.push(Compassion);
    emotionsComponents.push(mouse);
    emotionsComponents.push(ISI_2);
    
    for (const thisComponent of emotionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function emotionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'emotions' ---
    // get current time
    t = emotionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Anger* updates
    if (t >= 0.2 && Anger.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Anger.tStart = t;  // (not accounting for frame time here)
      Anger.frameNStart = frameN;  // exact frame index
      
      Anger.setAutoDraw(true);
    }

    
    // *Interest* updates
    if (t >= 0.2 && Interest.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Interest.tStart = t;  // (not accounting for frame time here)
      Interest.frameNStart = frameN;  // exact frame index
      
      Interest.setAutoDraw(true);
    }

    
    // *Hate* updates
    if (t >= 0.2 && Hate.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Hate.tStart = t;  // (not accounting for frame time here)
      Hate.frameNStart = frameN;  // exact frame index
      
      Hate.setAutoDraw(true);
    }

    
    // *Amusement* updates
    if (t >= 0.2 && Amusement.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Amusement.tStart = t;  // (not accounting for frame time here)
      Amusement.frameNStart = frameN;  // exact frame index
      
      Amusement.setAutoDraw(true);
    }

    
    // *Contempt* updates
    if (t >= 0.2 && Contempt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Contempt.tStart = t;  // (not accounting for frame time here)
      Contempt.frameNStart = frameN;  // exact frame index
      
      Contempt.setAutoDraw(true);
    }

    
    // *Pride* updates
    if (t >= 0.2 && Pride.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pride.tStart = t;  // (not accounting for frame time here)
      Pride.frameNStart = frameN;  // exact frame index
      
      Pride.setAutoDraw(true);
    }

    
    // *Disgust* updates
    if (t >= 0.2 && Disgust.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Disgust.tStart = t;  // (not accounting for frame time here)
      Disgust.frameNStart = frameN;  // exact frame index
      
      Disgust.setAutoDraw(true);
    }

    
    // *Joy* updates
    if (t >= 0.2 && Joy.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Joy.tStart = t;  // (not accounting for frame time here)
      Joy.frameNStart = frameN;  // exact frame index
      
      Joy.setAutoDraw(true);
    }

    
    // *Fear* updates
    if (t >= 0.2 && Fear.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Fear.tStart = t;  // (not accounting for frame time here)
      Fear.frameNStart = frameN;  // exact frame index
      
      Fear.setAutoDraw(true);
    }

    
    // *Pleasure* updates
    if (t >= 0.2 && Pleasure.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pleasure.tStart = t;  // (not accounting for frame time here)
      Pleasure.frameNStart = frameN;  // exact frame index
      
      Pleasure.setAutoDraw(true);
    }

    
    // *Disappointment* updates
    if (t >= 0.2 && Disappointment.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Disappointment.tStart = t;  // (not accounting for frame time here)
      Disappointment.frameNStart = frameN;  // exact frame index
      
      Disappointment.setAutoDraw(true);
    }

    
    // *Contentment* updates
    if (t >= 0.2 && Contentment.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Contentment.tStart = t;  // (not accounting for frame time here)
      Contentment.frameNStart = frameN;  // exact frame index
      
      Contentment.setAutoDraw(true);
    }

    
    // *Shame* updates
    if (t >= 0.2 && Shame.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Shame.tStart = t;  // (not accounting for frame time here)
      Shame.frameNStart = frameN;  // exact frame index
      
      Shame.setAutoDraw(true);
    }

    
    // *Admiration* updates
    if (t >= 0.2 && Admiration.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Admiration.tStart = t;  // (not accounting for frame time here)
      Admiration.frameNStart = frameN;  // exact frame index
      
      Admiration.setAutoDraw(true);
    }

    
    // *Regret* updates
    if (t >= 0.2 && Regret.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Regret.tStart = t;  // (not accounting for frame time here)
      Regret.frameNStart = frameN;  // exact frame index
      
      Regret.setAutoDraw(true);
    }

    
    // *Love* updates
    if (t >= 0.2 && Love.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Love.tStart = t;  // (not accounting for frame time here)
      Love.frameNStart = frameN;  // exact frame index
      
      Love.setAutoDraw(true);
    }

    
    // *Guilt* updates
    if (t >= 0.2 && Guilt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Guilt.tStart = t;  // (not accounting for frame time here)
      Guilt.frameNStart = frameN;  // exact frame index
      
      Guilt.setAutoDraw(true);
    }

    
    // *Relief* updates
    if (t >= 0.2 && Relief.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Relief.tStart = t;  // (not accounting for frame time here)
      Relief.frameNStart = frameN;  // exact frame index
      
      Relief.setAutoDraw(true);
    }

    
    // *Sadness* updates
    if (t >= 0.2 && Sadness.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Sadness.tStart = t;  // (not accounting for frame time here)
      Sadness.frameNStart = frameN;  // exact frame index
      
      Sadness.setAutoDraw(true);
    }

    
    // *Compassion* updates
    if (t >= 0.2 && Compassion.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Compassion.tStart = t;  // (not accounting for frame time here)
      Compassion.frameNStart = frameN;  // exact frame index
      
      Compassion.setAutoDraw(true);
    }

    // *mouse* updates
    if (t >= 0.2 && mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse.tStart = t;  // (not accounting for frame time here)
      mouse.frameNStart = frameN;  // exact frame index
      
      mouse.status = PsychoJS.Status.STARTED;
      mouse.mouseClock.reset();
      prevButtonState = mouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [Hate, Interest, Anger, Amusement, Contempt, Pride, Disgust, Joy, Fear, Pleasure, Disappointment, Contentment, Shame, Admiration, Regret, Love, Guilt, Relief, Sadness, Compassion]) {
            if (obj.contains(mouse)) {
              gotValidClick = true;
              mouse.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { 
            _mouseXYs = mouse.getPos();
            mouse.x.push(_mouseXYs[0]);
            mouse.y.push(_mouseXYs[1]);
            mouse.leftButton.push(_mouseButtons[0]);
            mouse.midButton.push(_mouseButtons[1]);
            mouse.rightButton.push(_mouseButtons[2]);
            mouse.time.push(mouse.mouseClock.getTime());
          }
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    if (t >= 0 && ISI_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ISI_2.tStart = t;  // (not accounting for frame time here)
      ISI_2.frameNStart = frameN;  // exact frame index
      
      ISI.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (ISI_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      ISI.status = PsychoJS.Status.FINISHED;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of emotionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function emotionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'emotions' ---
    for (const thisComponent of emotionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouse.x) {  psychoJS.experiment.addData('mouse.x', mouse.x[0])};
    if (mouse.y) {  psychoJS.experiment.addData('mouse.y', mouse.y[0])};
    if (mouse.leftButton) {  psychoJS.experiment.addData('mouse.leftButton', mouse.leftButton[0])};
    if (mouse.midButton) {  psychoJS.experiment.addData('mouse.midButton', mouse.midButton[0])};
    if (mouse.rightButton) {  psychoJS.experiment.addData('mouse.rightButton', mouse.rightButton[0])};
    if (mouse.time) {  psychoJS.experiment.addData('mouse.time', mouse.time[0])};
    if (mouse.clicked_name) {  psychoJS.experiment.addData('mouse.clicked_name', mouse.clicked_name[0])};
    
    // the Routine "emotions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var notesComponents;
function notesRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'notes' ---
    t = 0;
    notesClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    textNote.setText('');
    textNote.refresh();
    // setup some python lists for storing info about the mouseExit
    // current position of the mouse:
    mouseExit.x = [];
    mouseExit.y = [];
    mouseExit.leftButton = [];
    mouseExit.midButton = [];
    mouseExit.rightButton = [];
    mouseExit.time = [];
    mouseExit.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    notesComponents = [];
    notesComponents.push(textNote);
    notesComponents.push(textExit);
    notesComponents.push(mouseExit);
    notesComponents.push(ISI_3);
    
    for (const thisComponent of notesComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function notesRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'notes' ---
    // get current time
    t = notesClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textNote* updates
    if (t >= 0.2 && textNote.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textNote.tStart = t;  // (not accounting for frame time here)
      textNote.frameNStart = frameN;  // exact frame index
      
      textNote.setAutoDraw(true);
    }

    
    // *textExit* updates
    if (t >= 0.2 && textExit.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textExit.tStart = t;  // (not accounting for frame time here)
      textExit.frameNStart = frameN;  // exact frame index
      
      textExit.setAutoDraw(true);
    }

    // *mouseExit* updates
    if (t >= 0.2 && mouseExit.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouseExit.tStart = t;  // (not accounting for frame time here)
      mouseExit.frameNStart = frameN;  // exact frame index
      
      mouseExit.status = PsychoJS.Status.STARTED;
      mouseExit.mouseClock.reset();
      prevButtonState = mouseExit.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouseExit.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouseExit.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [textExit]) {
            if (obj.contains(mouseExit)) {
              gotValidClick = true;
              mouseExit.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { 
            _mouseXYs = mouseExit.getPos();
            mouseExit.x.push(_mouseXYs[0]);
            mouseExit.y.push(_mouseXYs[1]);
            mouseExit.leftButton.push(_mouseButtons[0]);
            mouseExit.midButton.push(_mouseButtons[1]);
            mouseExit.rightButton.push(_mouseButtons[2]);
            mouseExit.time.push(mouseExit.mouseClock.getTime());
          }
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    if (t >= 0 && ISI_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ISI_3.tStart = t;  // (not accounting for frame time here)
      ISI_3.frameNStart = frameN;  // exact frame index
      
      ISI.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (ISI_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      ISI.status = PsychoJS.Status.FINISHED;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of notesComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function notesRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'notes' ---
    for (const thisComponent of notesComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('textNote.text',textNote.text)
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouseExit.x) {  psychoJS.experiment.addData('mouseExit.x', mouseExit.x[0])};
    if (mouseExit.y) {  psychoJS.experiment.addData('mouseExit.y', mouseExit.y[0])};
    if (mouseExit.leftButton) {  psychoJS.experiment.addData('mouseExit.leftButton', mouseExit.leftButton[0])};
    if (mouseExit.midButton) {  psychoJS.experiment.addData('mouseExit.midButton', mouseExit.midButton[0])};
    if (mouseExit.rightButton) {  psychoJS.experiment.addData('mouseExit.rightButton', mouseExit.rightButton[0])};
    if (mouseExit.time) {  psychoJS.experiment.addData('mouseExit.time', mouseExit.time[0])};
    if (mouseExit.clicked_name) {  psychoJS.experiment.addData('mouseExit.clicked_name', mouseExit.clicked_name[0])};
    
    // the Routine "notes" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var byeComponents;
function byeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'bye' ---
    t = 0;
    byeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(4.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    byeComponents = [];
    byeComponents.push(text);
    
    for (const thisComponent of byeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function byeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'bye' ---
    // get current time
    t = byeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of byeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function byeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'bye' ---
    for (const thisComponent of byeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
