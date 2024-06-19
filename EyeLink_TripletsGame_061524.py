#!/usr/bin/env python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on July 13, 2022, at 13:52
If you publish work using this script the most relevant publication is:
    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y
"""

from __future__ import absolute_import, division
from __future__ import division
from __future__ import print_function

import psychopy
psychopy.useVersion('2021.1.0')
from psychopy import visual, core, event
# the rest of your script follows

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

import pylink
import os
import platform
import random
import time
import sys
from EyeLinkCoreGraphicsPsychoPy import EyeLinkCoreGraphicsPsychoPy
from psychopy import visual, core, event, monitors, gui
from PIL import Image  # for preparing the Host backdrop image
from string import ascii_letters, digits

# Switch to the script folder
script_path = os.path.dirname(sys.argv[0])
if len(script_path) != 0:
    os.chdir(script_path)

# Show only critical log message in the PsychoPy console
from psychopy import logging
logging.console.setLevel(logging.CRITICAL)

# Set this variable to True if you use the built-in retina screen as your
# primary display device on macOS. If have an external monitor, set this
# variable True if you choose to "Optimize for Built-in Retina Display"
# in the Displays preference settings.
use_retina = False

# Set this variable to True to run the script in "Dummy Mode"
dummy_mode = False

# Set this variable to True to run the task in full screen mode
# It is easier to debug the script in non-fullscreen mode
full_screen = True

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'exp'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
    # End the eyetracker session
    terminate_task()

#Store info about eyelink data
edf_fname = expInfo['participant']

# Set up a folder to store the EDF data files and the associated resources
# e.g., files defining the interest areas used in each trial
results_folder = 'results'
if not os.path.exists(results_folder):
    os.makedirs(results_folder)
# We download EDF data file from the EyeLink Host PC to the local hard
# drive at the end of each testing session, here we rename the EDF to
# include session start date/time
time_str = time.strftime("_%Y_%m_%d_%H_%M", time.localtime())
session_identifier = edf_fname + time_str

# create a folder for the current testing session in the "results" folder
session_folder = os.path.join(results_folder, session_identifier)
if not os.path.exists(session_folder):
    os.makedirs(session_folder)

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
#TODO: edit edf name 

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Display\\Desktop\\Eyelink_TripletTask\\Eyelink_TripletsGame.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

## Eyelink Setup
# Step 1: Connect to the EyeLink Host PC
#
# The Host IP address, by default, is "100.1.1.1".
# the "el_tracker" objected created here can be accessed through the Pylink
# Set the Host PC address to "None" (without quotes) to run the script
# in "Dummy Mode"
if dummy_mode:
    el_tracker = pylink.EyeLink(None)
else:
    try:
        el_tracker = pylink.EyeLink("100.1.1.1")
        print('Connection established with eye-tracker');
    except RuntimeError as error:
        print('ERROR:', error)
        core.quit()
        # End the eyetracker session
        terminate_task()
        sys.exit()

# Step 2: Open an EDF data file on the Host PC
edf_file = edf_fname + ".EDF"
try:
    el_tracker.openDataFile(edf_file)
except RuntimeError as err:
    print('ERROR:', err)
    # close the link if we have one open
    if el_tracker.isConnected():
        el_tracker.close()
    core.quit()
    # End the eyetracker session
    terminate_task()
    sys.exit()

# Add a header text to the EDF file to identify the current experiment name
# This is OPTIONAL. If your text starts with "RECORDED BY " it will be
# available in DataViewer's Inspector window by clicking
# the EDF session node in the top panel and looking for the "Recorded By:"
# field in the bottom panel of the Inspector.
preamble_text = 'RECORDED BY %s' % os.path.basename(__file__)
el_tracker.sendCommand("add_file_preamble_text '%s'" % preamble_text)

# Step 3: Configure the tracker
#
# Put the tracker in offline mode before we change tracking parameters
el_tracker.setOfflineMode()

# Get the software version:  1-EyeLink I, 2-EyeLink II, 3/4-EyeLink 1000,
# 5-EyeLink 1000 Plus, 6-Portable DUO
eyelink_ver = 0  # set version to 0, in case running in Dummy mode
if not dummy_mode:
    vstr = el_tracker.getTrackerVersionString()
    eyelink_ver = int(vstr.split()[-1].split('.')[0])
    # print out some version info in the shell
    print('Running experiment on %s, version %d' % (vstr, eyelink_ver))
    
# File and Link data control
# what eye events to save in the EDF file, include everything by default
file_event_flags = 'LEFT,RIGHT,FIXATION,SACCADE,BLINK,MESSAGE,BUTTON,INPUT'
# what eye events to make available over the link, include everything by default
link_event_flags = 'LEFT,RIGHT,FIXATION,SACCADE,BLINK,BUTTON,FIXUPDATE,INPUT'
# what sample data to save in the EDF data file and to make available
# over the link, include the 'HTARGET' flag to save head target sticker
# data for supported eye trackers
if eyelink_ver > 3:
    file_sample_flags = 'LEFT,RIGHT,GAZE,HREF,RAW,AREA,HTARGET,GAZERES,BUTTON,STATUS,INPUT'
    link_sample_flags = 'LEFT,RIGHT,GAZE,GAZERES,AREA,HTARGET,STATUS,INPUT'
else:
    file_sample_flags = 'LEFT,RIGHT,GAZE,HREF,RAW,AREA,GAZERES,BUTTON,STATUS,INPUT'
    link_sample_flags = 'LEFT,RIGHT,GAZE,GAZERES,AREA,STATUS,INPUT'
el_tracker.sendCommand("file_event_filter = %s" % file_event_flags)
el_tracker.sendCommand("file_sample_data = %s" % file_sample_flags)
el_tracker.sendCommand("link_event_filter = %s" % link_event_flags)
el_tracker.sendCommand("link_sample_data = %s" % link_sample_flags)


# Optional tracking parameters
# Sample rate, 250, 500, 1000, or 2000, check your tracker specification
if eyelink_ver > 2:
    el_tracker.sendCommand("sample_rate 500")
# Choose a calibration type, H3, HV3, HV5, HV13 (HV = horizontal/vertical),
el_tracker.sendCommand("calibration_type = HV9")
# Set a gamepad button to accept calibration/drift check target
# You need a supported gamepad/button box that is connected to the Host PC
el_tracker.sendCommand("button_function 5 'accept_target_fixation'")

# Step 4: set up a graphics environment for calibration
#
# Open a window, be sure to specify monitor parameters
mon = monitors.Monitor('myMonitor', width=53.0, distance=70.0)
win = visual.Window(fullscr=full_screen,
                    monitor=mon,
                    winType='pyglet',
                    units='pix')

# get the native screen resolution used by PsychoPy
scn_width, scn_height = win.size
# resolution fix for Mac retina displays
if 'Darwin' in platform.system():
    if use_retina:
        scn_width = int(scn_width/2.0)
        scn_height = int(scn_height/2.0)

# Pass the display pixel coordinates (left, top, right, bottom) to the tracker
# see the EyeLink Installation Guide, "Customizing Screen Settings"
el_coords = "screen_pixel_coords = 0 0 %d %d" % (scn_width - 1, scn_height - 1)
el_tracker.sendCommand(el_coords)

# Write a DISPLAY_COORDS message to the EDF file
# Data Viewer needs this piece of info for proper visualization, see Data
# Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
dv_coords = "DISPLAY_COORDS  0 0 %d %d" % (scn_width - 1, scn_height - 1)
el_tracker.sendMessage(dv_coords)

# Configure a graphics environment (genv) for tracker calibration
genv = EyeLinkCoreGraphicsPsychoPy(el_tracker, win)
print(genv)  # print out the version number of the CoreGraphics library

# Set background and foreground colors for the calibration target
# in PsychoPy, (-1, -1, -1)=black, (1, 1, 1)=white, (0, 0, 0)=mid-gray
foreground_color = (-1, -1, -1)
background_color = win.color
genv.setCalibrationColors(foreground_color, background_color)

# Set up the calibration target
#
# The target could be a "circle" (default), a "picture", a "movie" clip,
# or a rotating "spiral". To configure the type of calibration target, set
# genv.setTargetType to "circle", "picture", "movie", or "spiral", e.g.,
# genv.setTargetType('picture')
#
# Use gen.setPictureTarget() to set a "picture" target
# genv.setPictureTarget(os.path.join('images', 'fixTarget.bmp'))
#
# Use genv.setMovieTarget() to set a "movie" target
# genv.setMovieTarget(os.path.join('videos', 'calibVid.mov'))

# Use a picture as the calibration target
genv.setTargetType('picture')
genv.setPictureTarget(os.path.join('images', 'fixTarget.bmp'))

# Configure the size of the calibration target (in pixels)
# this option applies only to "circle" and "spiral" targets
# genv.setTargetSize(24)

# Beeps to play during calibration, validation and drift correction
# parameters: target, good, error
#     target -- sound to play when target moves
#     good -- sound to play on successful operation
#     error -- sound to play on failure or interruption
# Each parameter could be ''--default sound, 'off'--no sound, or a wav file
genv.setCalibrationSounds('', '', '')

# resolution fix for macOS retina display issues
if use_retina:
    genv.fixMacRetinaDisplay()

# Request Pylink to use the PsychoPy window we opened above for calibration
pylink.openGraphicsEx(genv)
    
    
# define a few helper functions for trial handling


def clear_screen(win):
    """ clear up the PsychoPy window"""

    win.fillColor = genv.getBackgroundColor()
    win.flip()


def show_msg(win, text, wait_for_keypress=True):
    """ Show task instructions on screen"""

    msg = visual.TextStim(win, text,
                          color=genv.getForegroundColor(),
                          wrapWidth=scn_width/2)
    clear_screen(win)
    msg.draw()
    win.flip()

    # wait indefinitely, terminates upon any key press
    if wait_for_keypress:
        event.waitKeys()
        clear_screen(win)


def terminate_task():
    """ Terminate the task gracefully and retrieve the EDF data filenum
    file_to_retrieve: The EDF on the Host that we would like to download
    win: the current window used by the experimental script
    """

    el_tracker = pylink.getEYELINK()

    if el_tracker.isConnected():
        # Terminate the current trial first if the task terminated prematurely
        error = el_tracker.isRecording()
        if error == pylink.TRIAL_OK:
            abort_trial()

        # Put tracker in Offline mode
        el_tracker.setOfflineMode()

        # Clear the Host PC screen and wait for 500 ms
        el_tracker.sendCommand('clear_screen 0')
        pylink.msecDelay(500)
        # Close the edf data file on the Host
        el_tracker.closeDataFile()

        # Show a file transfer message on the screen
        #msg = 'EDF data is transferring from EyeLink Host PC...'
        #show_msg(win, msg, wait_for_keypress=False)

        # Download the EDF data file from the Host PC to a local data folder
        # parameters: source_file_on_the_host, destination_file_on_local_drive
        local_edf = os.path.join(session_folder, session_identifier + '.EDF')
        try:
            el_tracker.receiveDataFile(edf_file, local_edf)
        except RuntimeError as error:
            print('ERROR:', error)

        # Close the link to the tracker.
        el_tracker.close()
        print('closed')

    # close the PsychoPy window
    win.close()
    # End the eyetracker session
   # terminate_task()
    # quit PsychoPy
    #save psychopy
    thisExp.saveAsWideText(filename+'.csv', delim=',')
    thisExp.saveAsPickle(filename)
    logging.flush()
    core.quit()
    
    sys.exit()


def abort_trial():
    """Ends recording """

    el_tracker = pylink.getEYELINK()

    # Stop recording
    if el_tracker.isRecording():
        # add 100 ms to catch final trial events
        pylink.pumpDelay(100)
        el_tracker.stopRecording()

    # clear the screen
    clear_screen(win)
    # Send a message to clear the Data Viewer screen
    bgcolor_RGB = (116, 116, 116)
    el_tracker.sendMessage('!V CLEAR %d %d %d' % bgcolor_RGB)

    # send a message to mark trial end
    el_tracker.sendMessage('TRIAL_RESULT %d' % pylink.TRIAL_ERROR)

    return pylink.TRIAL_ERROR

def start_eye_tracker(trial_index, trial_type):
    # get a reference to the currently active EyeLink connection
    el_tracker = pylink.getEYELINK()
    # put the tracker in the offline mode first
    el_tracker.setOfflineMode()
    # clear the host screen before we draw the backdrop
    el_tracker.sendCommand('clear_screen 0')
    # send a "TRIALID" message to mark the start of a trial, see Data
    # Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
    if trial_type=='encoding':    
        el_tracker.sendMessage('trialIndex %d' % trial_index)
        # record_status_message : show some info on the Host PC
        # here we show how many trial has been tested
        status_msg = 'eTrial number %d' % trial_index
        print(status_msg)
    elif trial_type=='retrieval':
        el_tracker.sendMessage('trialIndex %d' % rtrial_index)
        # record_status_message : show some info on the Host PC
        # here we show how many trial has been tested
        status_msg = 'retTrial number %d' % rtrial_index
        print(status_msg)

    el_tracker.sendCommand("record_status_message '%s'" % status_msg)
    
    #messages for when the images appear

    
    # drift check
    # we recommend drift-check at the beginning of each trial
    # the doDriftCorrect() function requires target position in integers
    # the last two arguments:
    # draw_target (1-default, 0-draw the target then call doDriftCorrect)
    # allow_setup (1-press ESCAPE to recalibrate, 0-not allowed)
    #
    # Skip drift-check if running the script in Dummy Mode
    while not dummy_mode:
        # terminate the task if no longer connected to the tracker or
        # user pressed Ctrl-C to terminate the task
        if (not el_tracker.isConnected()) or el_tracker.breakPressed():
            terminate_task()
            return pylink.ABORT_EXPT
        break
        # # drift-check and re-do camera setup if ESCAPE is pressed
        # try:
        #     error = el_tracker.doDriftCorrect(int(scn_width/2.0),
        #                                       int(scn_height/2.0), 1, 1)
        #     print('2')

        #     # break following a success drift-check
        #     if error is not pylink.ESC_KEY:
        #         break
        # except:
        #     pass

    # put tracker in idle/offline mode before recording
    el_tracker.setOfflineMode()

    # Start recording
    # arguments: sample_to_file, events_to_file, sample_over_link,
    # event_over_link (1-yes, 0-no)
    try:
        el_tracker.startRecording(1, 1, 1, 1)

    except RuntimeError as error:
        print("ERROR:", error)
        abort_trial()
        return pylink.TRIAL_ERROR

    # Allocate some time for the tracker to cache some samples
    pylink.pumpDelay(100)
   # print('are things working fine')
    

# Step 5: Set up the camera and calibrate the tracker

# Show the task instructions
task_msg = 'In the task, you may press the SPACEBAR to end a trial\n' + \
    '\nPress Ctrl-C to if you need to quit the task early\n'
if dummy_mode:
    task_msg = task_msg + '\nNow, press ENTER to start the task'
else:
    task_msg = task_msg + '\nNow, press ENTER twice to calibrate tracker'
show_msg(win, task_msg)

# skip this step if running the script in Dummy Mode
if not dummy_mode:
    try:
        el_tracker.doTrackerSetup()
    except RuntimeError as err:
        print('ERROR:', err)
        el_tracker.exitCalibration()
    
# Start Code - component code to be run after the window creation
# Setup the Window
win = visual.Window(
    size=[1280, 720], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "initCode"
initCodeClock = core.Clock()
import random, csv, os, codecs
#set random seed
random.seed()

#define rest of the variables
retProb = random.random()
rightPos = None
midPos = None
leftPos = None
firstPos = None
secondPos = None
thirdPos = None
TestQuestion = None
MouseResp = None
trialType = None
methodAns = None
nextTrial = None
methodCheck = None
retrievalImage = None
response = None
corrAns = None
decResponse = None
encodingType = None
trialPics = []
retrievalOld = []
retrievalNew = []

# Initialize components for Routine "trial"
trialClock = core.Clock()
Instructions = visual.TextStim(win=win, name='Instructions',
    text='In this task you will review sets of objects in triplets. Your task is to pay attention to where and when these objects appear. Press the spacebar to begin.',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
start = keyboard.Keyboard()

# Initialize components for Routine "first_view"
first_viewClock = core.Clock()
Triplet1 = visual.ImageStim(
    win=win,
    name='Triplet1', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Triplet2 = visual.ImageStim(
    win=win,
    name='Triplet2', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
Triplet3 = visual.ImageStim(
    win=win,
    name='Triplet3', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
sound_pop = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_pop')
sound_pop.setVolume(1.0)
sound_pop2 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_pop2')
sound_pop2.setVolume(1.0)
sound_pop3 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_pop3')
sound_pop3.setVolume(1.0)

# Initialize components for Routine "fix"
fixClock = core.Clock()
fix = visual.ImageStim(
    win=win,
    name='fix', 
    image='images/fixation.png', mask=None,
    ori=0, pos=(0, 0), size=(0.1, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "mask"
maskClock = core.Clock()
Mask = visual.ImageStim(
    win=win,
    name='Mask', 
    image='images/Mask.png', mask=None,
    ori=0, pos=(0, 0), size=(1.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "second_view"
second_viewClock = core.Clock()
img1 = visual.ImageStim(
    win=win,
    name='img1', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
img2 = visual.ImageStim(
    win=win,
    name='img2', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
img3 = visual.ImageStim(
    win=win,
    name='img3', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
sound_pop4 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_pop4')
sound_pop4.setVolume(1.0)
sound_pop5 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_pop5')
sound_pop5.setVolume(1.0)
sound_pop6 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_pop6')
sound_pop6.setVolume(1.0)

# Initialize components for Routine "methodQText"
methodQTextClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Was this set same or different as the previous set?',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "MethodCheck"
MethodCheckClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Was this set same or different as the previous set?',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
sameText = visual.TextStim(win=win, name='sameText',
    text='',
    font='Arial',
    pos=(-0.2, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
diffText = visual.TextStim(win=win, name='diffText',
    text='',
    font='Arial',
    pos=(0.2, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
leftCL = visual.Rect(
    win=win, name='leftCL',
    width=(-0.2, -0.2)[0], height=(-0.2, -0.2)[1],
    ori=0, pos=(-.2, -.3),
    lineWidth=3,     colorSpace='rgb',  lineColor='white', fillColor=(1.0000, 1.0000, 1.0000),
    opacity=0.5, depth=-4.0, interpolate=True)
rightCL = visual.Rect(
    win=win, name='rightCL',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0, pos=(0.2, -0.3),
    lineWidth=3,     colorSpace='rgb',  lineColor='white', fillColor=(1.0000, 1.0000, 1.0000),
    opacity=0.5, depth=-5.0, interpolate=True)
MethodMouse = event.Mouse(win=win)
x, y = [None, None]
MethodMouse.mouseClock = core.Clock()

# Initialize components for Routine "clicked_sound"
clicked_soundClock = core.Clock()
clickedSound = sound.Sound('A', secs=0.5, stereo=True, hamming=True,
    name='clickedSound')
clickedSound.setVolume(1.0)

# Initialize components for Routine "initRecallPics"
initRecallPicsClock = core.Clock()

# Initialize components for Routine "initRecallPics2"
initRecallPics2Clock = core.Clock()

# Initialize components for Routine "RetrievalImage"
RetrievalImageClock = core.Clock()
retIMG = visual.ImageStim(
    win=win,
    name='retIMG', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
sound_pop7 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_pop7')
sound_pop7.setVolume(1.0)

# Initialize components for Routine "Q2Text"
Q2TextClock = core.Clock()
question_text = visual.TextStim(win=win, name='question_text',
    text='When did you see this object?',
    font='Arial',
    pos=(0, 0.3), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Decision"
DecisionClock = core.Clock()
decisionQ_2 = visual.TextStim(win=win, name='decisionQ_2',
    text='When did you see this object?',
    font='Arial',
    pos=(0, 0.3), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
first_left = visual.Rect(
    win=win, name='first_left',
    width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
    ori=0, pos=(0, 0.1),
    lineWidth=3,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=0.5, depth=-2.0, interpolate=True)
second_middle = visual.Rect(
    win=win, name='second_middle',
    width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
    ori=0, pos=(0, -0.1),
    lineWidth=3,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=0.5, depth=-3.0, interpolate=True)
third_right = visual.Rect(
    win=win, name='third_right',
    width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
    ori=0, pos=(0, -0.3),
    lineWidth=3,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=0.5, depth=-4.0, interpolate=True)
First = visual.TextStim(win=win, name='First',
    text='First',
    font='Arial',
    pos=(0, 0.1), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
Second = visual.TextStim(win=win, name='Second',
    text='Second',
    font='Arial',
    pos=(0, -0.1), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
Third = visual.TextStim(win=win, name='Third',
    text='Third',
    font='Arial',
    pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
Order_Position_Response = event.Mouse(win=win)
x, y = [None, None]
Order_Position_Response.mouseClock = core.Clock()

# Initialize components for Routine "clicked_sound"
clicked_soundClock = core.Clock()
clickedSound = sound.Sound('A', secs=0.5, stereo=True, hamming=True,
    name='clickedSound')
clickedSound.setVolume(1.0)

# Initialize components for Routine "break_2"
break_2Clock = core.Clock()
BlockBreak = visual.TextStim(win=win, name='BlockBreak',
    text='You are done with the first portion of the task!\n\nNow, you have a three minute break. When the time is over, you will answer some questions.',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='In this task you will review sets of objects in triplets. Your task is to pay attention to where and when these objects appear. Press the spacebar to begin.',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
start2 = keyboard.Keyboard()

# Initialize components for Routine "first_view"
first_viewClock = core.Clock()
Triplet1 = visual.ImageStim(
    win=win,
    name='Triplet1', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Triplet2 = visual.ImageStim(
    win=win,
    name='Triplet2', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
Triplet3 = visual.ImageStim(
    win=win,
    name='Triplet3', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
sound_pop = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_pop')
sound_pop.setVolume(1.0)
sound_pop2 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_pop2')
sound_pop2.setVolume(1.0)
sound_pop3 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_pop3')
sound_pop3.setVolume(1.0)

# Initialize components for Routine "fix"
fixClock = core.Clock()
fix = visual.ImageStim(
    win=win,
    name='fix', 
    image='images/fixation.png', mask=None,
    ori=0, pos=(0, 0), size=(0.1, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "mask"
maskClock = core.Clock()
Mask = visual.ImageStim(
    win=win,
    name='Mask', 
    image='images/Mask.png', mask=None,
    ori=0, pos=(0, 0), size=(1.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "second_view"
second_viewClock = core.Clock()
img1 = visual.ImageStim(
    win=win,
    name='img1', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
img2 = visual.ImageStim(
    win=win,
    name='img2', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
img3 = visual.ImageStim(
    win=win,
    name='img3', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
sound_pop4 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_pop4')
sound_pop4.setVolume(1.0)
sound_pop5 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_pop5')
sound_pop5.setVolume(1.0)
sound_pop6 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_pop6')
sound_pop6.setVolume(1.0)

# Initialize components for Routine "methodQText"
methodQTextClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Was this set same or different as the previous set?',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "MethodCheck"
MethodCheckClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Was this set same or different as the previous set?',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
sameText = visual.TextStim(win=win, name='sameText',
    text='',
    font='Arial',
    pos=(-0.2, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
diffText = visual.TextStim(win=win, name='diffText',
    text='',
    font='Arial',
    pos=(0.2, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
leftCL = visual.Rect(
    win=win, name='leftCL',
    width=(-0.2, -0.2)[0], height=(-0.2, -0.2)[1],
    ori=0, pos=(-.2, -.3),
    lineWidth=3,     colorSpace='rgb',  lineColor='white', fillColor=(1.0000, 1.0000, 1.0000),
    opacity=0.5, depth=-4.0, interpolate=True)
rightCL = visual.Rect(
    win=win, name='rightCL',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0, pos=(0.2, -0.3),
    lineWidth=3,     colorSpace='rgb',  lineColor='white', fillColor=(1.0000, 1.0000, 1.0000),
    opacity=0.5, depth=-5.0, interpolate=True)
MethodMouse = event.Mouse(win=win)
x, y = [None, None]
MethodMouse.mouseClock = core.Clock()

# Initialize components for Routine "clicked_sound"
clicked_soundClock = core.Clock()
clickedSound = sound.Sound('A', secs=0.5, stereo=True, hamming=True,
    name='clickedSound')
clickedSound.setVolume(1.0)

# Initialize components for Routine "RetrievalImage"
RetrievalImageClock = core.Clock()
retIMG = visual.ImageStim(
    win=win,
    name='retIMG', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
sound_pop7 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_pop7')
sound_pop7.setVolume(1.0)

# Initialize components for Routine "Q2Text"
Q2TextClock = core.Clock()
question_text = visual.TextStim(win=win, name='question_text',
    text='When did you see this object?',
    font='Arial',
    pos=(0, 0.3), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Decision"
DecisionClock = core.Clock()
decisionQ_2 = visual.TextStim(win=win, name='decisionQ_2',
    text='When did you see this object?',
    font='Arial',
    pos=(0, 0.3), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
first_left = visual.Rect(
    win=win, name='first_left',
    width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
    ori=0, pos=(0, 0.1),
    lineWidth=3,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=0.5, depth=-2.0, interpolate=True)
second_middle = visual.Rect(
    win=win, name='second_middle',
    width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
    ori=0, pos=(0, -0.1),
    lineWidth=3,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=0.5, depth=-3.0, interpolate=True)
third_right = visual.Rect(
    win=win, name='third_right',
    width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
    ori=0, pos=(0, -0.3),
    lineWidth=3,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=0.5, depth=-4.0, interpolate=True)
First = visual.TextStim(win=win, name='First',
    text='First',
    font='Arial',
    pos=(0, 0.1), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
Second = visual.TextStim(win=win, name='Second',
    text='Second',
    font='Arial',
    pos=(0, -0.1), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
Third = visual.TextStim(win=win, name='Third',
    text='Third',
    font='Arial',
    pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
Order_Position_Response = event.Mouse(win=win)
x, y = [None, None]
Order_Position_Response.mouseClock = core.Clock()

# Initialize components for Routine "clicked_sound"
clicked_soundClock = core.Clock()
clickedSound = sound.Sound('A', secs=0.5, stereo=True, hamming=True,
    name='clickedSound')
clickedSound.setVolume(1.0)

# Initialize components for Routine "EndScreen"
EndScreenClock = core.Clock()
end = visual.TextStim(win=win, name='end',
    text='You are done with this task! Thank you for participating!',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#Initialization routine
# ------Prepare to start Routine "initCode"-------
continueRoutine = True
# update component parameters for each repeat
allPics = ['OBJ_1','OBJ_2','OBJ_3','OBJ_4','OBJ_5','OBJ_6','OBJ_7','OBJ_8','OBJ_9','OBJ_10','OBJ_11','OBJ_12','OBJ_13','OBJ_14','OBJ_15','OBJ_16','OBJ_17','OBJ_18','OBJ_19','OBJ_20','OBJ_21','OBJ_22','OBJ_23','OBJ_24','OBJ_25','OBJ_26','OBJ_28','OBJ_29','OBJ_30','OBJ_31','OBJ_32','OBJ_33','OBJ_35','OBJ_36','OBJ_37','OBJ_38','OBJ_39','OBJ_40','OBJ_41','OBJ_42','OBJ_43','OBJ_44','OBJ_45','OBJ_46','OBJ_47','OBJ_48','OBJ_49','OBJ_50','OBJ_51','OBJ_52','OBJ_53','OBJ_54','OBJ_55','OBJ_56','OBJ_57','OBJ_58','OBJ_59','OBJ_60','OBJ_61','OBJ_63','OBJ_64','OBJ_65','OBJ_66','OBJ_67','OBJ_68','OBJ_69','OBJ_70','OBJ_71','OBJ_72','OBJ_73','OBJ_74','OBJ_75','OBJ_77','OBJ_78','OBJ_79','OBJ_80','OBJ_81','OBJ_82','OBJ_83','OBJ_84','OBJ_85','OBJ_86','OBJ_87','OBJ_88','OBJ_89','OBJ_91','OBJ_92','OBJ_93','OBJ_94','OBJ_95','OBJ_96','OBJ_97','OBJ_98','OBJ_99','OBJ_100','OBJ_101','OBJ_102','OBJ_103','OBJ_104','OBJ_105','OBJ_106','OBJ_107','OBJ_109','OBJ_110','OBJ_111','OBJ_112','OBJ_113','OBJ_114','OBJ_115','OBJ_116','OBJ_119','OBJ_120','OBJ_121','OBJ_123','OBJ_125','OBJ_126','OBJ_128','OBJ_129','OBJ_130','OBJ_131','OBJ_133','OBJ_134','OBJ_135','OBJ_136','OBJ_137','OBJ_138','OBJ_139','OBJ_140','OBJ_141','OBJ_142','OBJ_143','OBJ_144','OBJ_145','OBJ_146','OBJ_147','OBJ_148','OBJ_149','OBJ_150','OBJ_151','OBJ_152','OBJ_153','OBJ_154','OBJ_155','OBJ_156','OBJ_157','OBJ_158','OBJ_160','OBJ_161','OBJ_163','OBJ_164','OBJ_165','OBJ_166','OBJ_167','OBJ_168','OBJ_170','OBJ_171','OBJ_172','OBJ_173','OBJ_174','OBJ_175','OBJ_177','OBJ_178','OBJ_179','OBJ_181','OBJ_182','OBJ_183','OBJ_184','OBJ_186','OBJ_187','OBJ_188','OBJ_189','OBJ_190','OBJ_191','OBJ_193','OBJ_194','OBJ_195','OBJ_196','OBJ_197','OBJ_198','OBJ_199','OBJ_200','OBJ_202','OBJ_203','OBJ_204','OBJ_205','OBJ_206','OBJ_208','OBJ_209','OBJ_210'];
#trialTypes= ["LMR","LMR","LMR","LMR","LMR","LMR","LMR","LMR","RML","RML","RML","RML","RML","RML","RML","RML" ,"MLR","MLR","MRL","MRL","LRM","LRM", "RLM", "RLM","RLM","LMR","LMR","LMR","LMR","LMR","LMR","LMR","LMR","RML","RML","RML","RML","RML","RML","RML","RML" ,"MLR","MLR","MRL","MRL","LRM","LRM", "LRM", "RLM","RLM"];
sameDiff = ["same","same","same","same","same","same","same","same","same","same","same","same","same","same","same","same","same","same","same","same","diff","diff","diff","diff","diff"];
shuffle(allPics)
shuffle(sameDiff)
#shuffle(trialTypes)

#So for the same trials:
# Define the strings
fixed_strings = ['LMR', 'RML']  # These will occur 7 times each
other_strings = ['MLR', 'MRL', 'LRM', 'RLM']  # These will be randomly selected to have total of 7 also

# Select 7 strings from other_strings with repetitions
selected_strings = random.choices(other_strings, k=9)

# Create a list to store the strings
sameTrials = fixed_strings * 9  # Repeating fixed_strings 9 times
sameTrials += selected_strings  # Adding the selected 9 strings

# Shuffle the list
random.shuffle(sameTrials)

# Print the randomized list
print("Randomized string list:")
print(sameTrials) #now this should be a list of 27 that we will run 20 of, but because it is indexed by eTrials, there needs to be more than 25 items. 

#for the different trials:
diffTrials = fixed_strings * 9  # Repeating fixed_strings 9 times
diffTrials += selected_strings  # Adding the selected 9 strings

# Shuffle the list
random.shuffle(diffTrials)

# Print the selected strings)
print(diffTrials) #because these are indexed by eTrials while they select the images, they need to be more than 25 items

#hard-coded names of all images and trial types (counterbalanced).
numItems = 210
#numTotencoding = 50
numEncodingBlock1 = 3
numEncodingBlock2 = 3
numTotretrieval = 4
numRetrieval1 = 2
numRetrieval2 = 2

# create final stimuli list
for i in range(0, numItems, 3):
    # make triplet
    trialPics.append(allPics[i:i+3])
    diffTrials += selected_strings
#70 triplets made from 210 images.

# these triplets will be shown during encoding
# Create indices for selecting triplets for each block
indices_block1 = random.sample(range(len(allPics) // 3), numEncodingBlock1)
indices_block2 = random.sample(set(range(len(allPics) // 3)) - set(indices_block1), numEncodingBlock2)

# Create encodingPics for each block using the selected indices
encodingPics1 = [allPics[i * 3:i * 3 + 3] for i in indices_block1]
encodingPics2 = [allPics[i * 3:i * 3 + 3] for i in indices_block2]

# Now you have unique sets of triplets for each block
print(encodingPics1)
print(encodingPics2)


samePics = []
#diffPics = []
samePics2 = [] #for block 2
#this is where I will store the images from same and diff trials so we know which ones to use for retrieval
eTrials = 0
TRIAL_INDEX = 0

# keep track of which components have finished
initCodeComponents = []
for thisComponent in initCodeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
initCodeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "initCode"-------
while continueRoutine:
    # get current time
    t = initCodeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=initCodeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        thisExp.saveAsWideText(filename+'.csv', delim=',')
        thisExp.saveAsPickle(filename)
        logging.flush()
        terminate_task()
        core.quit()

    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in initCodeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "initCode"-------
for thisComponent in initCodeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "initCode" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial"-------
continueRoutine = True
# update component parameters for each repeat
start.keys = []
start.rt = []
_start_allKeys = []
# keep track of which components have finished
trialComponents = [Instructions, start]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial"-------
while continueRoutine:
    # get current time
    t = trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instructions* updates
    if Instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructions.frameNStart = frameN  # exact frame index
        Instructions.tStart = t  # local t and not account for scr refresh
        Instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructions, 'tStartRefresh')  # time at next scr refresh
        Instructions.setAutoDraw(True)
    
    # *start* updates
    waitOnFlip = False
    if start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start.frameNStart = frameN  # exact frame index
        start.tStart = t  # local t and not account for scr refresh
        start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start, 'tStartRefresh')  # time at next scr refresh
        start.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(start.clock.reset)  # t=0 on next screen flip
    if start.status == STARTED and not waitOnFlip:
        theseKeys = start.getKeys(keyList=['space', 'q'], waitRelease=False)
        _start_allKeys.extend(theseKeys)
        if len(_start_allKeys):
            start.keys = _start_allKeys[-1].name  # just the last key pressed
            start.rt = _start_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        thisExp.saveAsWideText(filename+'.csv', delim=',')
        thisExp.saveAsPickle(filename)
        logging.flush()
        terminate_task()
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
EncodingTrials = data.TrialHandler(nReps=numEncodingBlock1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='EncodingTrials')
thisExp.addLoop(EncodingTrials)  # add the loop to the experiment
thisEncodingTrial = EncodingTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEncodingTrial.rgb)
if thisEncodingTrial != None:
    for paramName in thisEncodingTrial:
        exec('{} = thisEncodingTrial[paramName]'.format(paramName))
# record category of trial: encoding/retrieval
for thisEncodingTrial in EncodingTrials:
    trial_category = 'encoding'
    currentLoop = EncodingTrials
    # abbreviate parameter names if possible (e.g. rgb = thisEncodingTrial.rgb)
    if thisEncodingTrial != None:
        for paramName in thisEncodingTrial:
            exec('{} = thisEncodingTrial[paramName]'.format(paramName))
 
#First encoding block starts
# ------Prepare to start Routine "fix"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    trial_index = EncodingTrials.thisRepN
    #start recording eye-movements
    start_eye_tracker(trial_index, trial_category)
    # send a "TRIALID" message to mark the start of a trial, see Data
    # Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
    el_tracker.sendMessage('trialIndex %d' % trial_index) #HERE
    
    # update component parameters for each repeat
    # keep track of which components have finished
    fixComponents = [fix]
    for thisComponent in fixComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fix"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *"fix"* updates
        if fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix.frameNStart = frameN  # exact frame index
            fix.tStart = t  # local t and not account for scr refresh
            fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
            fix.setAutoDraw(True)
        if fix.status == STARTED:
            el_tracker.sendMessage('fixation %s' % fixClock.getTime())
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                fix.tStop = t  # not accounting for scr refresh
                fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix, 'tStopRefresh')  # time at next scr refresh
                fix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.saveAsWideText(filename+'.csv', delim=',')
            thisExp.saveAsPickle(filename)
            logging.flush()
            terminate_task()
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fix"-------
    for thisComponent in fixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    el_tracker.sendMessage('fixationEnd %s' % fixClock.getTime())
    
    
    # ------Prepare to start Routine "first_view"-------
    continueRoutine = True
    #start recording eye-movements
    trial_index = EncodingTrials.thisRepN
    el_tracker.sendMessage('!V TRIAL_VAR participant_ID %s' % expInfo['participant'])
    el_tracker.sendMessage('!V TRIAL_VAR trialcategory %s' %trial_category)
    el_tracker.sendMessage('!V TRIAL_VAR trialIndex %d' %trial_index)
    
    # update component parameters for each repeat
    import os
    #iterate through trial type and set a new one for each trial
    method_Trial = sameDiff[eTrials]
    if method_Trial == "same":
        trialType = sameTrials[eTrials]
    else:
            trialType = diffTrials[eTrials]
    el_tracker.sendMessage('!V TRIAL_VAR trialType %s' %trialType)
    
    #positions
    leftPos = -0.5, 0.0
    midPos = 0.0, 0.0
    rightPos = 0.5, 0.0
    
    if trialType == 'LMR':
        firstPos = leftPos
        secondPos = midPos
        thirdPos = rightPos
    elif trialType == 'LRM':
        firstPos = leftPos
        secondPos = rightPos
        thirdPos = midPos
    elif trialType == 'MLR':
        firstPos = midPos
        secondPos = leftPos
        thirdPos = rightPos
    elif trialType == 'RML':
        firstPos = rightPos
        secondPos = midPos
        thirdPos = leftPos
    elif trialType == 'RLM':
        firstPos = rightPos
        secondPos = leftPos
        thirdPos = midPos
    elif trialType == 'MRL':
        firstPos = midPos
        secondPos = rightPos
        thirdPos = leftPos
    
    #set images in triplets
    triplet1 = 'images/'+encodingPics1[eTrials][0]+'.png'
    triplet2 = 'images/'+encodingPics1[eTrials][1]+'.png'
    triplet3 = 'images/'+encodingPics1[eTrials][2]+'.png'
    
    EncodingTrials.addData ("Trial_Order", trialType)
    thisExp.addData("triplet1", triplet1)
    thisExp.addData("triplet2", triplet2)
    thisExp.addData("triplet3", triplet3)
    Triplet1.setPos(firstPos)
    Triplet1.setImage(triplet1)
    Triplet2.setPos(secondPos)
    Triplet2.setImage(triplet2)
    Triplet3.setPos(thirdPos)
    Triplet3.setImage(triplet3)
    #comment or delete?
    Triplet1.setPos(firstPos)
    Triplet1.setImage(triplet1)
    Triplet2.setPos(secondPos)
    Triplet2.setImage(triplet2)
    Triplet3.setPos(thirdPos)
    Triplet3.setImage(triplet3)
    sound_pop.setSound('POP.wav', hamming=True)
    sound_pop.setVolume(1.0, log=False)
    sound_pop2.setSound('POP.wav', hamming=True)
    sound_pop2.setVolume(1.0, log=False)
    sound_pop3.setSound('POP.wav', hamming=True)
    sound_pop3.setVolume(1.0, log=False)
    # keep track of which components have finished
    first_viewComponents = [Triplet1, Triplet2, Triplet3, sound_pop, sound_pop2, sound_pop3]
    for thisComponent in first_viewComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    first_viewClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "first_view"-------
    while continueRoutine:
        # get current time
        t = first_viewClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=first_viewClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *Triplet1* updates
        if Triplet1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Triplet1.frameNStart = frameN  # exact frame index
            Triplet1.tStart = t  # local t and not account for scr refresh
            Triplet1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Triplet1, 'tStartRefresh')  # time at next scr refresh
            Triplet1.setAutoDraw(True)
        if Triplet1.status == STARTED:
            el_tracker.sendMessage('Triplet1.running %s' % first_viewClock.getTime())
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Triplet1.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                Triplet1.tStop = t  # not accounting for scr refresh
                Triplet1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Triplet1, 'tStopRefresh')  # time at next scr refresh
                Triplet1.setAutoDraw(False)
                
        
        # *Triplet2* updates
        if Triplet2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            Triplet2.frameNStart = frameN  # exact frame index
            Triplet2.tStart = t  # local t and not account for scr refresh
            Triplet2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Triplet2, 'tStartRefresh')  # time at next scr refresh
            Triplet2.setAutoDraw(True)
        if Triplet2.status == STARTED:
            el_tracker.sendMessage('Triplet2.running %s' % first_viewClock.getTime())
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Triplet2.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                Triplet2.tStop = t  # not accounting for scr refresh
                Triplet2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Triplet2, 'tStopRefresh')  # time at next scr refresh
                Triplet2.setAutoDraw(False)
                
        
        # *Triplet3* updates
        if Triplet3.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            Triplet3.frameNStart = frameN  # exact frame index
            Triplet3.tStart = t  # local t and not account for scr refresh
            Triplet3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Triplet3, 'tStartRefresh')  # time at next scr refresh
            Triplet3.setAutoDraw(True)
        if Triplet3.status == STARTED:
            el_tracker.sendMessage('Triplet3.running %s' % first_viewClock.getTime())
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Triplet3.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                Triplet3.tStop = t  # not accounting for scr refresh
                Triplet3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Triplet3, 'tStopRefresh')  # time at next scr refresh
                Triplet3.setAutoDraw(False)
                #print("got here")
        # start/stop sound_pop
        if sound_pop.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            sound_pop.frameNStart = frameN  # exact frame index
            sound_pop.tStart = t  # local t and not account for scr refresh
            sound_pop.tStartRefresh = tThisFlipGlobal  # on global time
            sound_pop.play(when=win)  # sync with win flip
        # start/stop sound_pop2
        if sound_pop2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            sound_pop2.frameNStart = frameN  # exact frame index
            sound_pop2.tStart = t  # local t and not account for scr refresh
            sound_pop2.tStartRefresh = tThisFlipGlobal  # on global time
            sound_pop2.play(when=win)  # sync with win flip
        # start/stop sound_pop3
        if sound_pop3.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            sound_pop3.frameNStart = frameN  # exact frame index
            sound_pop3.tStart = t  # local t and not account for scr refresh
            sound_pop3.tStartRefresh = tThisFlipGlobal  # on global time
            sound_pop3.play(when=win)  # sync with win flip
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.saveAsWideText(filename+'.csv', delim=',')
            thisExp.saveAsPickle(filename)
            logging.flush()
            terminate_task()
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in first_viewComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "first_view"-------
    for thisComponent in first_viewComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_pop.stop()  # ensure sound has stopped at end of routine)
    sound_pop2.stop()  # ensure sound has stopped at end of routine
    sound_pop3.stop()  # ensure sound has stopped at end of routine
    el_tracker.sendMessage('firstviewEnding %s' % first_viewClock.getTime())
    # stop recording eye movements
   
    # the Routine "first_view" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "mask"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    maskComponents = [Mask]
    for thisComponent in maskComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    maskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "mask"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = maskClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=maskClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        el_tracker.sendMessage('mask %s' % Mask)

        # *Mask* updates
        if Mask.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Mask.frameNStart = frameN  # exact frame index
            Mask.tStart = t  # local t and not account for scr refresh
            Mask.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Mask, 'tStartRefresh')  # time at next scr refresh
            Mask.setAutoDraw(True)
        if Mask.status == STARTED:
            el_tracker.sendMessage('Mask.running %s' % maskClock.getTime())
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Mask.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                Mask.tStop = t  # not accounting for scr refresh
                Mask.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Mask, 'tStopRefresh')  # time at next scr refresh
                Mask.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.saveAsWideText(filename+'.csv', delim=',')
            thisExp.saveAsPickle(filename)
            logging.flush()
            terminate_task()
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in maskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "mask"-------
    for thisComponent in maskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    el_tracker.sendMessage('maskEnd %s' % maskClock.getTime()) 
    # ------Prepare to start Routine "second_view"-------
    continueRoutine = True
    # update component parameters for each repeat
    if method_Trial == "same":
        list = [0,1,2]
        random.shuffle(list)
        samePics.append(encodingPics1[eTrials][list[0]])
        EncodingTrials.addData("encodingType","same")
        encodingType = 'same'
    else:
        nextTrial = random.choice(diffTrials)
        while nextTrial == trialType:
            nextTrial = random.choice(diffTrials)
            end
        trialType = nextTrial
        methodAns = ['rightCL'] #different
        list = [0,1,2]
        random.shuffle(list)
        triplet1 = 'images/'+encodingPics1[eTrials][list[0]]+'.png'
        triplet2 = 'images/'+encodingPics1[eTrials][list[1]]+'.png'
        triplet3 = 'images/'+encodingPics1[eTrials][list[2]]+'.png'
        EncodingTrials.addData("encodingType","diff")
        encodingType = 'diff'
        
    el_tracker.sendMessage('!V TRIAL_VAR encodingType %s' %encodingType)
    el_tracker.sendMessage('!V TRIAL_VAR nextTrial %s' %nextTrial)
    el_tracker.sendMessage('!V TRIAL_VAR triplet1 %s' %triplet1)
    el_tracker.sendMessage('!V TRIAL_VAR triplet2 %s' %triplet2)
    el_tracker.sendMessage('!V TRIAL_VAR triplet3 %s' %triplet3)

 #have to re-state positions and trial types
    if trialType == 'LMR':
        firstPos = leftPos
        secondPos = midPos
        thirdPos = rightPos
    elif trialType == 'LRM':
        firstPos = leftPos
        secondPos = rightPos
        thirdPos = midPos
    elif trialType == 'MLR':
        firstPos = midPos
        secondPos = leftPos
        thirdPos = rightPos
    elif trialType == 'RML':
        firstPos = rightPos
        secondPos = midPos
        thirdPos = leftPos
    elif trialType == 'RLM':
        firstPos = rightPos
        secondPos = leftPos
        thirdPos = midPos
    elif trialType == 'MRL':
        firstPos = midPos
        secondPos = rightPos
        secondPos = rightPos
        thirdPos = leftPos
    
    EncodingTrials.addData("triplet1", triplet1)
    EncodingTrials.addData("triplet2", triplet2)
    EncodingTrials.addData("triplet3", triplet3)
    EncodingTrials.addData("nextTrial", nextTrial)
    EncodingTrials.addData("Trial_Order", trialType)
    img1.setPos(firstPos)
    img1.setImage(triplet1)
    img2.setPos(secondPos)
    img2.setImage(triplet2)
    img3.setPos(thirdPos)
    img3.setImage(triplet3)
    sound_pop4.setSound('POP.wav', hamming=True)
    sound_pop4.setVolume(1.0, log=False)
    sound_pop5.setSound('POP.wav', hamming=True)
    sound_pop5.setVolume(1.0, log=False)
    sound_pop6.setSound('POP.wav', hamming=True)
    sound_pop6.setVolume(1.0, log=False)
    # keep track of which components have finished
    second_viewComponents = [img1, img2, img3, sound_pop4, sound_pop5, sound_pop6]
    for thisComponent in second_viewComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    second_viewClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "second_view"-------
    while continueRoutine:
        # get current time
        t = second_viewClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=second_viewClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *img1* updates
        if img1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            img1.frameNStart = frameN  # exact frame index
            img1.tStart = t  # local t and not account for scr refresh
            img1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(img1, 'tStartRefresh')  # time at next scr refresh
            img1.setAutoDraw(True)
        if img1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            el_tracker.sendMessage('Triplet1.running %s' % second_viewClock.getTime())
            if tThisFlipGlobal > img1.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                img1.tStop = t  # not accounting for scr refresh
                img1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(img1, 'tStopRefresh')  # time at next scr refresh
                img1.setAutoDraw(False)
        
        # *img2* updates
        if img2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            img2.frameNStart = frameN  # exact frame index
            img2.tStart = t  # local t and not account for scr refresh
            img2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(img2, 'tStartRefresh')  # time at next scr refresh
            img2.setAutoDraw(True)
        if img2.status == STARTED:
            el_tracker.sendMessage('Triplet2.running %s' % second_viewClock.getTime())
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > img2.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                img2.tStop = t  # not accounting for scr refresh
                img2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(img2, 'tStopRefresh')  # time at next scr refresh
                img2.setAutoDraw(False)
        
        # *img3* updates
        if img3.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            img3.frameNStart = frameN  # exact frame index
            img3.tStart = t  # local t and not account for scr refresh
            img3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(img3, 'tStartRefresh')  # time at next scr refresh
            img3.setAutoDraw(True)
        if img3.status == STARTED:
            el_tracker.sendMessage('Triplet3.running %s' % second_viewClock.getTime())
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > img3.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                img3.tStop = t  # not accounting for scr refresh
                img3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(img3, 'tStopRefresh')  # time at next scr refresh
                img3.setAutoDraw(False)
        # start/stop sound_pop4
        if sound_pop4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_pop4.frameNStart = frameN  # exact frame index
            sound_pop4.tStart = t  # local t and not account for scr refresh
            sound_pop4.tStartRefresh = tThisFlipGlobal  # on global time
            sound_pop4.play(when=win)  # sync with win flip
        # start/stop sound_pop5
        if sound_pop5.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            sound_pop5.frameNStart = frameN  # exact frame index
            sound_pop5.tStart = t  # local t and not account for scr refresh
            sound_pop5.tStartRefresh = tThisFlipGlobal  # on global time
            sound_pop5.play(when=win)  # sync with win flip
        # start/stop sound_pop6
        if sound_pop6.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            sound_pop6.frameNStart = frameN  # exact frame index
            sound_pop6.tStart = t  # local t and not account for scr refresh
            sound_pop6.tStartRefresh = tThisFlipGlobal  # on global time
            sound_pop6.play(when=win)  # sync with win flip
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.saveAsWideText(filename+'.csv', delim=',')
            thisExp.saveAsPickle(filename)
            logging.flush()
            terminate_task()
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in second_viewComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "second_view"-------
    for thisComponent in second_viewComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    eTrials = eTrials + 1
    TRIAL_INDEX = TRIAL_INDEX + 1
    el_tracker.sendMessage('!V TRIAL_VAR eTrials %d' %eTrials) 
    sound_pop4.stop()  # ensure sound has stopped at end of routine
    sound_pop5.stop()  # ensure sound has stopped at end of routine
    sound_pop6.stop()  # ensure sound has stopped at end of routine
    el_tracker.sendMessage('secondviewEnding %s' % second_viewClock.getTime())
    
    # the Routine "second_view" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "methodQText"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    methodQTextComponents = [text_2]
    for thisComponent in methodQTextComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    methodQTextClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "methodQText"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = methodQTextClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=methodQTextClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            el_tracker.sendMessage('methodText %s' % methodQTextClock.getTime())
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.saveAsWideText(filename+'.csv', delim=',')
            thisExp.saveAsPickle(filename)
            logging.flush()
            terminate_task()
            core.quit()
      
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in methodQTextComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "methodQText"-------
    for thisComponent in methodQTextComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    el_tracker.sendMessage('methodtextEnding %s' % methodQTextClock.getTime())
    
    # ------Prepare to start Routine "MethodCheck"-------
    continueRoutine = True
    # update component parameters for each repeat
    sameText.setText('Same')
    diffText.setText('Different')
    # setup some python lists for storing info about the MethodMouse
    MethodMouse.x = []
    MethodMouse.y = []
    MethodMouse.leftButton = []
    MethodMouse.midButton = []
    MethodMouse.rightButton = []
    MethodMouse.time = []
    MethodMouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    MethodCheckComponents = [text, sameText, diffText, leftCL, rightCL, MethodMouse]
    for thisComponent in MethodCheckComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    MethodCheckClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "MethodCheck"-------
    while continueRoutine:
        # get current time
        t = MethodCheckClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=MethodCheckClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *sameText* updates
        if sameText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sameText.frameNStart = frameN  # exact frame index
            sameText.tStart = t  # local t and not account for scr refresh
            sameText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sameText, 'tStartRefresh')  # time at next scr refresh
            sameText.setAutoDraw(True)
        
        # *diffText* updates
        if diffText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            diffText.frameNStart = frameN  # exact frame index
            diffText.tStart = t  # local t and not account for scr refresh
            diffText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(diffText, 'tStartRefresh')  # time at next scr refresh
            diffText.setAutoDraw(True)
        
        # *leftCL* updates
        if leftCL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            leftCL.frameNStart = frameN  # exact frame index
            leftCL.tStart = t  # local t and not account for scr refresh
            leftCL.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(leftCL, 'tStartRefresh')  # time at next scr refresh
            leftCL.setAutoDraw(True)
        
        # *rightCL* updates
        if rightCL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rightCL.frameNStart = frameN  # exact frame index
            rightCL.tStart = t  # local t and not account for scr refresh
            rightCL.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rightCL, 'tStartRefresh')  # time at next scr refresh
            rightCL.setAutoDraw(True)
        # *MethodMouse* updates
        if MethodMouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            MethodMouse.frameNStart = frameN  # exact frame index
            MethodMouse.tStart = t  # local t and not account for scr refresh
            MethodMouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MethodMouse, 'tStartRefresh')  # time at next scr refresh
            MethodMouse.status = STARTED
            MethodMouse.mouseClock.reset()
            prevButtonState = MethodMouse.getPressed()  # if button is down already this ISN'T a new click
        if MethodMouse.status == STARTED:  # only update if started and not finished!
            el_tracker.sendMessage('methodCheck %s' %MethodCheckClock.getTime())
            buttons = MethodMouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [rightCL, leftCL]:
                        if obj.contains(MethodMouse):
                            gotValidClick = True
                            MethodMouse.clicked_name.append(obj.name)
                    x, y = MethodMouse.getPos()
                    MethodMouse.x.append(x)
                    MethodMouse.y.append(y)
                    buttons = MethodMouse.getPressed()
                    MethodMouse.leftButton.append(buttons[0])
                    MethodMouse.midButton.append(buttons[1])
                    MethodMouse.rightButton.append(buttons[2])
                    MethodMouse.time.append(MethodMouse.mouseClock.getTime())
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.saveAsWideText(filename+'.csv', delim=',')
            thisExp.saveAsPickle(filename)
            logging.flush()
            terminate_task()
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in MethodCheckComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "MethodCheck"-------
    for thisComponent in MethodCheckComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if MethodMouse.clicked_name == methodAns:
        EncodingTrials.addData ("methodCheck", '1')
        methodCheck = 1
    else:
        EncodingTrials.addData ("methodCheck", '0')
        methodCheck = 0

    
    #store whether or not they answered correctly for the "same" or "different" trial type.
    thisExp.addData("Method Clicked", MethodMouse.clicked_name);
    el_tracker.sendMessage('methodEnding %s' % MethodCheckClock.getTime())

    # store data for EncodingTrials (TrialHandler)
    if len(MethodMouse.leftButton): EncodingTrials.addData('MethodMouse.leftButton', MethodMouse.leftButton[0])
    if len(MethodMouse.midButton): EncodingTrials.addData('MethodMouse.midButton', MethodMouse.midButton[0])
    if len(MethodMouse.rightButton): EncodingTrials.addData('MethodMouse.rightButton', MethodMouse.rightButton[0])
    if len(MethodMouse.time): EncodingTrials.addData('MethodMouse.time', MethodMouse.time[0])
    if len(MethodMouse.clicked_name): EncodingTrials.addData('MethodMouse.clicked_name', MethodMouse.clicked_name[0])
    el_tracker.sendMessage('!V TRIAL_VAR methodCheck %s' %methodCheck)
    el_tracker.sendMessage('!V TRIAL_VAR methodClicked %s' %MethodMouse.clicked_name)

    # the Routine "MethodCheck" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "clicked_sound"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    clickedSound.setSound('click.wav', secs=0.5, hamming=True)
    clickedSound.setVolume(1.0, log=False)
    # keep track of which components have finished
    clicked_soundComponents = [clickedSound]
    for thisComponent in clicked_soundComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    clicked_soundClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "clicked_sound"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = clicked_soundClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=clicked_soundClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop clickedSound
        if clickedSound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            clickedSound.frameNStart = frameN  # exact frame index
            clickedSound.tStart = t  # local t and not account for scr refresh
            clickedSound.tStartRefresh = tThisFlipGlobal  # on global time
            clickedSound.play(when=win)  # sync with win flip
        if clickedSound.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > clickedSound.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                clickedSound.tStop = t  # not accounting for scr refresh
                clickedSound.frameNStop = frameN  # exact frame index
                win.timeOnFlip(clickedSound, 'tStopRefresh')  # time at next scr refresh
                clickedSound.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.saveAsWideText(filename+'.csv', delim=',')
            thisExp.saveAsPickle(filename)
            logging.flush()
            terminate_task()
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in clicked_soundComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "clicked_sound"-------
    for thisComponent in clicked_soundComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    clickedSound.stop()  # ensure sound has stopped at end of routine
    thisExp.nextEntry()
#store eye-tracking related data in edf
# record trial variables to the EDF data file, for details, see Data
# Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
el_tracker.sendMessage('!V TRIAL_VAR trialIndex %d' % trial_index)
EncodingTrials.addData("TRIAL_INDEX", str(TRIAL_INDEX))
el_tracker.sendMessage('!V TRIAL_VAR trialCategory %s' % trial_category)
EncodingTrials.addData("trialCategory", str(trial_category))
el_tracker.sendMessage('!V TRIAL_VAR eTrials %d' %eTrials)
EncodingTrials.addData("encodingTrials", str(eTrials))
el_tracker.sendMessage('!V TRIAL_VAR methodCheck %s' %methodCheck)
EncodingTrials.addData("methodCheck", str(methodCheck))
el_tracker.sendMessage('!V TRIAL_VAR methodClicked %s' %MethodMouse.clicked_name)
el_tracker.sendMessage('!V TRIAL_VAR encodingType %s' %encodingType)
el_tracker.sendMessage('!V TRIAL_VAR triplet1 %s' %triplet1)
el_tracker.sendMessage('!V TRIAL_VAR triplet2 %s' %triplet2)
el_tracker.sendMessage('!V TRIAL_VAR triplet3 %s' %triplet3)
el_tracker.sendMessage('!V TRIAL_VAR nextTrial %s' %nextTrial)
    
    # send a 'TRIAL_RESULT' message to mark the end of trial, see Data
    # Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
el_tracker.sendMessage('TRIAL_RESULT %d' % pylink.TRIAL_OK)
    
# completed numEncoding repeats of 'EncodingTrials'
# ------Prepare to start Routine "break_2"-------
continueRoutine = True
# update component parameters for each repeat
start2.keys = []
start2.rt = []
_start2_allKeys = []
# keep track of which components have finished
break_2Components = [BlockBreak, text_4, start2]
for thisComponent in break_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
break_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "break_2"-------
while continueRoutine:
    # get current time
    t = break_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=break_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    theseKeys = start2.getKeys(keyList=['space','q'], waitRelease=False)
    _start2_allKeys.extend(theseKeys)
    if len(_start2_allKeys):
        start2.keys = _start2_allKeys[-1].name  # just the last key pressed
        start2.rt = _start2_allKeys[-1].rt
        # a response ends the routine
        continueRoutine = False
    
    # *BlockBreak* updates
    if BlockBreak.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        BlockBreak.frameNStart = frameN  # exact frame index
        BlockBreak.tStart = t  # local t and not account for scr refresh
        BlockBreak.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BlockBreak, 'tStartRefresh')  # time at next scr refresh
        BlockBreak.setAutoDraw(True)
    if BlockBreak.status == STARTED:
        el_tracker.sendMessage('blockBreak %s' % break_2Clock.getTime())
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > BlockBreak.tStartRefresh + 180-frameTolerance:
            # keep track of stop time/frame for later
            BlockBreak.tStop = t  # not accounting for scr refresh
            BlockBreak.frameNStop = frameN  # exact frame index
            win.timeOnFlip(BlockBreak, 'tStopRefresh')  # time at next scr refresh
            BlockBreak.setAutoDraw(False)
            theseKeys = start2.getKeys(keyList=['space','q'], waitRelease=False)
            _start2_allKeys.extend(theseKeys)
            if len(_start2_allKeys):
                start2.keys = _start2_allKeys[-1].name  # just the last key pressed
                start2.rt = _start2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 180.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # *start2* updates
    waitOnFlip = False
    if start2.status == NOT_STARTED and tThisFlip >= 180.0-frameTolerance:
        # keep track of start time/frame for later
        start2.frameNStart = frameN  # exact frame index
        start2.tStart = t  # local t and not account for scr refresh
        start2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start2, 'tStartRefresh')  # time at next scr refresh
        start2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(start2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(start2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if start2.status == STARTED and not waitOnFlip:
        theseKeys = start2.getKeys(keyList=['space','q'], waitRelease=False)
        _start2_allKeys.extend(theseKeys)
        if len(_start2_allKeys):
            start2.keys = _start2_allKeys[-1].name  # just the last key pressed
            start2.rt = _start2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        thisExp.saveAsWideText(filename+'.csv', delim=',')
        thisExp.saveAsPickle(filename)
        logging.flush()
        terminate_task()
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in break_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "break_2"-------
for thisComponent in break_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('BlockBreak.started', BlockBreak.tStartRefresh)
thisExp.addData('BlockBreak.stopped', BlockBreak.tStopRefresh)
# check responses
if start2.keys in ['', [], None]:  # No response was made
    start2.keys = None
#thisExp.addData('start2.keys',start2.keys)
if start2.keys != None:  # we had a response
    el_tracker.sendMessage('breakEnding %s' % break_2Clock.getTime())
thisExp.nextEntry()
# the Routine "break_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#Recalibrate after the break
# skip this step if running the script in Dummy Mode
if not dummy_mode:
    try:
        el_tracker.doTrackerSetup()
    except RuntimeError as err:
        print('ERROR:', err)
        el_tracker.exitCalibration()

    
#First retrieval block:
# ------Prepare to start Routine "initRecallPics"-------
continueRoutine = True
# update component parameters for each repeat
retTrials = 0
retNew = 0
retSame = 0
random.shuffle(samePics)
#same pics are all pictures that came from 'same' trials, one picture per trial
#shuffle and put in retrieval list.
#retrievalNew = []
retrievalSame = []

retrievalSame.append(samePics)
# keep track of which components have finished
initRecallPicsComponents = []
for thisComponent in initRecallPicsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
initRecallPicsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "initRecallPics"-------
while continueRoutine:
    # get current time
    t = initRecallPicsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=initRecallPicsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        thisExp.saveAsWideText(filename+'.csv', delim=',')
        thisExp.saveAsPickle(filename)
        logging.flush()
        terminate_task()
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in initRecallPicsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "initRecallPics"-------
for thisComponent in initRecallPicsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "initRecallPics" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
RetrievalTrials = data.TrialHandler(nReps=numRetrieval1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='RetrievalTrials')
thisExp.addLoop(RetrievalTrials)  # add the loop to the experiment
thisRetrievalTrial = RetrievalTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRetrievalTrial.rgb)
if thisRetrievalTrial != None:
    for paramName in thisRetrievalTrial:
        exec('{} = thisRetrievalTrial[paramName]'.format(paramName))

for thisRetrievalTrial in RetrievalTrials:
    trial_category = 'retrieval'
    currentLoop = RetrievalTrials
    # abbreviate parameter names if possible (e.g. rgb = thisRetrievalTrial.rgb)
    if thisRetrievalTrial != None:
        for paramName in thisRetrievalTrial:
            exec('{} = thisRetrievalTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "RetrievalImage"-------
    continueRoutine = True
    rtrial_index = RetrievalTrials.thisRepN
    trial_category= 'retrieval'
    #start recording eye-movements
    start_eye_tracker(rtrial_index, trial_category)
    
    # send a "TRIALID" message to mark the start of a trial, see Data
    # Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
    el_tracker.sendMessage('!V TRIAL_VAR trialCategory %s' %trial_category)
    el_tracker.sendMessage('!V TRIAL_VAR retTrials %d' %rtrial_index) #HERE
    
    # update component parameters for each repeat
    retrievalImage = None
    
    if retProb < 1.1:
        retType = "old"
        RetrievalTrials.addData("retType", "old")
        length = len(samePics)
        if(length == 0):
            sys.exit(1)
        retrievalImage = 'images/' + samePics[retSame] + '.png'
        retSame = retSame + 1
    #so I am telling it that it needs to take an image from same pics
    #and iterate through those pictures with more retrieval trials
    #no 'new' retrieval at this point.
    else:
        retType = "new"
        RetrievalTrials.addData("retType", "new")
        length = len(newPics)
        if(length == 0):
            sys.exit(1)
        retrievalImage = 'images/' + newPics[retNew] + '.png'
        retNew = retNew + 1
        
    retIMG.setImage(retrievalImage)
    sound_pop7.setSound('POP.wav', hamming=True)
    sound_pop7.setVolume(1.0, log=False)
    # keep track of which components have finished
    RetrievalImageComponents = [retIMG, sound_pop7]
    for thisComponent in RetrievalImageComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RetrievalImageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "RetrievalImage"-------
    while continueRoutine:
        # get current time
        t = RetrievalImageClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RetrievalImageClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *retIMG* updates
        if retIMG.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            retIMG.frameNStart = frameN  # exact frame index
            retIMG.tStart = t  # local t and not account for scr refresh
            retIMG.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(retIMG, 'tStartRefresh')  # time at next scr refresh
            retIMG.setAutoDraw(True)
        if retIMG.status == STARTED:
            el_tracker.sendMessage('retImg %s' % RetrievalImageClock.getTime())
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > retIMG.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                retIMG.tStop = t  # not accounting for scr refresh
                retIMG.frameNStop = frameN  # exact frame index
                win.timeOnFlip(retIMG, 'tStopRefresh')  # time at next scr refresh
                retIMG.setAutoDraw(False)
        # start/stop sound_pop7
        if sound_pop7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_pop7.frameNStart = frameN  # exact frame index
            sound_pop7.tStart = t  # local t and not account for scr refresh
            sound_pop7.tStartRefresh = tThisFlipGlobal  # on global time
            sound_pop7.play(when=win)  # sync with win flip
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):        
            thisExp.saveAsWideText(filename+'.csv', delim=',')
            thisExp.saveAsPickle(filename)
            logging.flush()
            terminate_task()
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RetrievalImageComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "RetrievalImage"-------
    for thisComponent in RetrievalImageComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    el_tracker.sendMessage('retimgEnding %s' % RetrievalImageClock.getTime())
    sound_pop7.stop()  # ensure sound has stopped at end of routine
    el_tracker.sendMessage('!V TRIAL_VAR retIMG %s' %retrievalImage)
 #   RetrievalTrials.addData('retIMG', str(retIMG))
    RetrievalTrials.addData('retIMG', str(retrievalImage))
    # the Routine "RetrievalImage" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Q2Text"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    Q2TextComponents = [question_text]
    for thisComponent in Q2TextComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Q2TextClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Q2Text"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Q2TextClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Q2TextClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *question_text* updates
        if question_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            question_text.frameNStart = frameN  # exact frame index
            question_text.tStart = t  # local t and not account for scr refresh
            question_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question_text, 'tStartRefresh')  # time at next scr refresh
            question_text.setAutoDraw(True)
        if question_text.status == STARTED:
            el_tracker.sendMessage('methodText %s' % Q2TextClock.getTime())
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > question_text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                question_text.tStop = t  # not accounting for scr refresh
                question_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(question_text, 'tStopRefresh')  # time at next scr refresh
                question_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.saveAsWideText(filename+'.csv', delim=',')
            thisExp.saveAsPickle(filename)
            logging.flush()
            terminate_task()
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Q2TextComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Q2Text"-------
    for thisComponent in Q2TextComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    el_tracker.sendMessage('textEnding %s' % Q2TextClock.getTime())
    
    # ------Prepare to start Routine "Decision"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the Order_Position_Response
    Order_Position_Response.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    DecisionComponents = [decisionQ_2, first_left, second_middle, third_right, First, Second, Third, Order_Position_Response]
    for thisComponent in DecisionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    DecisionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Decision"-------
    while continueRoutine:
        # get current time
        t = DecisionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=DecisionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *decisionQ_2* updates
        if decisionQ_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            decisionQ_2.frameNStart = frameN  # exact frame index
            decisionQ_2.tStart = t  # local t and not account for scr refresh
            decisionQ_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(decisionQ_2, 'tStartRefresh')  # time at next scr refresh
            decisionQ_2.setAutoDraw(True)
        
        # *first_left* updates
        if first_left.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            first_left.frameNStart = frameN  # exact frame index
            first_left.tStart = t  # local t and not account for scr refresh
            first_left.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(first_left, 'tStartRefresh')  # time at next scr refresh
            first_left.setAutoDraw(True)
        
        # *second_middle* updates
        if second_middle.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            second_middle.frameNStart = frameN  # exact frame index
            second_middle.tStart = t  # local t and not account for scr refresh
            second_middle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(second_middle, 'tStartRefresh')  # time at next scr refresh
            second_middle.setAutoDraw(True)
        
        # *third_right* updates
        if third_right.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            third_right.frameNStart = frameN  # exact frame index
            third_right.tStart = t  # local t and not account for scr refresh
            third_right.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(third_right, 'tStartRefresh')  # time at next scr refresh
            third_right.setAutoDraw(True)
        
        # *First* updates
        if First.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            First.frameNStart = frameN  # exact frame index
            First.tStart = t  # local t and not account for scr refresh
            First.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(First, 'tStartRefresh')  # time at next scr refresh
            First.setAutoDraw(True)
        
        # *Second* updates
        if Second.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Second.frameNStart = frameN  # exact frame index
            Second.tStart = t  # local t and not account for scr refresh
            Second.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Second, 'tStartRefresh')  # time at next scr refresh
            Second.setAutoDraw(True)
        
        # *Third* updates
        if Third.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Third.frameNStart = frameN  # exact frame index
            Third.tStart = t  # local t and not account for scr refresh
            Third.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Third, 'tStartRefresh')  # time at next scr refresh
            Third.setAutoDraw(True)
        # *Order_Position_Response* updates
        if Order_Position_Response.status == NOT_STARTED and t >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Order_Position_Response.frameNStart = frameN  # exact frame index
            Order_Position_Response.tStart = t  # local t and not account for scr refresh
            Order_Position_Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Order_Position_Response, 'tStartRefresh')  # time at next scr refresh
            Order_Position_Response.status = STARTED
            Order_Position_Response.mouseClock.reset()
            prevButtonState = Order_Position_Response.getPressed()  # if button is down already this ISN'T a new click
        if Order_Position_Response.status == STARTED:  # only update if started and not finished!
            el_tracker.sendMessage('Decision %s' %DecisionClock.getTime())
            buttons = Order_Position_Response.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [first_left,second_middle,third_right]:
                        if obj.contains(Order_Position_Response):
                            gotValidClick = True
                            Order_Position_Response.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.saveAsWideText(filename+'.csv', delim=',')
            thisExp.saveAsPickle(filename)
            logging.flush()
            terminate_task()
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in DecisionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    el_tracker.sendMessage ('!V TRIAL_VAR orderResponse %s' %Order_Position_Response.clicked_name[0])
    # -------Ending Routine "Decision"-------
    for thisComponent in DecisionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    retTrials = retTrials + 1
    TRIAL_INDEX = TRIAL_INDEX + 1
    el_tracker.sendMessage('!V TRIAL_VAR retTrials %d' %retTrials)
    RetrievalTrials.addData("retTrials", str(retTrials))
    RetrievalTrials.addData("TRIAL_INDEX", str(TRIAL_INDEX))
    thisExp.addData("TRIAL_INDEX", str(TRIAL_INDEX))
    el_tracker.sendMessage('decisionClock %s' % DecisionClock)
    # store data for RetrievalTrials (TrialHandler)
    x, y = Order_Position_Response.getPos()
    buttons = Order_Position_Response.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        for obj in [first_left,second_middle,third_right]:
            if obj.contains(Order_Position_Response):
                gotValidClick = True
                Order_Position_Response.clicked_name.append(obj.name)
    RetrievalTrials.addData('Order_Position_Response.leftButton', buttons[0])
    RetrievalTrials.addData('Order_Position_Response.midButton', buttons[1])
    RetrievalTrials.addData('Order_Position_Response.rightButton', buttons[2])
    if len(Order_Position_Response.clicked_name):
        RetrievalTrials.addData('Order_Position_Response.clicked_name', Order_Position_Response.clicked_name[0])
    
    # the Routine "Decision" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "clicked_sound"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    clickedSound.setSound('click.wav', secs=0.5, hamming=True)
    clickedSound.setVolume(1.0, log=False)
    # keep track of which components have finished
    clicked_soundComponents = [clickedSound]
    for thisComponent in clicked_soundComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    clicked_soundClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "clicked_sound"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = clicked_soundClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=clicked_soundClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop clickedSound
        if clickedSound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            clickedSound.frameNStart = frameN  # exact frame index
            clickedSound.tStart = t  # local t and not account for scr refresh
            clickedSound.tStartRefresh = tThisFlipGlobal  # on global time
            clickedSound.play(when=win)  # sync with win flip
        if clickedSound.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > clickedSound.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                clickedSound.tStop = t  # not accounting for scr refresh
                clickedSound.frameNStop = frameN  # exact frame index
                win.timeOnFlip(clickedSound, 'tStopRefresh')  # time at next scr refresh
                clickedSound.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.saveAsWideText(filename+'.csv', delim=',')
            thisExp.saveAsPickle(filename)
            logging.flush()
            terminate_task()
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in clicked_soundComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "clicked_sound"-------
    for thisComponent in clicked_soundComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    clickedSound.stop()  # ensure sound has stopped at end of routine
    thisExp.nextEntry()
    
#store eye-tracking related data in edf
# record trial variables to the EDF data file, for details, see Data
# Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
el_tracker.sendMessage('!V TRIAL_VAR retIMG %s' %retrievalImage)
RetrievalTrials.addData("retrievalTrials", str(retTrials))
RetrievalTrials.addData("TRIAL_INDEX", str(TRIAL_INDEX))
RetrievalTrials.addData("retIMG", str(retrievalImage))
el_tracker.sendMessage('!V TRIAL_VAR retTrials %d' %retTrials)
el_tracker.sendMessage ('!V TRIAL_VAR orderResponse %s' %Order_Position_Response.clicked_name[0])
    
# send a 'TRIAL_RESULT' message to mark the end of trial, see Data
# Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
el_tracker.sendMessage('TRIAL_RESULT %d' % pylink.TRIAL_OK)
    
# completed numRetrieval repeats of 'RetrievalTrials'

#Second encoding block initialization
#Initialization routine2
# ------Prepare to start Routine "init2"-------
continueRoutine = True
#Starting Encoding Block 2 after the break!
#resetting same and different trial type lists. 
sameDiff2 = ["same","same","same","same","same","same","same","same","same","same","same","same","same","same","same","same","same","same","same","same","diff","diff","diff","diff","diff"];
shuffle(sameDiff2)

#So for the same trials:
# Define the strings
fixed_strings = ['LMR', 'RML']  # These will occur 7 times each
other_strings = ['MLR', 'MRL', 'LRM', 'RLM']  # These will be randomly selected to have total of 7 also

# Select 7 strings from other_strings with repetitions
selected_strings = random.choices(other_strings, k=9)

# Create a list to store the strings
sameTrials2 = fixed_strings * 9  # Repeating fixed_strings 9 times
sameTrials2 += selected_strings  # Adding the selected 9 strings

# Shuffle the list
random.shuffle(sameTrials2)

# Print the randomized list
print("Randomized string list:")
print(sameTrials) #now this should be a list of 27 that we will run 20 of, but because it is indexed by eTrials, there needs to be more than 25 items. 

#for the different trials:
diffTrials2 = fixed_strings * 9  # Repeating fixed_strings 9 times
diffTrials2 += selected_strings  # Adding the selected 9 strings

# Shuffle the list
random.shuffle(diffTrials2)

# Print the selected strings)
print(diffTrials2) #because these are indexed by eTrials while they select the images, they need to be more than 25 items

#hard-coded names of all images and trial types (counterbalanced).
numItems = 210
#numTotencoding = 50
numEncodingBlock1 = 3
numEncodingBlock2 = 3
numTotretrieval = 4
numRetrieval1 = 2
numRetrieval2 = 2
eTrials2 = 0

# keep track of which components have finished
initCodeComponents = []
for thisComponent in initCodeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
initCodeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "initCode"-------
while continueRoutine:
    # get current time
    t = initCodeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=initCodeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        thisExp.saveAsWideText(filename+'.csv', delim=',')
        thisExp.saveAsPickle(filename)
        logging.flush()
        terminate_task()
        core.quit()

    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in initCodeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "initCode"-------
for thisComponent in initCodeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "initCode" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial"-------
continueRoutine = True
# update component parameters for each repeat
start.keys = []
start.rt = []
_start_allKeys = []
# keep track of which components have finished
trialComponents = [Instructions, start]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial"-------
while continueRoutine:
    # get current time
    t = trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instructions* updates
    if Instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructions.frameNStart = frameN  # exact frame index
        Instructions.tStart = t  # local t and not account for scr refresh
        Instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructions, 'tStartRefresh')  # time at next scr refresh
        Instructions.setAutoDraw(True)
    
    # *start* updates
    waitOnFlip = False
    if start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start.frameNStart = frameN  # exact frame index
        start.tStart = t  # local t and not account for scr refresh
        start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start, 'tStartRefresh')  # time at next scr refresh
        start.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(start.clock.reset)  # t=0 on next screen flip
    if start.status == STARTED and not waitOnFlip:
        theseKeys = start.getKeys(keyList=['space', 'q'], waitRelease=False)
        _start_allKeys.extend(theseKeys)
        if len(_start_allKeys):
            start.keys = _start_allKeys[-1].name  # just the last key pressed
            start.rt = _start_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        thisExp.saveAsWideText(filename+'.csv', delim=',')
        thisExp.saveAsPickle(filename)
        logging.flush()
        terminate_task()
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
EncodingBlock2 = data.TrialHandler(nReps=numEncodingBlock2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='EncodingBlock2')
thisExp.addLoop(EncodingBlock2)  # add the loop to the experiment
thisEncodingBlock2 = EncodingBlock2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEncodingBlock2.rgb)
if thisEncodingBlock2 != None:
    for paramName in thisEncodingBlock2:
        exec('{} = thisEncodingBlock2[paramName]'.format(paramName))

for thisEncodingBlock2 in EncodingBlock2:
    trial_category = 'encoding'
    currentLoop = EncodingBlock2
    # abbreviate parameter names if possible (e.g. rgb = thisEncodingBlock2.rgb)
    if thisEncodingBlock2 != None:
        for paramName in thisEncodingBlock2:
            exec('{} = thisEncodingBlock2[paramName]'.format(paramName))

#Second encoding block starts
    # ------Prepare to start Routine "fix"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    
    trial_index = EncodingBlock2.thisRepN
    #start recording eye-movements
    start_eye_tracker(trial_index, trial_category)

    # send a "TRIALID" message to mark the start of a trial, see Data
    # Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
    el_tracker.sendMessage('trialIndex %d' % trial_index) #HERE
    
    # update component parameters for each repeat
    # keep track of which components have finished
    fixComponents = [fix]
    for thisComponent in fixComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fix"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        el_tracker.sendMessage('fix %s' % fix)
        # *fix* updates
        if fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix.frameNStart = frameN  # exact frame index
            fix.tStart = t  # local t and not account for scr refresh
            fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
            fix.setAutoDraw(True)
        if fix.status == STARTED:
            el_tracker.sendMessage('fixation %s' % fixClock.getTime())
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                fix.tStop = t  # not accounting for scr refresh
                fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix, 'tStopRefresh')  # time at next scr refresh
                fix.setAutoDraw(False)
                el_tracker.sendMessage('fixation %s' % fixClock.getTime())
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.saveAsWideText(filename+'.csv', delim=',')
            thisExp.saveAsPickle(filename)
            logging.flush()
            terminate_task()
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fix"-------
    for thisComponent in fixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    el_tracker.sendMessage('fixationEnd %s' % fixClock.getTime())
    
    
    # ------Prepare to start Routine "first_view"-------
    continueRoutine = True
    # update component parameters for each repeat
    import os
    #iterate through trial type and set a new one for each trial
    method_Trial = sameDiff2[eTrials2]
    if method_Trial == "same":
        trialType = sameTrials2[eTrials2]
    else:
            trialType = diffTrials2[eTrials2]
    el_tracker.sendMessage('!V TRIAL_VAR trialType %s' %trialType)
    el_tracker.sendMessage('!V TRIAL_VAR trialcategory %s' %trial_category)
    el_tracker.sendMessage('!V TRIAL_VAR trialIndex %d' %trial_index)
    
    #positions
    leftPos = -0.5, 0.0
    midPos = 0.0, 0.0
    rightPos = 0.5, 0.0
    
    if trialType == 'LMR':
        firstPos = leftPos
        secondPos = midPos
        thirdPos = rightPos
    elif trialType == 'LRM':
        firstPos = leftPos
        secondPos = rightPos
        thirdPos = midPos
    elif trialType == 'MLR':
        firstPos = midPos
        secondPos = leftPos
        thirdPos = rightPos
    elif trialType == 'RML':
        firstPos = rightPos
        secondPos = midPos
        thirdPos = leftPos
    elif trialType == 'RLM':
        firstPos = rightPos
        secondPos = leftPos
        thirdPos = midPos
    elif trialType == 'MRL':
        firstPos = midPos
        secondPos = rightPos
        thirdPos = leftPos
    
    #set images in triplets
    triplet1 = 'images/'+encodingPics2[eTrials2][0]+'.png'
    triplet2 = 'images/'+encodingPics2[eTrials2][1]+'.png'
    triplet3 = 'images/'+encodingPics2[eTrials2][2]+'.png'
    
    EncodingBlock2.addData ("Trial_Order", trialType)
 #   thisExp.addData("TrialOrder", trialType)
    thisExp.addData("triplet1", triplet1)
    thisExp.addData("triplet2", triplet2)
    thisExp.addData("triplet3", triplet3)
    Triplet1.setPos(firstPos)
    Triplet1.setImage(triplet1)
    Triplet2.setPos(secondPos)
    Triplet2.setImage(triplet2)
    Triplet3.setPos(thirdPos)
    Triplet3.setImage(triplet3)
    sound_pop.setSound('POP.wav', hamming=True)
    sound_pop.setVolume(1.0, log=False)
    sound_pop2.setSound('POP.wav', hamming=True)
    sound_pop2.setVolume(1.0, log=False)
    sound_pop3.setSound('POP.wav', hamming=True)
    sound_pop3.setVolume(1.0, log=False)
    # keep track of which components have finished
    first_viewComponents = [Triplet1, Triplet2, Triplet3, sound_pop, sound_pop2, sound_pop3]
    for thisComponent in first_viewComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    first_viewClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "first_view"-------
    while continueRoutine:
        # get current time
        t = first_viewClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=first_viewClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Triplet1* updates
        if Triplet1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Triplet1.frameNStart = frameN  # exact frame index
            Triplet1.tStart = t  # local t and not account for scr refresh
            Triplet1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Triplet1, 'tStartRefresh')  # time at next scr refresh
            Triplet1.setAutoDraw(True)
        if Triplet1.status == STARTED:
            el_tracker.sendMessage('Triplet1.running %s' % first_viewClock.getTime())
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Triplet1.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                Triplet1.tStop = t  # not accounting for scr refresh
                Triplet1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Triplet1, 'tStopRefresh')  # time at next scr refresh
                Triplet1.setAutoDraw(False)
        
        # *Triplet2* updates
        if Triplet2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            Triplet2.frameNStart = frameN  # exact frame index
            Triplet2.tStart = t  # local t and not account for scr refresh
            Triplet2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Triplet2, 'tStartRefresh')  # time at next scr refresh
            Triplet2.setAutoDraw(True)
        if Triplet2.status == STARTED:
            el_tracker.sendMessage('Triplet2.running %s' % first_viewClock.getTime())
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Triplet2.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                Triplet2.tStop = t  # not accounting for scr refresh
                Triplet2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Triplet2, 'tStopRefresh')  # time at next scr refresh
                Triplet2.setAutoDraw(False)
        
        # *Triplet3* updates
        if Triplet3.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            Triplet3.frameNStart = frameN  # exact frame index
            Triplet3.tStart = t  # local t and not account for scr refresh
            Triplet3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Triplet3, 'tStartRefresh')  # time at next scr refresh
            Triplet3.setAutoDraw(True)
        if Triplet3.status == STARTED:
            el_tracker.sendMessage('Triplet3.running %s' % first_viewClock.getTime())
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Triplet3.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                Triplet3.tStop = t  # not accounting for scr refresh
                Triplet3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Triplet3, 'tStopRefresh')  # time at next scr refresh
                Triplet3.setAutoDraw(False)
        # start/stop sound_pop
        if sound_pop.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            sound_pop.frameNStart = frameN  # exact frame index
            sound_pop.tStart = t  # local t and not account for scr refresh
            sound_pop.tStartRefresh = tThisFlipGlobal  # on global time
            sound_pop.play(when=win)  # sync with win flip
        # start/stop sound_pop2
        if sound_pop2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            sound_pop2.frameNStart = frameN  # exact frame index
            sound_pop2.tStart = t  # local t and not account for scr refresh
            sound_pop2.tStartRefresh = tThisFlipGlobal  # on global time
            sound_pop2.play(when=win)  # sync with win flip
        # start/stop sound_pop3
        if sound_pop3.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            sound_pop3.frameNStart = frameN  # exact frame index
            sound_pop3.tStart = t  # local t and not account for scr refresh
            sound_pop3.tStartRefresh = tThisFlipGlobal  # on global time
            sound_pop3.play(when=win)  # sync with win flip
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]): 
            thisExp.saveAsWideText(filename+'.csv', delim=',')
            thisExp.saveAsPickle(filename)
            logging.flush()
            terminate_task()
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in first_viewComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "first_view"-------
    for thisComponent in first_viewComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_pop.stop()  # ensure sound has stopped at end of routine
    sound_pop2.stop()  # ensure sound has stopped at end of routine
    sound_pop3.stop()  # ensure sound has stopped at end of routine
    el_tracker.sendMessage('firstviewEnding %s' % first_viewClock.getTime())
    # the Routine "first_view" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "mask"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    maskComponents = [Mask]
    for thisComponent in maskComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    maskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "mask"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = maskClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=maskClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Mask* updates
        if Mask.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Mask.frameNStart = frameN  # exact frame index
            Mask.tStart = t  # local t and not account for scr refresh
            Mask.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Mask, 'tStartRefresh')  # time at next scr refresh
            Mask.setAutoDraw(True)
        if Mask.status == STARTED:
            el_tracker.sendMessage('maskRunning %s' % maskClock.getTime())
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Mask.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                Mask.tStop = t  # not accounting for scr refresh
                Mask.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Mask, 'tStopRefresh')  # time at next scr refresh
                Mask.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.saveAsWideText(filename+'.csv', delim=',')
            thisExp.saveAsPickle(filename)
            logging.flush()
            terminate_task()
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in maskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "mask"-------
    for thisComponent in maskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    el_tracker.sendMessage('maskEnding %s' % maskClock.getTime())
    # ------Prepare to start Routine "second_view"-------
    continueRoutine = True
    # update component parameters for each repeat
    #randPos = random.random()
    #used to be same or different trials based on random number, but now making sure there are 20 same trials and 5 diff trials
    if method_Trial == "same":
        list = [0,1,2]
        random.shuffle(list)
        samePics2.append(encodingPics2[eTrials2][list[0]])
        EncodingBlock2.addData("encodingType","same")
        encodingType = 'same'
    else:
        nextTrial = random.choice(diffTrials2)
        while nextTrial == trialType:
            nextTrial = random.choice(diffTrials2)
            end
        trialType = nextTrial
        methodAns = ['rightCL'] #different
        list = [0,1,2]
        random.shuffle(list)
        triplet1 = 'images/'+encodingPics2[eTrials2][list[0]]+'.png'
        triplet2 = 'images/'+encodingPics2[eTrials2][list[1]]+'.png'
        triplet3 = 'images/'+encodingPics2[eTrials2][list[2]]+'.png'
        EncodingBlock2.addData("encodingType","diff")
        encodingType = 'diff'

    el_tracker.sendMessage('!V TRIAL_VAR encodingType %s' %encodingType)
    el_tracker.sendMessage('!V TRIAL_VAR nextTrial %s' %nextTrial)
    el_tracker.sendMessage('!V TRIAL_VAR triplet1 %s' %triplet1)
    el_tracker.sendMessage('!V TRIAL_VAR triplet2 %s' %triplet2)
    el_tracker.sendMessage('!V TRIAL_VAR triplet3 %s' %triplet3)
    #have to re-state positions and trial types
    if trialType == 'LMR':
        firstPos = leftPos
        secondPos = midPos
        thirdPos = rightPos
    elif trialType == 'LRM':
        firstPos = leftPos
        secondPos = rightPos
        thirdPos = midPos
    elif trialType == 'MLR':
        firstPos = midPos
        secondPos = leftPos
        thirdPos = rightPos
    elif trialType == 'RML':
        firstPos = rightPos
        secondPos = midPos
        thirdPos = leftPos
    elif trialType == 'RLM':
        firstPos = rightPos
        secondPos = leftPos
        thirdPos = midPos
    elif trialType == 'MRL':
        firstPos = midPos
        secondPos = rightPos
        thirdPos = leftPos
    
    EncodingBlock2.addData("triplet1", triplet1)
    EncodingBlock2.addData("triplet2", triplet2)
    EncodingBlock2.addData("triplet3", triplet3)
    EncodingBlock2.addData("nextTrial", nextTrial)
    EncodingBlock2.addData("Trial_Order", trialType)
    img1.setPos(firstPos)
    img1.setImage(triplet1)
    img2.setPos(secondPos)
    img2.setImage(triplet2)
    img3.setPos(thirdPos)
    img3.setImage(triplet3)
    sound_pop4.setSound('POP.wav', hamming=True)
    sound_pop4.setVolume(1.0, log=False)
    sound_pop5.setSound('POP.wav', hamming=True)
    sound_pop5.setVolume(1.0, log=False)
    sound_pop6.setSound('POP.wav', hamming=True)
    sound_pop6.setVolume(1.0, log=False)
    # keep track of which components have finished
    second_viewComponents = [img1, img2, img3, sound_pop4, sound_pop5, sound_pop6]
    for thisComponent in second_viewComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    second_viewClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "second_view"-------
    while continueRoutine:
        # get current time
        t = second_viewClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=second_viewClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *img1* updates
        if img1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            img1.frameNStart = frameN  # exact frame index
            img1.tStart = t  # local t and not account for scr refresh
            img1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(img1, 'tStartRefresh')  # time at next scr refresh
            img1.setAutoDraw(True)
        if img1.status == STARTED:
            el_tracker.sendMessage('Triplet1.running %s' % second_viewClock.getTime())
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > img1.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                img1.tStop = t  # not accounting for scr refresh
                img1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(img1, 'tStopRefresh')  # time at next scr refresh
                img1.setAutoDraw(False)
        
        # *img2* updates
        if img2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            img2.frameNStart = frameN  # exact frame index
            img2.tStart = t  # local t and not account for scr refresh
            img2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(img2, 'tStartRefresh')  # time at next scr refresh
            img2.setAutoDraw(True)
        if img2.status == STARTED:
            el_tracker.sendMessage('Triplet2.running %s' % second_viewClock.getTime())
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > img2.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                img2.tStop = t  # not accounting for scr refresh
                img2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(img2, 'tStopRefresh')  # time at next scr refresh
                img2.setAutoDraw(False)
        
        # *img3* updates
        if img3.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            img3.frameNStart = frameN  # exact frame index
            img3.tStart = t  # local t and not account for scr refresh
            img3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(img3, 'tStartRefresh')  # time at next scr refresh
            img3.setAutoDraw(True)
        if img3.status == STARTED:
            el_tracker.sendMessage('Triplet3.running %s' % second_viewClock.getTime())
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > img3.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                img3.tStop = t  # not accounting for scr refresh
                img3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(img3, 'tStopRefresh')  # time at next scr refresh
                img3.setAutoDraw(False)
        # start/stop sound_pop4
        if sound_pop4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_pop4.frameNStart = frameN  # exact frame index
            sound_pop4.tStart = t  # local t and not account for scr refresh
            sound_pop4.tStartRefresh = tThisFlipGlobal  # on global time
            sound_pop4.play(when=win)  # sync with win flip
        # start/stop sound_pop5
        if sound_pop5.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            sound_pop5.frameNStart = frameN  # exact frame index
            sound_pop5.tStart = t  # local t and not account for scr refresh
            sound_pop5.tStartRefresh = tThisFlipGlobal  # on global time
            sound_pop5.play(when=win)  # sync with win flip
        # start/stop sound_pop6
        if sound_pop6.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            sound_pop6.frameNStart = frameN  # exact frame index
            sound_pop6.tStart = t  # local t and not account for scr refresh
            sound_pop6.tStartRefresh = tThisFlipGlobal  # on global time
            sound_pop6.play(when=win)  # sync with win flip
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.saveAsWideText(filename+'.csv', delim=',')
            thisExp.saveAsPickle(filename)
            logging.flush()
            terminate_task()
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in second_viewComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "second_view"-------
    for thisComponent in second_viewComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    eTrials2 = eTrials2 + 1
    TRIAL_INDEX = TRIAL_INDEX + 1
    el_tracker.sendMessage('!V TRIAL_VAR eTrials %d' %eTrials2)
    print(eTrials2)
    sound_pop4.stop()  # ensure sound has stopped at end of routine
    sound_pop5.stop()  # ensure sound has stopped at end of routine)
    sound_pop6.stop()  # ensure sound has stopped at end of routine
    el_tracker.sendMessage('secondviewEnding %s' % second_viewClock.getTime())
    # the Routine "second_view" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "methodQText"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    methodQTextComponents = [text_2]
    for thisComponent in methodQTextComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    methodQTextClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "methodQText"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = methodQTextClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=methodQTextClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            el_tracker.sendMessage('methodCheck %s' %MethodCheckClock.getTime())
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.saveAsWideText(filename+'.csv', delim=',')
            thisExp.saveAsPickle(filename)
            logging.flush()
            terminate_task()
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in methodQTextComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "methodQText"-------
    for thisComponent in methodQTextComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    el_tracker.sendMessage('methodtextEnding %s' % methodQTextClock.getTime())
    
    # ------Prepare to start Routine "MethodCheck"-------
    continueRoutine = True
    # update component parameters for each repeat
    sameText.setText('Same')
    diffText.setText('Different')
    # setup some python lists for storing info about the MethodMouse
    MethodMouse.x = []
    MethodMouse.y = []
    MethodMouse.leftButton = []
    MethodMouse.midButton = []
    MethodMouse.rightButton = []
    MethodMouse.time = []
    MethodMouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    MethodCheckComponents = [text, sameText, diffText, leftCL, rightCL, MethodMouse]
    for thisComponent in MethodCheckComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    MethodCheckClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "MethodCheck"-------
    while continueRoutine:
        # get current time
        t = MethodCheckClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=MethodCheckClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *sameText* updates
        if sameText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sameText.frameNStart = frameN  # exact frame index
            sameText.tStart = t  # local t and not account for scr refresh
            sameText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sameText, 'tStartRefresh')  # time at next scr refresh
            sameText.setAutoDraw(True)
        
        # *diffText* updates
        if diffText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            diffText.frameNStart = frameN  # exact frame index
            diffText.tStart = t  # local t and not account for scr refresh
            diffText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(diffText, 'tStartRefresh')  # time at next scr refresh
            diffText.setAutoDraw(True)
        
        # *leftCL* updates
        if leftCL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            leftCL.frameNStart = frameN  # exact frame index
            leftCL.tStart = t  # local t and not account for scr refresh
            leftCL.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(leftCL, 'tStartRefresh')  # time at next scr refresh
            leftCL.setAutoDraw(True)
        
        # *rightCL* updates
        if rightCL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rightCL.frameNStart = frameN  # exact frame index
            rightCL.tStart = t  # local t and not account for scr refresh
            rightCL.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rightCL, 'tStartRefresh')  # time at next scr refresh
            rightCL.setAutoDraw(True)
        # *MethodMouse* updates
        if MethodMouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            MethodMouse.frameNStart = frameN  # exact frame index
            MethodMouse.tStart = t  # local t and not account for scr refresh
            MethodMouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MethodMouse, 'tStartRefresh')  # time at next scr refresh
            MethodMouse.status = STARTED
            MethodMouse.mouseClock.reset()
            prevButtonState = MethodMouse.getPressed()  # if button is down already this ISN'T a new click
        if MethodMouse.status == STARTED:  # only update if started and not finished!
            el_tracker.sendMessage('methodCheck %s' %MethodCheckClock.getTime())
            buttons = MethodMouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [rightCL, leftCL]:
                        if obj.contains(MethodMouse):
                            gotValidClick = True
                            MethodMouse.clicked_name.append(obj.name)
                    x, y = MethodMouse.getPos()
                    MethodMouse.x.append(x)
                    MethodMouse.y.append(y)
                    buttons = MethodMouse.getPressed()
                    MethodMouse.leftButton.append(buttons[0])
                    MethodMouse.midButton.append(buttons[1])
                    MethodMouse.rightButton.append(buttons[2])
                    MethodMouse.time.append(MethodMouse.mouseClock.getTime())
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.saveAsWideText(filename+'.csv', delim=',')
            thisExp.saveAsPickle(filename)
            logging.flush()
            terminate_task()
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in MethodCheckComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "MethodCheck"-------
    for thisComponent in MethodCheckComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if MethodMouse.clicked_name == methodAns:
        EncodingBlock2.addData ("methodCheck", '1')
        methodCheck = 1
    else:
        EncodingBlock2.addData ("methodCheck", '0')
        methodCheck = 0

    #store whether or not they answered correctly for the "same" or "different" trial type.
    thisExp.addData("Method Clicked", MethodMouse.clicked_name);
    el_tracker.sendMessage('methodCheckClock %s' % MethodCheckClock)
    # store data for EncodingBlock2 (TrialHandler)
    if len(MethodMouse.leftButton): EncodingBlock2.addData('MethodMouse.leftButton', MethodMouse.leftButton[0])
    if len(MethodMouse.midButton): EncodingBlock2.addData('MethodMouse.midButton', MethodMouse.midButton[0])
    if len(MethodMouse.rightButton): EncodingBlock2.addData('MethodMouse.rightButton', MethodMouse.rightButton[0])
    if len(MethodMouse.time): EncodingBlock2.addData('MethodMouse.time', MethodMouse.time[0])
    if len(MethodMouse.clicked_name): EncodingBlock2.addData('MethodMouse.clicked_name', MethodMouse.clicked_name[0])
    
    el_tracker.sendMessage('!V TRIAL_VAR methodCheck %s' %methodCheck)
    EncodingBlock2.addData('methodCheck',str(methodCheck))
    el_tracker.sendMessage('!V TRIAL_VAR methodClicked %s' %MethodMouse.clicked_name)
    # the Routine "MethodCheck" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "clicked_sound"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    clickedSound.setSound('click.wav', secs=0.5, hamming=True)
    clickedSound.setVolume(1.0, log=False)
    # keep track of which components have finished
    clicked_soundComponents = [clickedSound]
    for thisComponent in clicked_soundComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    clicked_soundClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "clicked_sound"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = clicked_soundClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=clicked_soundClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop clickedSound
        if clickedSound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            clickedSound.frameNStart = frameN  # exact frame index
            clickedSound.tStart = t  # local t and not account for scr refresh
            clickedSound.tStartRefresh = tThisFlipGlobal  # on global time
            clickedSound.play(when=win)  # sync with win flip
        if clickedSound.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > clickedSound.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                clickedSound.tStop = t  # not accounting for scr refresh
                clickedSound.frameNStop = frameN  # exact frame index
                win.timeOnFlip(clickedSound, 'tStopRefresh')  # time at next scr refresh
                clickedSound.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.saveAsWideText(filename+'.csv', delim=',')
            thisExp.saveAsPickle(filename)
            logging.flush()
            terminate_task()
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in clicked_soundComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "clicked_sound"-------
    for thisComponent in clicked_soundComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    clickedSound.stop()  # ensure sound has stopped at end of routine
    thisExp.nextEntry()
    
#store eye-tracking related data in edf
# record trial variables to the EDF data file, for details, see Data
# Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
el_tracker.sendMessage('!V TRIAL_VAR trialIndex %d' % trial_index)
EncodingBlock2.addData("TRIAL_INDEX", str(TRIAL_INDEX))
el_tracker.sendMessage('!V TRIAL_VAR trialCategory %s' % trial_category)
EncodingBlock2.addData("trialCategory", str(trial_category))
EncodingBlock2.addData("encodingTrials", str(eTrials2))
el_tracker.sendMessage('!V TRIAL_VAR eTrials %d' %eTrials2)   
el_tracker.sendMessage('!V TRIAL_VAR methodCheck %s' %methodCheck)
EncodingBlock2.addData("methodCheck", str(methodCheck))
el_tracker.sendMessage('!V TRIAL_VAR methodClicked %s' %MethodMouse.clicked_name)
el_tracker.sendMessage('!V TRIAL_VAR encodingType %s' %encodingType)
el_tracker.sendMessage('!V TRIAL_VAR triplet1 %s' %triplet1)
el_tracker.sendMessage('!V TRIAL_VAR triplet2 %s' %triplet2)
el_tracker.sendMessage('!V TRIAL_VAR triplet3 %s' %triplet3)
el_tracker.sendMessage('!V TRIAL_VAR nextTrial %s' %nextTrial)

# send a 'TRIAL_RESULT' message to mark the end of trial, see Data
# Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
el_tracker.sendMessage('TRIAL_RESULT %d' % pylink.TRIAL_OK)
# completed numEncoding repeats of 'EncodingBlock2'

# ------Prepare to start Routine "break_2"-------
continueRoutine = True
# update component parameters for each repeat
start2.keys = []
start2.rt = []
_start2_allKeys = []
# keep track of which components have finished
break_2Components = [BlockBreak, text_4, start2]
for thisComponent in break_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
break_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "break_2"-------
while continueRoutine:
    # get current time
    t = break_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=break_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    theseKeys = start2.getKeys(keyList=['space','q'], waitRelease=False)
    _start2_allKeys.extend(theseKeys)
    if len(_start2_allKeys):
        start2.keys = _start2_allKeys[-1].name  # just the last key pressed
        start2.rt = _start2_allKeys[-1].rt
        # a response ends the routine
        continueRoutine = False
    
    # *BlockBreak* updates
    if BlockBreak.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        BlockBreak.frameNStart = frameN  # exact frame index
        BlockBreak.tStart = t  # local t and not account for scr refresh
        BlockBreak.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BlockBreak, 'tStartRefresh')  # time at next scr refresh
        BlockBreak.setAutoDraw(True)
    if BlockBreak.status == STARTED:
        el_tracker.sendMessage('blockBreak %s' % break_2Clock.getTime())
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > BlockBreak.tStartRefresh + 180-frameTolerance:
            # keep track of stop time/frame for later
            BlockBreak.tStop = t  # not accounting for scr refresh
            BlockBreak.frameNStop = frameN  # exact frame index
            win.timeOnFlip(BlockBreak, 'tStopRefresh')  # time at next scr refresh
            BlockBreak.setAutoDraw(False)
            theseKeys = start2.getKeys(keyList=['space','q'], waitRelease=False)
            _start2_allKeys.extend(theseKeys)
            if len(_start2_allKeys):
                start2.keys = _start2_allKeys[-1].name  # just the last key pressed
                start2.rt = _start2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 180.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # *start2* updates
    waitOnFlip = False
    if start2.status == NOT_STARTED and tThisFlip >= 180.0-frameTolerance:
        # keep track of start time/frame for later
        start2.frameNStart = frameN  # exact frame index
        start2.tStart = t  # local t and not account for scr refresh
        start2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start2, 'tStartRefresh')  # time at next scr refresh
        start2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(start2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(start2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if start2.status == STARTED and not waitOnFlip:
        theseKeys = start2.getKeys(keyList=['space','q'], waitRelease=False)
        _start2_allKeys.extend(theseKeys)
        if len(_start2_allKeys):
            start2.keys = _start2_allKeys[-1].name  # just the last key pressed
            start2.rt = _start2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        thisExp.saveAsWideText(filename+'.csv', delim=',')
        thisExp.saveAsPickle(filename)
        logging.flush()
        terminate_task()
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in break_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "break_2"-------
for thisComponent in break_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if start2.keys in ['', [], None]:  # No response was made
    start2.keys = None
#thisExp.addData('start2.keys',start2.keys)
if start2.keys != None:  # we had a response
    el_tracker.sendMessage('breakEnding %s' % break_2Clock.getTime())
thisExp.nextEntry()
# the Routine "break_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#Recalibrate after the break
# skip this step if running the script in Dummy Mode
if not dummy_mode:
    try:
        el_tracker.doTrackerSetup()
    except RuntimeError as err:
        print('ERROR:', err)
        el_tracker.exitCalibration()
        
#Second retrieval block starts   
# ------Prepare to start Routine "initRecallPics2"-------
continueRoutine = True
# update component parameters for each repeat
retTrials = 0
retNew = 0
retSame = 0
random.shuffle(samePics2)
#same pics are all pictures that came from 'same' trials
#shuffle and put in retrieval list.
#retrievalNew = []
retrievalSame = []

retrievalSame.append(samePics2)
# keep track of which components have finished
initRecallPics2Components = []
for thisComponent in initRecallPics2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
initRecallPics2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1


# -------Run Routine "initRecallPics2"-------
while continueRoutine:
    # get current time
    t = initRecallPics2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=initRecallPics2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        thisExp.saveAsWideText(filename+'.csv', delim=',')
        thisExp.saveAsPickle(filename)
        logging.flush()
        terminate_task()
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in initRecallPics2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "initRecallPics2"-------
for thisComponent in initRecallPics2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "initRecallPics2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
RetrievalBlock2 = data.TrialHandler(nReps=numRetrieval2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='RetrievalBlock2')
thisExp.addLoop(RetrievalBlock2)  # add the loop to the experiment
thisRetrievalBlock2 = RetrievalBlock2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRetrievalBlock2.rgb)
if thisRetrievalBlock2 != None:
    for paramName in thisRetrievalBlock2l:
        exec('{} = thisRetrievalBlock2[paramName]'.format(paramName))

for thisRetrievalBlock2 in RetrievalBlock2:
    trial_category = 'retrieval'
    currentLoop = RetrievalBlock2
    # abbreviate parameter names if possible (e.g. rgb = thisRetrievalBlock2.rgb)
    if thisRetrievalBlock2 != None:
        for paramName in thisRetrievalBlock2l:
            exec('{} = thisRetrievalBlock2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "RetrievalImage"-------
    continueRoutine = True
    rtrial_index = RetrievalBlock2.thisRepN
    trial_category= 'retrieval'
    #start recording eye-movements
    start_eye_tracker(rtrial_index, trial_category)
    
    # send a "TRIALID" message to mark the start of a trial, see Data
    # Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
    el_tracker.sendMessage('!V TRIAL_VAR trialCategory %s' %trial_category)
    el_tracker.sendMessage('!V TRIAL_VAR retTrials %d' %rtrial_index) #HERE
    
    # update component parameters for each repeat
    retrievalImage = None
    
    if retProb < 1.1:
        retType = "old"
        RetrievalBlock2.addData("retType", "old")
        length = len(samePics)
        if(length == 0):
            sys.exit(1)
        retrievalImage = 'images/' + samePics2[retSame] + '.png'
        retSame = retSame + 1
    #so I am telling it that it needs to take an image from same pics
    #and iterate through those pictures with more retrieval trials
    #no 'new' retrieval at this point.
    else:
        retType = "new"
        RetrievalBlock2.addData("retType", "new")
        length = len(newPics)
        if(length == 0):
            sys.exit(1)
        retrievalImage = 'images/' + newPics[retNew] + '.png'
        retNew = retNew + 1
        
    retIMG.setImage(retrievalImage)
    sound_pop7.setSound('POP.wav', hamming=True)
    sound_pop7.setVolume(1.0, log=False)
    # keep track of which components have finished
    RetrievalImageComponents = [retIMG, sound_pop7]
    for thisComponent in RetrievalImageComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RetrievalImageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "RetrievalImage"-------
    while continueRoutine:
        # get current time
        t = RetrievalImageClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RetrievalImageClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *retIMG* updates
        if retIMG.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            retIMG.frameNStart = frameN  # exact frame index
            retIMG.tStart = t  # local t and not account for scr refresh
            retIMG.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(retIMG, 'tStartRefresh')  # time at next scr refresh
            retIMG.setAutoDraw(True)
        if retIMG.status == STARTED:
            el_tracker.sendMessage('retImg.running %s' % RetrievalImageClock.getTime())
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > retIMG.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                retIMG.tStop = t  # not accounting for scr refresh
                retIMG.frameNStop = frameN  # exact frame index
                win.timeOnFlip(retIMG, 'tStopRefresh')  # time at next scr refresh
                retIMG.setAutoDraw(False)
        # start/stop sound_pop7
        if sound_pop7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_pop7.frameNStart = frameN  # exact frame index
            sound_pop7.tStart = t  # local t and not account for scr refresh
            sound_pop7.tStartRefresh = tThisFlipGlobal  # on global time
            sound_pop7.play(when=win)  # sync with win flip
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.saveAsWideText(filename+'.csv', delim=',')
            thisExp.saveAsPickle(filename)
            logging.flush()
            terminate_task()
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RetrievalImageComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
# -------Ending Routine "RetrievalImage"-------
for thisComponent in RetrievalImageComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_pop7.stop()  # ensure sound has stopped at end of routine
el_tracker.sendMessage('retImg.ending %s' % RetrievalImageClock.getTime())
el_tracker.sendMessage('!V TRIAL_VAR retIMG %s' %retrievalImage)
RetrievalTrials.addData("retrievalTrials", str(retTrials))
RetrievalBlock2.addData("TRIAL_INDEX", str(TRIAL_INDEX))
RetrievalBlock2.addData("retIMG", str(retrievalImage))  # Note the closing parenthesis fix here
#print( "this is ret trial", RetrievalTrials.thisRepN)
# the Routine "RetrievalImage" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

    
# ------Prepare to start Routine "Q2Text"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
Q2TextComponents = [question_text]
for thisComponent in Q2TextComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Q2TextClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
    
    # -------Run Routine "Q2Text"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Q2TextClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Q2TextClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
        
    # *question_text* updates
    if question_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        question_text.frameNStart = frameN  # exact frame index
        question_text.tStart = t  # local t and not account for scr refresh
        question_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(question_text, 'tStartRefresh')  # time at next scr refresh
        question_text.setAutoDraw(True)
    if question_text.status == STARTED:
        el_tracker.sendMessage('methodText %s' % Q2TextClock.getTime())
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > question_text.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            question_text.tStop = t  # not accounting for scr refresh
            question_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(question_text, 'tStopRefresh')  # time at next scr refresh
            question_text.setAutoDraw(False)
                
        
        # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        thisExp.saveAsWideText(filename+'.csv', delim=',')
        thisExp.saveAsPickle(filename)
        logging.flush()
        terminate_task()
        core.quit()
        
        # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Q2TextComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
        
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    
# -------Ending Routine "Q2Text"-------
for thisComponent in Q2TextComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
    el_tracker.sendMessage('textEnding %s' % Q2TextClock.getTime())
    
    # ------Prepare to start Routine "Decision"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the Order_Position_Response
    Order_Position_Response.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    DecisionComponents = [decisionQ_2, first_left, second_middle, third_right, First, Second, Third, Order_Position_Response]
    for thisComponent in DecisionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    DecisionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Decision"-------
    while continueRoutine:
        # get current time
        t = DecisionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=DecisionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *decisionQ_2* updates
        if decisionQ_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            decisionQ_2.frameNStart = frameN  # exact frame index
            decisionQ_2.tStart = t  # local t and not account for scr refresh
            decisionQ_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(decisionQ_2, 'tStartRefresh')  # time at next scr refresh
            decisionQ_2.setAutoDraw(True)
        
        # *first_left* updates
        if first_left.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            first_left.frameNStart = frameN  # exact frame index
            first_left.tStart = t  # local t and not account for scr refresh
            first_left.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(first_left, 'tStartRefresh')  # time at next scr refresh
            first_left.setAutoDraw(True)
    
        
        # *second_middle* updates
        if second_middle.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            second_middle.frameNStart = frameN  # exact frame index
            second_middle.tStart = t  # local t and not account for scr refresh
            second_middle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(second_middle, 'tStartRefresh')  # time at next scr refresh
            second_middle.setAutoDraw(True)
        
        # *third_right* updates
        if third_right.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            third_right.frameNStart = frameN  # exact frame index
            third_right.tStart = t  # local t and not account for scr refresh
            third_right.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(third_right, 'tStartRefresh')  # time at next scr refresh
            third_right.setAutoDraw(True)
        
        # *First* updates
        if First.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            First.frameNStart = frameN  # exact frame index
            First.tStart = t  # local t and not account for scr refresh
            First.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(First, 'tStartRefresh')  # time at next scr refresh
            First.setAutoDraw(True)
        
        # *Second* updates
        if Second.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Second.frameNStart = frameN  # exact frame index
            Second.tStart = t  # local t and not account for scr refresh
            Second.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Second, 'tStartRefresh')  # time at next scr refresh
            Second.setAutoDraw(True)
        
        # *Third* updates
        if Third.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Third.frameNStart = frameN  # exact frame index
            Third.tStart = t  # local t and not account for scr refresh
            Third.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Third, 'tStartRefresh')  # time at next scr refresh
            Third.setAutoDraw(True)
        # *Order_Position_Response* updates
        if Order_Position_Response.status == NOT_STARTED and t >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Order_Position_Response.frameNStart = frameN  # exact frame index
            Order_Position_Response.tStart = t  # local t and not account for scr refresh
            Order_Position_Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Order_Position_Response, 'tStartRefresh')  # time at next scr refresh
            Order_Position_Response.status = STARTED
            Order_Position_Response.mouseClock.reset()
            prevButtonState = Order_Position_Response.getPressed()  # if button is down already this ISN'T a new click
        if Order_Position_Response.status == STARTED:  # only update if started and not finished!
            buttons = Order_Position_Response.getPressed()
            el_tracker.sendMessage('Decision %s' % DecisionClock.getTime())
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [first_left,second_middle,third_right]:
                        if obj.contains(Order_Position_Response):
                            gotValidClick = True
                            Order_Position_Response.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.saveAsWideText(filename+'.csv', delim=',')
            thisExp.saveAsPickle(filename)
            logging.flush()
            terminate_task()
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in DecisionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    el_tracker.sendMessage ('!V TRIAL_VAR orderResponse %s' %Order_Position_Response.clicked_name[0])
    
    # -------Ending Routine "Decision"-------
    for thisComponent in DecisionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    retTrials = retTrials + 1
    TRIAL_INDEX = TRIAL_INDEX + 1
    RetrievalBlock2.addData("retTrials", str(retTrials))
    RetrievalBlock2.addData("TRIAL_INDEX", str(TRIAL_INDEX))
    thisExp.addData("TRIAL_INDEX", str(TRIAL_INDEX))
    el_tracker.sendMessage('!V TRIAL_VAR retTrials %d' %retTrials)
    el_tracker.sendMessage('decisionClock %s' % DecisionClock)
    # store data for RetrievalBlock2 (TrialHandler)
    x, y = Order_Position_Response.getPos()
    buttons = Order_Position_Response.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        for obj in [first_left,second_middle,third_right]:
            if obj.contains(Order_Position_Response):
                gotValidClick = True
                Order_Position_Response.clicked_name.append(obj.name)
    RetrievalBlock2.addData('Order_Position_Response.leftButton', buttons[0])
    RetrievalBlock2.addData('Order_Position_Response.midButton', buttons[1])
    RetrievalBlock2.addData('Order_Position_Response.rightButton', buttons[2])
    if len(Order_Position_Response.clicked_name):
        RetrievalBlock2.addData('Order_Position_Response.clicked_name', Order_Position_Response.clicked_name[0])
    
    # the Routine "Decision" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "clicked_sound"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    clickedSound.setSound('click.wav', secs=0.5, hamming=True)
    clickedSound.setVolume(1.0, log=False)
    # keep track of which components have finished
    clicked_soundComponents = [clickedSound]
    for thisComponent in clicked_soundComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    clicked_soundClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "clicked_sound"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = clicked_soundClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=clicked_soundClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop clickedSound
        if clickedSound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            clickedSound.frameNStart = frameN  # exact frame index
            clickedSound.tStart = t  # local t and not account for scr refresh
            clickedSound.tStartRefresh = tThisFlipGlobal  # on global time
            clickedSound.play(when=win)  # sync with win flip
        if clickedSound.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > clickedSound.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                clickedSound.tStop = t  # not accounting for scr refresh
                clickedSound.frameNStop = frameN  # exact frame index
                win.timeOnFlip(clickedSound, 'tStopRefresh')  # time at next scr refresh
                clickedSound.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.saveAsWideText(filename+'.csv', delim=',')
            thisExp.saveAsPickle(filename)
            logging.flush()
            terminate_task()
            core.quit()
            # -------Ending Routine "clicked_sound"-------
    for thisComponent in clicked_soundComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    clickedSound.stop()  # ensure sound has stopped at end of routine
    RetrievalTrials.addData('clickedSound.started', clickedSound.tStartRefresh)
    RetrievalTrials.addData('clickedSound.stopped', clickedSound.tStopRefresh)
    thisExp.nextEntry()
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename+'.csv', delim=',')
    thisExp.saveAsPickle(filename)
    logging.flush()

# completed numRetrieval repeats of 'RetrievalBlock2'
#store eye-tracking related data in edf

# record trial variables to the EDF data file, for details, see Data
# Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
el_tracker.sendMessage('!V TRIAL_VAR retIMG %s' %retrievalImage)
RetrievalBlock2.addData("retrievalTrials", str(retTrials))
RetrievalBlock2.addData("TRIAL_INDEX", str(TRIAL_INDEX))
RetrievalBlock2.addData("retIMG", str(retrievalImage))
el_tracker.sendMessage('!V TRIAL_VAR retTrials %d' %retTrials)
el_tracker.sendMessage ('!V TRIAL_VAR orderResponse %s' %Order_Position_Response.clicked_name[0])

    
# send a 'TRIAL_RESULT' message to mark the end of trial, see Data
# Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
el_tracker.sendMessage('TRIAL_RESULT %d' % pylink.TRIAL_OK)
#ret2end
# ------Prepare to start Routine "EndScreen"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndScreenComponents = [end]
for thisComponent in EndScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "EndScreen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end* updates
    if end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end.frameNStart = frameN  # exact frame index
        end.tStart = t  # local t and not account for scr refresh
        end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end, 'tStartRefresh')  # time at next scr refresh
        end.setAutoDraw(True)
    if end.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            end.tStop = t  # not accounting for scr refresh
            end.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end, 'tStopRefresh')  # time at next scr refresh
            end.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        thisExp.saveAsWideText(filename+'.csv', delim=',')
        thisExp.saveAsPickle(filename)
        logging.flush()
        core.quit()
        # End the eyetracker session
        terminate_task()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EndScreen"-------
for thisComponent in EndScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('end.started', end.tStartRefresh)
thisExp.addData('end.stopped', end.tStopRefresh)
# End the eyetracker session
terminate_task()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# End the eyetracker session
terminate_task()
logging.flush()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim=',')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
   