from __future__ import print_function
# ------------------------------------------------------------------------------------------------
# Copyright (c) 2016 Microsoft Corporation
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
# associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
# NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# ------------------------------------------------------------------------------------------------

# Tutorial sample #2: Run simple mission using raw XML

from builtins import range
import MalmoPython
import os
import sys
import time
import json
from Tile import *
from Board import *

if sys.version_info[0] == 2:
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately
else:
    import functools
    print = functools.partial(print, flush=True)

# More interesting generator string: "3;7,44*49,73,35:1,159:4,95:13,35:13,159:11,95:10,159:14,159:6,35:6,95:6;12;"

def _convertIndexToXZ(index,rows,cols):
    z = index%cols + 1
    x = abs(rows - index//cols -1)
    return (x,z)

def generateXMLFromBoard(board):
    input_xml = ""
    index = 0
    for eachTile in board.board:
        (x,z) = _convertIndexToXZ(index,board.rows,board.cols)
        if eachTile.isGolem():
            input_xml+= "<DrawEntity x= "+ "\"" +str(x+0.5)+"\""+ " y=\"19\" z="+ "\""+str(z+0.5)+"\""+" type=\"Zombie\" />\n"#uncomment to spawn zombie
            input_xml += "<DrawBlock x= " +"\""+ str(x)+"\""+ " y=\"17\" z= " +"\""+ str(z)+"\"" +" type=\"redstone_block\" />\n"
        elif eachTile.isPit():
            input_xml += "<DrawBlock x= " +"\""+ str(x)+"\""+ " y=\"17\" z= " +"\""+ str(z)+"\"" +" type=\"air\" />\n"
        elif eachTile.isTreasure():
              input_xml += "<DrawBlock x= " +"\""+ str(x)+"\""+ " y=\"17\" z= " +"\""+ str(z)+"\"" +" type=\"air\" />\n"
              input_xml += "<DrawBlock x= " +"\""+ str(x)+"\""+ " y=\"17\" z= " +"\""+ str(z)+"\"" +" type=\"gold_block\" />\n"
        elif eachTile.isExit():
            input_xml += "<DrawBlock x= " +"\""+ str(x)+"\""+ " y=\"17\" z= " +"\""+ str(z)+"\"" +" type=\"emerald_block\" />\n"     
        else:
            #print("here",x,z)
            input_xml += "<DrawBlock x= " +"\""+ str(x)+"\""+ " y=\"17\" z= " +"\""+ str(z)+"\"" +" type=\"lapis_block\" />\n"
        index += 1    
    return mapXML(input_xml,clearStructures(board.rows,board.cols,17,True))

def clearStructures(number_row,num_cols,y,toHeight=False):
    toClear = ""
    maxY = y
    if toHeight:  
        starty = 1
    else:
        starty = y
    for y in range(starty,maxY+1):
        for index in range(number_row*num_cols):
            (x,z) = _convertIndexToXZ(index,number_row,num_cols)
            toClear += "<DrawBlock x= " +"\""+ str(x)+"\""+ " y=\""+str(y)+"\" z= " +"\""+ str(z)+"\"" +" type=\"air\" />\n"
    return toClear

def mapXML(input_xml,clear_xml):
    return '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
            <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            
              <About>
                <Summary>Hello world!</Summary>
              </About>
              <ServerSection>
              <ServerInitialConditions>
                  <Time>
                    <StartTime>15000</StartTime>
                    <AllowPassageOfTime>false</AllowPassageOfTime>
                  </Time>
              </ServerInitialConditions>
                <ServerHandlers>
                  <FlatWorldGenerator generatorString="3;5*1,35:15;1;village(size=10)"/>
                  <DrawingDecorator>
                      '''+"""{}\n{}""".format(clear_xml,input_xml)+'''
                  </DrawingDecorator>
                  <ServerQuitWhenAnyAgentFinishes/>
                </ServerHandlers>
              </ServerSection>
              
              <AgentSection mode="Creative">
                <Name>GolumGlobe</Name>
                <AgentStart>
                    <Placement x="0.5" y="18.0" z="1.5" yaw="0"/>
                </AgentStart>
                <AgentHandlers>
                  <ChatCommands/>
                  <ObservationFromFullStats/>
                  <ContinuousMovementCommands turnSpeedDegs="400"/>
                </AgentHandlers>
              </AgentSection>
            </Mission>'''
