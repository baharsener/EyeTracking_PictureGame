/***************************** 
 * Eyelink_Tripletsgame Test *
 *****************************/

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'Eyelink_TripletsGame';  // from the Builder filename that created this script
let expInfo = {'participant': ''};

// Start code blocks for 'Before Experiment'
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
flowScheduler.add(initCodeRoutineBegin());
flowScheduler.add(initCodeRoutineEachFrame());
flowScheduler.add(initCodeRoutineEnd());
flowScheduler.add(trialRoutineBegin());
flowScheduler.add(trialRoutineEachFrame());
flowScheduler.add(trialRoutineEnd());
const EncodingTrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(EncodingTrialsLoopBegin, EncodingTrialsLoopScheduler);
flowScheduler.add(EncodingTrialsLoopScheduler);
flowScheduler.add(EncodingTrialsLoopEnd);
flowScheduler.add(initRecallPicsRoutineBegin());
flowScheduler.add(initRecallPicsRoutineEachFrame());
flowScheduler.add(initRecallPicsRoutineEnd());
const RetrievalTrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(RetrievalTrialsLoopBegin, RetrievalTrialsLoopScheduler);
flowScheduler.add(RetrievalTrialsLoopScheduler);
flowScheduler.add(RetrievalTrialsLoopEnd);
flowScheduler.add(break_2RoutineBegin());
flowScheduler.add(break_2RoutineEachFrame());
flowScheduler.add(break_2RoutineEnd());
const EncodingBlock2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(EncodingBlock2LoopBegin, EncodingBlock2LoopScheduler);
flowScheduler.add(EncodingBlock2LoopScheduler);
flowScheduler.add(EncodingBlock2LoopEnd);
const RetrievalBlock2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(RetrievalBlock2LoopBegin, RetrievalBlock2LoopScheduler);
flowScheduler.add(RetrievalBlock2LoopScheduler);
flowScheduler.add(RetrievalBlock2LoopEnd);
flowScheduler.add(EndScreenRoutineBegin());
flowScheduler.add(EndScreenRoutineEachFrame());
flowScheduler.add(EndScreenRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.1.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var initCodeClock;
var trialClock;
var Instructions;
var start;
var first_viewClock;
var Triplet1;
var Triplet2;
var Triplet3;
var sound_pop;
var sound_pop2;
var sound_pop3;
var maskClock;
var Mask;
var second_viewClock;
var img1;
var img2;
var img3;
var sound_pop4;
var sound_pop5;
var sound_pop6;
var methodQTextClock;
var text_2;
var MethodCheckClock;
var text;
var sameText;
var diffText;
var leftCL;
var rightCL;
var MethodMouse;
var clicked_soundClock;
var clickedSound;
var initRecallPicsClock;
var RetrievalImageClock;
var retIMG;
var sound_pop7;
var Q2TextClock;
var question_text;
var DecisionClock;
var decisionQ_2;
var first_left;
var second_middle;
var third_right;
var First;
var Second;
var Third;
var Order_Position_Response;
var break_2Clock;
var BlockBreak;
var text_4;
var start2;
var EndScreenClock;
var end;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "initCode"
  initCodeClock = new util.Clock();
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  Instructions = new visual.TextStim({
    win: psychoJS.window,
    name: 'Instructions',
    text: 'In this task you will review sets of objects in triplets. Your task is to pay attention to where and when these objects appear. Press the spacebar to begin.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  start = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "first_view"
  first_viewClock = new util.Clock();
  Triplet1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Triplet1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  Triplet2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Triplet2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  Triplet3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Triplet3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  sound_pop = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  sound_pop.setVolume(1.0);
  sound_pop2 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  sound_pop2.setVolume(1.0);
  sound_pop3 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  sound_pop3.setVolume(1.0);
  // Initialize components for Routine "mask"
  maskClock = new util.Clock();
  Mask = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Mask', units : undefined, 
    image : 'images/Mask.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [1.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "second_view"
  second_viewClock = new util.Clock();
  img1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'img1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  img2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'img2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  img3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'img3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  sound_pop4 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  sound_pop4.setVolume(1.0);
  sound_pop5 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  sound_pop5.setVolume(1.0);
  sound_pop6 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  sound_pop6.setVolume(1.0);
  // Initialize components for Routine "methodQText"
  methodQTextClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'Was this set same or different as the previous set?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "MethodCheck"
  MethodCheckClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Was this set same or different as the previous set?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  sameText = new visual.TextStim({
    win: psychoJS.window,
    name: 'sameText',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.2), (- 0.3)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  diffText = new visual.TextStim({
    win: psychoJS.window,
    name: 'diffText',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.2, (- 0.3)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  leftCL = new visual.Rect ({
    win: psychoJS.window, name: 'leftCL', 
    width: (-0.2, -0.2)[0], height: (-0.2, -0.2)[1],
    ori: 0, pos: (-.2, -.3),
    lineWidth: 3, lineColor: new util.Color('white'),
    fillColor: new util.Color([1.0, 1.0, 1.0]),
    opacity: 0.5, depth: -4, interpolate: true,
  });
  
  rightCL = new visual.Rect ({
    win: psychoJS.window, name: 'rightCL', 
    width: (0.2, 0.2)[0], height: (0.2, 0.2)[1],
    ori: 0, pos: (0.2, -0.3),
    lineWidth: 3, lineColor: new util.Color('white'),
    fillColor: new util.Color([1.0, 1.0, 1.0]),
    opacity: 0.5, depth: -5, interpolate: true,
  });
  
  MethodMouse = new core.Mouse({
    win: psychoJS.window,
  });
  MethodMouse.mouseClock = new util.Clock();
  // Initialize components for Routine "clicked_sound"
  clicked_soundClock = new util.Clock();
  clickedSound = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 0.5,
    });
  clickedSound.setVolume(1.0);
  // Initialize components for Routine "initRecallPics"
  initRecallPicsClock = new util.Clock();
  // Initialize components for Routine "RetrievalImage"
  RetrievalImageClock = new util.Clock();
  retIMG = new visual.ImageStim({
    win : psychoJS.window,
    name : 'retIMG', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  sound_pop7 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  sound_pop7.setVolume(1.0);
  // Initialize components for Routine "Q2Text"
  Q2TextClock = new util.Clock();
  question_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'question_text',
    text: 'When did you see this object?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Decision"
  DecisionClock = new util.Clock();
  decisionQ_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'decisionQ_2',
    text: 'When did you see this object?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  first_left = new visual.Rect ({
    win: psychoJS.window, name: 'first_left', 
    width: (0.15, 0.15)[0], height: (0.15, 0.15)[1],
    ori: 0, pos: (0, 0.1),
    lineWidth: 3, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 0.5, depth: -2, interpolate: true,
  });
  
  second_middle = new visual.Rect ({
    win: psychoJS.window, name: 'second_middle', 
    width: (0.15, 0.15)[0], height: (0.15, 0.15)[1],
    ori: 0, pos: (0, -0.1),
    lineWidth: 3, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 0.5, depth: -3, interpolate: true,
  });
  
  third_right = new visual.Rect ({
    win: psychoJS.window, name: 'third_right', 
    width: (0.15, 0.15)[0], height: (0.15, 0.15)[1],
    ori: 0, pos: (0, -0.3),
    lineWidth: 3, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 0.5, depth: -4, interpolate: true,
  });
  
  First = new visual.TextStim({
    win: psychoJS.window,
    name: 'First',
    text: 'First',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.1], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  Second = new visual.TextStim({
    win: psychoJS.window,
    name: 'Second',
    text: 'Second',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.1)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  Third = new visual.TextStim({
    win: psychoJS.window,
    name: 'Third',
    text: 'Third',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -7.0 
  });
  
  Order_Position_Response = new core.Mouse({
    win: psychoJS.window,
  });
  Order_Position_Response.mouseClock = new util.Clock();
  // Initialize components for Routine "clicked_sound"
  clicked_soundClock = new util.Clock();
  clickedSound = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 0.5,
    });
  clickedSound.setVolume(1.0);
  // Initialize components for Routine "break_2"
  break_2Clock = new util.Clock();
  BlockBreak = new visual.TextStim({
    win: psychoJS.window,
    name: 'BlockBreak',
    text: 'You are done with the first portion of the task!\n\nNow, you have a three minute break. When the time is over, you will see instructions on the screen.\n\nThe next half of the task will be identical to the first half!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'In this task you will review sets of objects in triplets. Your task is to pay attention to where and when these objects appear. Press the spacebar to begin.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  start2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "first_view"
  first_viewClock = new util.Clock();
  Triplet1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Triplet1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  Triplet2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Triplet2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  Triplet3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Triplet3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  sound_pop = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  sound_pop.setVolume(1.0);
  sound_pop2 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  sound_pop2.setVolume(1.0);
  sound_pop3 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  sound_pop3.setVolume(1.0);
  // Initialize components for Routine "mask"
  maskClock = new util.Clock();
  Mask = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Mask', units : undefined, 
    image : 'images/Mask.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [1.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "second_view"
  second_viewClock = new util.Clock();
  img1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'img1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  img2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'img2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  img3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'img3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  sound_pop4 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  sound_pop4.setVolume(1.0);
  sound_pop5 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  sound_pop5.setVolume(1.0);
  sound_pop6 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  sound_pop6.setVolume(1.0);
  // Initialize components for Routine "methodQText"
  methodQTextClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'Was this set same or different as the previous set?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "MethodCheck"
  MethodCheckClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Was this set same or different as the previous set?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  sameText = new visual.TextStim({
    win: psychoJS.window,
    name: 'sameText',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.2), (- 0.3)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  diffText = new visual.TextStim({
    win: psychoJS.window,
    name: 'diffText',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.2, (- 0.3)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  leftCL = new visual.Rect ({
    win: psychoJS.window, name: 'leftCL', 
    width: (-0.2, -0.2)[0], height: (-0.2, -0.2)[1],
    ori: 0, pos: (-.2, -.3),
    lineWidth: 3, lineColor: new util.Color('white'),
    fillColor: new util.Color([1.0, 1.0, 1.0]),
    opacity: 0.5, depth: -4, interpolate: true,
  });
  
  rightCL = new visual.Rect ({
    win: psychoJS.window, name: 'rightCL', 
    width: (0.2, 0.2)[0], height: (0.2, 0.2)[1],
    ori: 0, pos: (0.2, -0.3),
    lineWidth: 3, lineColor: new util.Color('white'),
    fillColor: new util.Color([1.0, 1.0, 1.0]),
    opacity: 0.5, depth: -5, interpolate: true,
  });
  
  MethodMouse = new core.Mouse({
    win: psychoJS.window,
  });
  MethodMouse.mouseClock = new util.Clock();
  // Initialize components for Routine "clicked_sound"
  clicked_soundClock = new util.Clock();
  clickedSound = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 0.5,
    });
  clickedSound.setVolume(1.0);
  // Initialize components for Routine "RetrievalImage"
  RetrievalImageClock = new util.Clock();
  retIMG = new visual.ImageStim({
    win : psychoJS.window,
    name : 'retIMG', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  sound_pop7 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  sound_pop7.setVolume(1.0);
  // Initialize components for Routine "Q2Text"
  Q2TextClock = new util.Clock();
  question_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'question_text',
    text: 'When did you see this object?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Decision"
  DecisionClock = new util.Clock();
  decisionQ_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'decisionQ_2',
    text: 'When did you see this object?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  first_left = new visual.Rect ({
    win: psychoJS.window, name: 'first_left', 
    width: (0.15, 0.15)[0], height: (0.15, 0.15)[1],
    ori: 0, pos: (0, 0.1),
    lineWidth: 3, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 0.5, depth: -2, interpolate: true,
  });
  
  second_middle = new visual.Rect ({
    win: psychoJS.window, name: 'second_middle', 
    width: (0.15, 0.15)[0], height: (0.15, 0.15)[1],
    ori: 0, pos: (0, -0.1),
    lineWidth: 3, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 0.5, depth: -3, interpolate: true,
  });
  
  third_right = new visual.Rect ({
    win: psychoJS.window, name: 'third_right', 
    width: (0.15, 0.15)[0], height: (0.15, 0.15)[1],
    ori: 0, pos: (0, -0.3),
    lineWidth: 3, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 0.5, depth: -4, interpolate: true,
  });
  
  First = new visual.TextStim({
    win: psychoJS.window,
    name: 'First',
    text: 'First',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.1], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  Second = new visual.TextStim({
    win: psychoJS.window,
    name: 'Second',
    text: 'Second',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.1)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  Third = new visual.TextStim({
    win: psychoJS.window,
    name: 'Third',
    text: 'Third',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -7.0 
  });
  
  Order_Position_Response = new core.Mouse({
    win: psychoJS.window,
  });
  Order_Position_Response.mouseClock = new util.Clock();
  // Initialize components for Routine "clicked_sound"
  clicked_soundClock = new util.Clock();
  clickedSound = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 0.5,
    });
  clickedSound.setVolume(1.0);
  // Initialize components for Routine "EndScreen"
  EndScreenClock = new util.Clock();
  end = new visual.TextStim({
    win: psychoJS.window,
    name: 'end',
    text: 'You are done with this task! Thank you for participating!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var initCodeComponents;
function initCodeRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'initCode'-------
    t = 0;
    initCodeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    initCodeComponents = [];
    
    initCodeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function initCodeRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'initCode'-------
    // get current time
    t = initCodeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    initCodeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function initCodeRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'initCode'-------
    initCodeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "initCode" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _start_allKeys;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'trial'-------
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    start.keys = undefined;
    start.rt = undefined;
    _start_allKeys = [];
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(Instructions);
    trialComponents.push(start);
    
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'trial'-------
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Instructions* updates
    if (t >= 0.0 && Instructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instructions.tStart = t;  // (not accounting for frame time here)
      Instructions.frameNStart = frameN;  // exact frame index
      
      Instructions.setAutoDraw(true);
    }

    
    // *start* updates
    if (t >= 0.0 && start.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      start.tStart = t;  // (not accounting for frame time here)
      start.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { start.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { start.start(); }); // start on screen flip
    }

    if (start.status === PsychoJS.Status.STARTED) {
      let theseKeys = start.getKeys({keyList: ['space', 'q'], waitRelease: false});
      _start_allKeys = _start_allKeys.concat(theseKeys);
      if (_start_allKeys.length > 0) {
        start.keys = _start_allKeys[_start_allKeys.length - 1].name;  // just the last key pressed
        start.rt = _start_allKeys[_start_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
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
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'trial'-------
    trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    start.stop();
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var EncodingTrials;
var currentLoop;
function EncodingTrialsLoopBegin(EncodingTrialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  EncodingTrials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: numEncoding, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'EncodingTrials'
  });
  psychoJS.experiment.addLoop(EncodingTrials); // add the loop to the experiment
  currentLoop = EncodingTrials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  EncodingTrials.forEach(function() {
    const snapshot = EncodingTrials.getSnapshot();

    EncodingTrialsLoopScheduler.add(importConditions(snapshot));
    EncodingTrialsLoopScheduler.add(first_viewRoutineBegin(snapshot));
    EncodingTrialsLoopScheduler.add(first_viewRoutineEachFrame(snapshot));
    EncodingTrialsLoopScheduler.add(first_viewRoutineEnd(snapshot));
    EncodingTrialsLoopScheduler.add(maskRoutineBegin(snapshot));
    EncodingTrialsLoopScheduler.add(maskRoutineEachFrame(snapshot));
    EncodingTrialsLoopScheduler.add(maskRoutineEnd(snapshot));
    EncodingTrialsLoopScheduler.add(second_viewRoutineBegin(snapshot));
    EncodingTrialsLoopScheduler.add(second_viewRoutineEachFrame(snapshot));
    EncodingTrialsLoopScheduler.add(second_viewRoutineEnd(snapshot));
    EncodingTrialsLoopScheduler.add(methodQTextRoutineBegin(snapshot));
    EncodingTrialsLoopScheduler.add(methodQTextRoutineEachFrame(snapshot));
    EncodingTrialsLoopScheduler.add(methodQTextRoutineEnd(snapshot));
    EncodingTrialsLoopScheduler.add(MethodCheckRoutineBegin(snapshot));
    EncodingTrialsLoopScheduler.add(MethodCheckRoutineEachFrame(snapshot));
    EncodingTrialsLoopScheduler.add(MethodCheckRoutineEnd(snapshot));
    EncodingTrialsLoopScheduler.add(clicked_soundRoutineBegin(snapshot));
    EncodingTrialsLoopScheduler.add(clicked_soundRoutineEachFrame(snapshot));
    EncodingTrialsLoopScheduler.add(clicked_soundRoutineEnd(snapshot));
    EncodingTrialsLoopScheduler.add(endLoopIteration(EncodingTrialsLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function EncodingTrialsLoopEnd() {
  psychoJS.experiment.removeLoop(EncodingTrials);

  return Scheduler.Event.NEXT;
}


var RetrievalTrials;
function RetrievalTrialsLoopBegin(RetrievalTrialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  RetrievalTrials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: numRetrieval, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'RetrievalTrials'
  });
  psychoJS.experiment.addLoop(RetrievalTrials); // add the loop to the experiment
  currentLoop = RetrievalTrials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  RetrievalTrials.forEach(function() {
    const snapshot = RetrievalTrials.getSnapshot();

    RetrievalTrialsLoopScheduler.add(importConditions(snapshot));
    RetrievalTrialsLoopScheduler.add(RetrievalImageRoutineBegin(snapshot));
    RetrievalTrialsLoopScheduler.add(RetrievalImageRoutineEachFrame(snapshot));
    RetrievalTrialsLoopScheduler.add(RetrievalImageRoutineEnd(snapshot));
    RetrievalTrialsLoopScheduler.add(Q2TextRoutineBegin(snapshot));
    RetrievalTrialsLoopScheduler.add(Q2TextRoutineEachFrame(snapshot));
    RetrievalTrialsLoopScheduler.add(Q2TextRoutineEnd(snapshot));
    RetrievalTrialsLoopScheduler.add(DecisionRoutineBegin(snapshot));
    RetrievalTrialsLoopScheduler.add(DecisionRoutineEachFrame(snapshot));
    RetrievalTrialsLoopScheduler.add(DecisionRoutineEnd(snapshot));
    RetrievalTrialsLoopScheduler.add(clicked_soundRoutineBegin(snapshot));
    RetrievalTrialsLoopScheduler.add(clicked_soundRoutineEachFrame(snapshot));
    RetrievalTrialsLoopScheduler.add(clicked_soundRoutineEnd(snapshot));
    RetrievalTrialsLoopScheduler.add(endLoopIteration(RetrievalTrialsLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function RetrievalTrialsLoopEnd() {
  psychoJS.experiment.removeLoop(RetrievalTrials);

  return Scheduler.Event.NEXT;
}


var EncodingBlock2;
function EncodingBlock2LoopBegin(EncodingBlock2LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  EncodingBlock2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: numEncoding, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'EncodingBlock2'
  });
  psychoJS.experiment.addLoop(EncodingBlock2); // add the loop to the experiment
  currentLoop = EncodingBlock2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  EncodingBlock2.forEach(function() {
    const snapshot = EncodingBlock2.getSnapshot();

    EncodingBlock2LoopScheduler.add(importConditions(snapshot));
    EncodingBlock2LoopScheduler.add(first_viewRoutineBegin(snapshot));
    EncodingBlock2LoopScheduler.add(first_viewRoutineEachFrame(snapshot));
    EncodingBlock2LoopScheduler.add(first_viewRoutineEnd(snapshot));
    EncodingBlock2LoopScheduler.add(maskRoutineBegin(snapshot));
    EncodingBlock2LoopScheduler.add(maskRoutineEachFrame(snapshot));
    EncodingBlock2LoopScheduler.add(maskRoutineEnd(snapshot));
    EncodingBlock2LoopScheduler.add(second_viewRoutineBegin(snapshot));
    EncodingBlock2LoopScheduler.add(second_viewRoutineEachFrame(snapshot));
    EncodingBlock2LoopScheduler.add(second_viewRoutineEnd(snapshot));
    EncodingBlock2LoopScheduler.add(methodQTextRoutineBegin(snapshot));
    EncodingBlock2LoopScheduler.add(methodQTextRoutineEachFrame(snapshot));
    EncodingBlock2LoopScheduler.add(methodQTextRoutineEnd(snapshot));
    EncodingBlock2LoopScheduler.add(MethodCheckRoutineBegin(snapshot));
    EncodingBlock2LoopScheduler.add(MethodCheckRoutineEachFrame(snapshot));
    EncodingBlock2LoopScheduler.add(MethodCheckRoutineEnd(snapshot));
    EncodingBlock2LoopScheduler.add(clicked_soundRoutineBegin(snapshot));
    EncodingBlock2LoopScheduler.add(clicked_soundRoutineEachFrame(snapshot));
    EncodingBlock2LoopScheduler.add(clicked_soundRoutineEnd(snapshot));
    EncodingBlock2LoopScheduler.add(endLoopIteration(EncodingBlock2LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function EncodingBlock2LoopEnd() {
  psychoJS.experiment.removeLoop(EncodingBlock2);

  return Scheduler.Event.NEXT;
}


var RetrievalBlock2;
function RetrievalBlock2LoopBegin(RetrievalBlock2LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  RetrievalBlock2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: numRetrieval, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'RetrievalBlock2'
  });
  psychoJS.experiment.addLoop(RetrievalBlock2); // add the loop to the experiment
  currentLoop = RetrievalBlock2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  RetrievalBlock2.forEach(function() {
    const snapshot = RetrievalBlock2.getSnapshot();

    RetrievalBlock2LoopScheduler.add(importConditions(snapshot));
    RetrievalBlock2LoopScheduler.add(RetrievalImageRoutineBegin(snapshot));
    RetrievalBlock2LoopScheduler.add(RetrievalImageRoutineEachFrame(snapshot));
    RetrievalBlock2LoopScheduler.add(RetrievalImageRoutineEnd(snapshot));
    RetrievalBlock2LoopScheduler.add(Q2TextRoutineBegin(snapshot));
    RetrievalBlock2LoopScheduler.add(Q2TextRoutineEachFrame(snapshot));
    RetrievalBlock2LoopScheduler.add(Q2TextRoutineEnd(snapshot));
    RetrievalBlock2LoopScheduler.add(DecisionRoutineBegin(snapshot));
    RetrievalBlock2LoopScheduler.add(DecisionRoutineEachFrame(snapshot));
    RetrievalBlock2LoopScheduler.add(DecisionRoutineEnd(snapshot));
    RetrievalBlock2LoopScheduler.add(clicked_soundRoutineBegin(snapshot));
    RetrievalBlock2LoopScheduler.add(clicked_soundRoutineEachFrame(snapshot));
    RetrievalBlock2LoopScheduler.add(clicked_soundRoutineEnd(snapshot));
    RetrievalBlock2LoopScheduler.add(endLoopIteration(RetrievalBlock2LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function RetrievalBlock2LoopEnd() {
  psychoJS.experiment.removeLoop(RetrievalBlock2);

  return Scheduler.Event.NEXT;
}


var trialType;
var method_Trial;
var leftPos;
var midPos;
var rightPos;
var firstPos;
var secondPos;
var thirdPos;
var triplet1;
var triplet2;
var triplet3;
var first_viewComponents;
function first_viewRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'first_view'-------
    t = 0;
    first_viewClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    trialType = trialTypes[eTrials];
    method_Trial = sameDiff[eTrials];
    //iterate through trial type and set a new one for each trial
    leftPos = [(- 0.5), 0.0];
    midPos = [0.0, 0.0];
    rightPos = [0.5, 0.0];
    //define positions of left right middle
    if ((trialType === "LMR")) {
        firstPos = leftPos;
        secondPos = midPos;
        thirdPos = rightPos;
    } else if ((trialType === "LRM")) {
        firstPos = leftPos;
        secondPos = rightPos;
        thirdPos = midPos;
    } else if ((trialType === "MLR")) {
        firstPos = midPos;
        secondPos = leftPos;
        thirdPos = rightPos;
    } else if ((trialType === "RML")) {
        firstPos = rightPos;
        secondPos = midPos;
        thirdPos = leftPos;
    } else if ((trialType === "RLM")) {
         firstPos = rightPos;
         secondPos = leftPos;
         thirdPos = midPos;
    } else if ((trialType === "MRL")) {
         firstPos = midPos;
         secondPos = rightPos;
         thirdPos = leftPos;
    }
    triplet1 = (("images/" + encodingPics[eTrials][0]) + ".png");
    triplet2 = (("images/" + encodingPics[eTrials][1]) + ".png");
    triplet3 = (("images/" + encodingPics[eTrials][2]) + ".png");
    
    thisExp.addData("Trial_Order", trialType);
    thisExp.addData("triplet1", triplet1);
    thisExp.addData("triplet2", triplet2);
    thisExp.addData("triplet3", triplet3);
    Triplet1.setPos(firstPos);
    Triplet1.setImage(triplet1);
    Triplet2.setPos(secondPos);
    Triplet2.setImage(triplet2);
    Triplet3.setPos(thirdPos);
    Triplet3.setImage(triplet3);
    sound_pop = new sound.Sound({
    win: psychoJS.window,
    value: 'POP.wav',
    secs: -1,
    });
    sound_pop.setVolume(1.0);
    sound_pop2 = new sound.Sound({
    win: psychoJS.window,
    value: 'POP.wav',
    secs: -1,
    });
    sound_pop2.setVolume(1.0);
    sound_pop3 = new sound.Sound({
    win: psychoJS.window,
    value: 'POP.wav',
    secs: -1,
    });
    sound_pop3.setVolume(1.0);
    // keep track of which components have finished
    first_viewComponents = [];
    first_viewComponents.push(Triplet1);
    first_viewComponents.push(Triplet2);
    first_viewComponents.push(Triplet3);
    first_viewComponents.push(sound_pop);
    first_viewComponents.push(sound_pop2);
    first_viewComponents.push(sound_pop3);
    
    first_viewComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function first_viewRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'first_view'-------
    // get current time
    t = first_viewClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Triplet1* updates
    if (t >= 0.0 && Triplet1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Triplet1.tStart = t;  // (not accounting for frame time here)
      Triplet1.frameNStart = frameN;  // exact frame index
      
      Triplet1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Triplet1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Triplet1.setAutoDraw(false);
    }
    
    // *Triplet2* updates
    if (t >= 2 && Triplet2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Triplet2.tStart = t;  // (not accounting for frame time here)
      Triplet2.frameNStart = frameN;  // exact frame index
      
      Triplet2.setAutoDraw(true);
    }

    frameRemains = 2 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Triplet2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Triplet2.setAutoDraw(false);
    }
    
    // *Triplet3* updates
    if (t >= 4 && Triplet3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Triplet3.tStart = t;  // (not accounting for frame time here)
      Triplet3.frameNStart = frameN;  // exact frame index
      
      Triplet3.setAutoDraw(true);
    }

    frameRemains = 4 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Triplet3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Triplet3.setAutoDraw(false);
    }
    // start/stop sound_pop
    if (t >= 0 && sound_pop.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_pop.tStart = t;  // (not accounting for frame time here)
      sound_pop.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_pop.play(); });  // screen flip
      sound_pop.status = PsychoJS.Status.STARTED;
    }
    if (t >= (sound_pop.getDuration() + sound_pop.tStart)     && sound_pop.status === PsychoJS.Status.STARTED) {
      sound_pop.stop();  // stop the sound (if longer than duration)
      sound_pop.status = PsychoJS.Status.FINISHED;
    }
    // start/stop sound_pop2
    if (t >= 2 && sound_pop2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_pop2.tStart = t;  // (not accounting for frame time here)
      sound_pop2.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_pop2.play(); });  // screen flip
      sound_pop2.status = PsychoJS.Status.STARTED;
    }
    if (t >= (sound_pop2.getDuration() + sound_pop2.tStart)     && sound_pop2.status === PsychoJS.Status.STARTED) {
      sound_pop2.stop();  // stop the sound (if longer than duration)
      sound_pop2.status = PsychoJS.Status.FINISHED;
    }
    // start/stop sound_pop3
    if (t >= 4 && sound_pop3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_pop3.tStart = t;  // (not accounting for frame time here)
      sound_pop3.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_pop3.play(); });  // screen flip
      sound_pop3.status = PsychoJS.Status.STARTED;
    }
    if (t >= (sound_pop3.getDuration() + sound_pop3.tStart)     && sound_pop3.status === PsychoJS.Status.STARTED) {
      sound_pop3.stop();  // stop the sound (if longer than duration)
      sound_pop3.status = PsychoJS.Status.FINISHED;
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
    first_viewComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function first_viewRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'first_view'-------
    first_viewComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    sound_pop.stop();  // ensure sound has stopped at end of routine
    sound_pop2.stop();  // ensure sound has stopped at end of routine
    sound_pop3.stop();  // ensure sound has stopped at end of routine
    // the Routine "first_view" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var maskComponents;
function maskRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'mask'-------
    t = 0;
    maskClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.500000);
    // update component parameters for each repeat
    // keep track of which components have finished
    maskComponents = [];
    maskComponents.push(Mask);
    
    maskComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function maskRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'mask'-------
    // get current time
    t = maskClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Mask* updates
    if (t >= 0.0 && Mask.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Mask.tStart = t;  // (not accounting for frame time here)
      Mask.frameNStart = frameN;  // exact frame index
      
      Mask.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Mask.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Mask.setAutoDraw(false);
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
    maskComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function maskRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'mask'-------
    maskComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var methodAns;
var nextTrial;
var second_viewComponents;
function second_viewRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'second_view'-------
    t = 0;
    second_viewClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    if ((method_Trial == "same")) {
        trialType = trialTypes[eTrials];
        methodAns = ["sameText"];
        samePics.push(encodingPics[eTrials][0]);
        samePics.push(encodingPics[eTrials][1]);
        samePics.push(encodingPics[eTrials][2]);
        thisExp.addData("encodingType", "same");
        nextTrial = [];
    
    } else {
        nextTrial = trialTypes[Math.floor(Math.random() * trialTypes.length)];
        while ((nextTrial == trialTypes[eTrials])) {
            nextTrial = trialTypes[Math.floor(Math.random() * trialTypes.length)];
            end;
        }
        trialType = nextTrial;
        if ((trialType === "LMR")) {
        firstPos = leftPos;
        secondPos = midPos;
        thirdPos = rightPos;
    } else if ((trialType === "LRM")) {
        firstPos = leftPos;
        secondPos = rightPos;
        thirdPos = midPos;
    } else if ((trialType === "MLR")) {
        firstPos = midPos;
        secondPos = leftPos;
        thirdPos = rightPos;
    } else if ((trialType === "RML")) {
        firstPos = rightPos;
        secondPos = midPos;
        thirdPos = leftPos;
    } else if ((trialType === "RLM")) {
         firstPos = rightPos;
         secondPos = leftPos;
         thirdPos = midPos;
    } else if ((trialType === "MRL")) {
         firstPos = midPos;
         secondPos = rightPos;
         thirdPos = leftPos;
    }
        triplet1 = (("images/" + encodingPics[eTrials][0]) + ".png");
        triplet2 = (("images/" + encodingPics[eTrials][1]) + ".png");
        triplet3 = (("images/" + encodingPics[eTrials][2]) + ".png");
        thisExp.addData("encodingType", "diff");
        methodAns = ["diffText"];
    }
    
    thisExp.addData("triplet1", triplet1);
    thisExp.addData("triplet2", triplet2);
    thisExp.addData("triplet3", triplet3);
    thisExp.addData("trialType",trialType);
    thisExp.addData("nextTrial", nextTrial);
    img1.setPos(firstPos);
    img1.setImage(triplet1);
    img2.setPos(secondPos);
    img2.setImage(triplet2);
    img3.setPos(thirdPos);
    img3.setImage(triplet3);
    sound_pop4 = new sound.Sound({
    win: psychoJS.window,
    value: 'POP.wav',
    secs: -1,
    });
    sound_pop4.setVolume(1.0);
    sound_pop5 = new sound.Sound({
    win: psychoJS.window,
    value: 'POP.wav',
    secs: -1,
    });
    sound_pop5.setVolume(1.0);
    sound_pop6 = new sound.Sound({
    win: psychoJS.window,
    value: 'POP.wav',
    secs: -1,
    });
    sound_pop6.setVolume(1.0);
    // keep track of which components have finished
    second_viewComponents = [];
    second_viewComponents.push(img1);
    second_viewComponents.push(img2);
    second_viewComponents.push(img3);
    second_viewComponents.push(sound_pop4);
    second_viewComponents.push(sound_pop5);
    second_viewComponents.push(sound_pop6);
    
    second_viewComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function second_viewRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'second_view'-------
    // get current time
    t = second_viewClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *img1* updates
    if (t >= 0.0 && img1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      img1.tStart = t;  // (not accounting for frame time here)
      img1.frameNStart = frameN;  // exact frame index
      
      img1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (img1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      img1.setAutoDraw(false);
    }
    
    // *img2* updates
    if (t >= 2 && img2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      img2.tStart = t;  // (not accounting for frame time here)
      img2.frameNStart = frameN;  // exact frame index
      
      img2.setAutoDraw(true);
    }

    frameRemains = 2 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (img2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      img2.setAutoDraw(false);
    }
    
    // *img3* updates
    if (t >= 4 && img3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      img3.tStart = t;  // (not accounting for frame time here)
      img3.frameNStart = frameN;  // exact frame index
      
      img3.setAutoDraw(true);
    }

    frameRemains = 4 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (img3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      img3.setAutoDraw(false);
    }
    // start/stop sound_pop4
    if (t >= 0.0 && sound_pop4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_pop4.tStart = t;  // (not accounting for frame time here)
      sound_pop4.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_pop4.play(); });  // screen flip
      sound_pop4.status = PsychoJS.Status.STARTED;
    }
    if (t >= (sound_pop4.getDuration() + sound_pop4.tStart)     && sound_pop4.status === PsychoJS.Status.STARTED) {
      sound_pop4.stop();  // stop the sound (if longer than duration)
      sound_pop4.status = PsychoJS.Status.FINISHED;
    }
    // start/stop sound_pop5
    if (t >= 2 && sound_pop5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_pop5.tStart = t;  // (not accounting for frame time here)
      sound_pop5.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_pop5.play(); });  // screen flip
      sound_pop5.status = PsychoJS.Status.STARTED;
    }
    if (t >= (sound_pop5.getDuration() + sound_pop5.tStart)     && sound_pop5.status === PsychoJS.Status.STARTED) {
      sound_pop5.stop();  // stop the sound (if longer than duration)
      sound_pop5.status = PsychoJS.Status.FINISHED;
    }
    // start/stop sound_pop6
    if (t >= 4 && sound_pop6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_pop6.tStart = t;  // (not accounting for frame time here)
      sound_pop6.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_pop6.play(); });  // screen flip
      sound_pop6.status = PsychoJS.Status.STARTED;
    }
    if (t >= (sound_pop6.getDuration() + sound_pop6.tStart)     && sound_pop6.status === PsychoJS.Status.STARTED) {
      sound_pop6.stop();  // stop the sound (if longer than duration)
      sound_pop6.status = PsychoJS.Status.FINISHED;
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
    second_viewComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var eTrials;
function second_viewRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'second_view'-------
    second_viewComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    eTrials = (eTrials + 1);
    EncodingTrials.addData("eTrials", eTrials.toString());
    console.log(eTrials);
    console.log("triplet1",triplet1)
    
    
    sound_pop4.stop();  // ensure sound has stopped at end of routine
    sound_pop5.stop();  // ensure sound has stopped at end of routine
    sound_pop6.stop();  // ensure sound has stopped at end of routine
    // the Routine "second_view" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var methodQTextComponents;
function methodQTextRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'methodQText'-------
    t = 0;
    methodQTextClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    methodQTextComponents = [];
    methodQTextComponents.push(text_2);
    
    methodQTextComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function methodQTextRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'methodQText'-------
    // get current time
    t = methodQTextClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_2.setAutoDraw(false);
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
    methodQTextComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function methodQTextRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'methodQText'-------
    methodQTextComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var gotValidClick;
var MethodCheckComponents;
function MethodCheckRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'MethodCheck'-------
    t = 0;
    MethodCheckClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    sameText.setText('Same');
    diffText.setText('Different');
    // setup some python lists for storing info about the MethodMouse
    // current position of the mouse:
    MethodMouse.x = [];
    MethodMouse.y = [];
    MethodMouse.leftButton = [];
    MethodMouse.midButton = [];
    MethodMouse.rightButton = [];
    MethodMouse.time = [];
    MethodMouse.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    MethodCheckComponents = [];
    MethodCheckComponents.push(text);
    MethodCheckComponents.push(sameText);
    MethodCheckComponents.push(diffText);
    MethodCheckComponents.push(leftCL);
    MethodCheckComponents.push(rightCL);
    MethodCheckComponents.push(MethodMouse);
    
    MethodCheckComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var prevButtonState;
var _mouseButtons;
var _mouseXYs;
function MethodCheckRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'MethodCheck'-------
    // get current time
    t = MethodCheckClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    
    // *sameText* updates
    if (t >= 0.0 && sameText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sameText.tStart = t;  // (not accounting for frame time here)
      sameText.frameNStart = frameN;  // exact frame index
      
      sameText.setAutoDraw(true);
    }

    
    // *diffText* updates
    if (t >= 0.0 && diffText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      diffText.tStart = t;  // (not accounting for frame time here)
      diffText.frameNStart = frameN;  // exact frame index
      
      diffText.setAutoDraw(true);
    }

    
    // *leftCL* updates
    if (t >= 0.0 && leftCL.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      leftCL.tStart = t;  // (not accounting for frame time here)
      leftCL.frameNStart = frameN;  // exact frame index
      
      leftCL.setAutoDraw(true);
    }

    
    // *rightCL* updates
    if (t >= 0.0 && rightCL.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rightCL.tStart = t;  // (not accounting for frame time here)
      rightCL.frameNStart = frameN;  // exact frame index
      
      rightCL.setAutoDraw(true);
    }

    // *MethodMouse* updates
    if (t >= 0.0 && MethodMouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      MethodMouse.tStart = t;  // (not accounting for frame time here)
      MethodMouse.frameNStart = frameN;  // exact frame index
      
      MethodMouse.status = PsychoJS.Status.STARTED;
      MethodMouse.mouseClock.reset();
      prevButtonState = MethodMouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (MethodMouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = MethodMouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = MethodMouse.getPos();
          MethodMouse.x.push(_mouseXYs[0]);
          MethodMouse.y.push(_mouseXYs[1]);
          MethodMouse.leftButton.push(_mouseButtons[0]);
          MethodMouse.midButton.push(_mouseButtons[1]);
          MethodMouse.rightButton.push(_mouseButtons[2]);
          MethodMouse.time.push(MethodMouse.mouseClock.getTime());
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [rightCL, leftCL]) {
            if (obj.contains(MethodMouse)) {
              gotValidClick = true;
              MethodMouse.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
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
    MethodCheckComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function MethodCheckRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'MethodCheck'-------
    MethodCheckComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    if ((MethodMouse.clicked_name[0] == methodAns)) {
        thisExp.addData("methodCheck", "1");
    } else {
        thisExp.addData("methodCheck", "0");
    }
    
    thisExp.addData("Method Clicked", MethodMouse.clicked_name);
    // store data for thisExp (ExperimentHandler)
    if (MethodMouse.x) {  psychoJS.experiment.addData('MethodMouse.x', MethodMouse.x[0])};
    if (MethodMouse.y) {  psychoJS.experiment.addData('MethodMouse.y', MethodMouse.y[0])};
    if (MethodMouse.leftButton) {  psychoJS.experiment.addData('MethodMouse.leftButton', MethodMouse.leftButton[0])};
    if (MethodMouse.midButton) {  psychoJS.experiment.addData('MethodMouse.midButton', MethodMouse.midButton[0])};
    if (MethodMouse.rightButton) {  psychoJS.experiment.addData('MethodMouse.rightButton', MethodMouse.rightButton[0])};
    if (MethodMouse.time) {  psychoJS.experiment.addData('MethodMouse.time', MethodMouse.time[0])};
    if (MethodMouse.clicked_name) {  psychoJS.experiment.addData('MethodMouse.clicked_name', MethodMouse.clicked_name[0])};
    
    // the Routine "MethodCheck" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var clicked_soundComponents;
function clicked_soundRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'clicked_sound'-------
    t = 0;
    clicked_soundClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    clickedSound = new sound.Sound({
    win: psychoJS.window,
    value: 'click.wav',
    secs: 0.5,
    });
    clickedSound.secs=0.5;
    clickedSound.setVolume(1.0);
    // keep track of which components have finished
    clicked_soundComponents = [];
    clicked_soundComponents.push(clickedSound);
    
    clicked_soundComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function clicked_soundRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'clicked_sound'-------
    // get current time
    t = clicked_soundClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop clickedSound
    if (t >= 0.0 && clickedSound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      clickedSound.tStart = t;  // (not accounting for frame time here)
      clickedSound.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ clickedSound.play(); });  // screen flip
      clickedSound.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (clickedSound.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (0.5 > 0.5) {  clickedSound.stop();  // stop the sound (if longer than duration)
        clickedSound.status = PsychoJS.Status.FINISHED;
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
    clicked_soundComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function clicked_soundRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'clicked_sound'-------
    clicked_soundComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    clickedSound.stop();  // ensure sound has stopped at end of routine
    return Scheduler.Event.NEXT;
  };
}


var retTrials;
var retProb;
var retSame;
var retNew;
var retrievalNew;
var retrievalSame;
var initRecallPicsComponents;
function initRecallPicsRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'initRecallPics'-------
    t = 0;
    initRecallPicsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    retTrials = 0;
    retProb = Math.random();
    retSame = 0;
    retNew = 0;
    
    shuffle(newPics);
    shuffle(samePics);
    //same pics are all pictures that came from 'same' trials
    //shuffle and put in retrieval list.
    retrievalNew = [];
    retrievalSame = [];
    
    retrievalNew.push(newPics);
    retrievalSame.push(samePics);
    // keep track of which components have finished
    initRecallPicsComponents = [];
    
    initRecallPicsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function initRecallPicsRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'initRecallPics'-------
    // get current time
    t = initRecallPicsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    initRecallPicsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function initRecallPicsRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'initRecallPics'-------
    initRecallPicsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "initRecallPics" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var retType;
var retrievalImage;
var RetrievalImageComponents;
function RetrievalImageRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'RetrievalImage'-------
    t = 0;
    RetrievalImageClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    retProb = Math.random();
    if (retProb< 1.1) {
        retType = "old";
        thisExp.addData("retType", "old");
        retrievalImage = (("images/" + samePics[retSame]) + ".png");
        retSame = (retSame + 1);
    //so I am telling it that it needs to take an image from same pics
    //and iterate through those pictures with more retrieval trials
    //no 'new' retrieval at this point.
        } else {
        retType = "new";
        thisExp.addData("retType", "new");
        retrievalImage = (("images/" + newPics[retNew]) + ".png");
        retNew = (retNew + 1);
    }
    thisExp.addData("retIMG", retrievalImage);
    thisExp.addData("Retrieval Type", retType);
    
    retIMG.setImage(retrievalImage);
    sound_pop7 = new sound.Sound({
    win: psychoJS.window,
    value: 'POP.wav',
    secs: -1,
    });
    sound_pop7.setVolume(1.0);
    // keep track of which components have finished
    RetrievalImageComponents = [];
    RetrievalImageComponents.push(retIMG);
    RetrievalImageComponents.push(sound_pop7);
    
    RetrievalImageComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function RetrievalImageRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'RetrievalImage'-------
    // get current time
    t = RetrievalImageClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *retIMG* updates
    if (t >= 0 && retIMG.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      retIMG.tStart = t;  // (not accounting for frame time here)
      retIMG.frameNStart = frameN;  // exact frame index
      
      retIMG.setAutoDraw(true);
    }

    frameRemains = 0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (retIMG.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      retIMG.setAutoDraw(false);
    }
    // start/stop sound_pop7
    if (t >= 0.0 && sound_pop7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_pop7.tStart = t;  // (not accounting for frame time here)
      sound_pop7.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_pop7.play(); });  // screen flip
      sound_pop7.status = PsychoJS.Status.STARTED;
    }
    if (t >= (sound_pop7.getDuration() + sound_pop7.tStart)     && sound_pop7.status === PsychoJS.Status.STARTED) {
      sound_pop7.stop();  // stop the sound (if longer than duration)
      sound_pop7.status = PsychoJS.Status.FINISHED;
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
    RetrievalImageComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function RetrievalImageRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'RetrievalImage'-------
    RetrievalImageComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    sound_pop7.stop();  // ensure sound has stopped at end of routine
    // the Routine "RetrievalImage" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var Q2TextComponents;
function Q2TextRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Q2Text'-------
    t = 0;
    Q2TextClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    Q2TextComponents = [];
    Q2TextComponents.push(question_text);
    
    Q2TextComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Q2TextRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Q2Text'-------
    // get current time
    t = Q2TextClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *question_text* updates
    if (t >= 0.0 && question_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      question_text.tStart = t;  // (not accounting for frame time here)
      question_text.frameNStart = frameN;  // exact frame index
      
      question_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (question_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      question_text.setAutoDraw(false);
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
    Q2TextComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Q2TextRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Q2Text'-------
    Q2TextComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var decTrials;
var DecisionComponents;
function DecisionRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Decision'-------
    t = 0;
    DecisionClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    decTrials = 0;
    // setup some python lists for storing info about the Order_Position_Response
    Order_Position_Response.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    DecisionComponents = [];
    DecisionComponents.push(decisionQ_2);
    DecisionComponents.push(first_left);
    DecisionComponents.push(second_middle);
    DecisionComponents.push(third_right);
    DecisionComponents.push(First);
    DecisionComponents.push(Second);
    DecisionComponents.push(Third);
    DecisionComponents.push(Order_Position_Response);
    
    DecisionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function DecisionRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Decision'-------
    // get current time
    t = DecisionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *decisionQ_2* updates
    if (t >= 0.0 && decisionQ_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      decisionQ_2.tStart = t;  // (not accounting for frame time here)
      decisionQ_2.frameNStart = frameN;  // exact frame index
      
      decisionQ_2.setAutoDraw(true);
    }

    
    // *first_left* updates
    if (t >= 0.0 && first_left.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      first_left.tStart = t;  // (not accounting for frame time here)
      first_left.frameNStart = frameN;  // exact frame index
      
      first_left.setAutoDraw(true);
    }

    
    // *second_middle* updates
    if (t >= 0.0 && second_middle.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      second_middle.tStart = t;  // (not accounting for frame time here)
      second_middle.frameNStart = frameN;  // exact frame index
      
      second_middle.setAutoDraw(true);
    }

    
    // *third_right* updates
    if (t >= 0.0 && third_right.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      third_right.tStart = t;  // (not accounting for frame time here)
      third_right.frameNStart = frameN;  // exact frame index
      
      third_right.setAutoDraw(true);
    }

    
    // *First* updates
    if (t >= 0.0 && First.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      First.tStart = t;  // (not accounting for frame time here)
      First.frameNStart = frameN;  // exact frame index
      
      First.setAutoDraw(true);
    }

    
    // *Second* updates
    if (t >= 0.0 && Second.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Second.tStart = t;  // (not accounting for frame time here)
      Second.frameNStart = frameN;  // exact frame index
      
      Second.setAutoDraw(true);
    }

    
    // *Third* updates
    if (t >= 0.0 && Third.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Third.tStart = t;  // (not accounting for frame time here)
      Third.frameNStart = frameN;  // exact frame index
      
      Third.setAutoDraw(true);
    }

    // *Order_Position_Response* updates
    if (t >= 0.0 && Order_Position_Response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Order_Position_Response.tStart = t;  // (not accounting for frame time here)
      Order_Position_Response.frameNStart = frameN;  // exact frame index
      
      Order_Position_Response.status = PsychoJS.Status.STARTED;
      Order_Position_Response.mouseClock.reset();
      prevButtonState = Order_Position_Response.getPressed();  // if button is down already this ISN'T a new click
      }
    if (Order_Position_Response.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = Order_Position_Response.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [first_left,second_middle,third_right]) {
            if (obj.contains(Order_Position_Response)) {
              gotValidClick = true;
              Order_Position_Response.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
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
    DecisionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function DecisionRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Decision'-------
    DecisionComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    retTrials = (retTrials + 1);
    RetrievalTrials.addData("retTrials", retTrials.toString());
    // store data for thisExp (ExperimentHandler)
    _mouseXYs = Order_Position_Response.getPos();
    _mouseButtons = Order_Position_Response.getPressed();
    psychoJS.experiment.addData('Order_Position_Response.x', _mouseXYs[0]);
    psychoJS.experiment.addData('Order_Position_Response.y', _mouseXYs[1]);
    psychoJS.experiment.addData('Order_Position_Response.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('Order_Position_Response.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('Order_Position_Response.rightButton', _mouseButtons[2]);
    if (Order_Position_Response.clicked_name.length > 0) {
      psychoJS.experiment.addData('Order_Position_Response.clicked_name', Order_Position_Response.clicked_name[0]);}
    // the Routine "Decision" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _start2_allKeys;
var break_2Components;
function break_2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'break_2'-------
    t = 0;
    break_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    start2.keys = undefined;
    start2.rt = undefined;
    _start2_allKeys = [];
    // keep track of which components have finished
    break_2Components = [];
    break_2Components.push(BlockBreak);
    break_2Components.push(text_4);
    break_2Components.push(start2);
    
    break_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function break_2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'break_2'-------
    // get current time
    t = break_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *BlockBreak* updates
    if (t >= 0.0 && BlockBreak.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      BlockBreak.tStart = t;  // (not accounting for frame time here)
      BlockBreak.frameNStart = frameN;  // exact frame index
      
      BlockBreak.setAutoDraw(true);
    }

    frameRemains = 0.0 + 180 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (BlockBreak.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      BlockBreak.setAutoDraw(false);
    }
    
    // *text_4* updates
    if (t >= 180.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }

    
    // *start2* updates
    if (t >= 180.0 && start2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      start2.tStart = t;  // (not accounting for frame time here)
      start2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { start2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { start2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { start2.clearEvents(); });
    }

    if (start2.status === PsychoJS.Status.STARTED) {
      let theseKeys = start2.getKeys({keyList: ['space'], waitRelease: false});
      _start2_allKeys = _start2_allKeys.concat(theseKeys);
      if (_start2_allKeys.length > 0) {
        start2.keys = _start2_allKeys[_start2_allKeys.length - 1].name;  // just the last key pressed
        start2.rt = _start2_allKeys[_start2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
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
    break_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function break_2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'break_2'-------
    break_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('start2.keys', start2.keys);
    if (typeof start2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('start2.rt', start2.rt);
        routineTimer.reset();
        }
    
    start2.stop();
    // the Routine "break_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var EndScreenComponents;
function EndScreenRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'EndScreen'-------
    t = 0;
    EndScreenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    EndScreenComponents = [];
    EndScreenComponents.push(end);
    
    EndScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function EndScreenRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'EndScreen'-------
    // get current time
    t = EndScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *end* updates
    if (t >= 0.0 && end.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end.tStart = t;  // (not accounting for frame time here)
      end.frameNStart = frameN;  // exact frame index
      
      end.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (end.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      end.setAutoDraw(false);
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
    EndScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EndScreenRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'EndScreen'-------
    EndScreenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
