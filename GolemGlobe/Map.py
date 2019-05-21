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

if sys.version_info[0] == 2:
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately
else:
    import functools
    print = functools.partial(print, flush=True)

# More interesting generator string: "3;7,44*49,73,35:1,159:4,95:13,35:13,159:11,95:10,159:14,159:6,35:6,95:6;12;"

missionXML='''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
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
                      <DrawBlock x="0" y="7" z="1" type="air"/>
                      <DrawBlock x="1" y="7" z="1" type="air"/>
                      <DrawBlock x="2" y="7" z="1" type="air"/>
                      <DrawBlock x="3" y="7" z="1" type="air"/>
                      <DrawBlock x="4" y="7" z="1" type="air"/>
                      <DrawBlock x="5" y="7" z="1" type="air"/>
                      <DrawBlock x="6" y="7" z="1" type="air"/>
                      <DrawBlock x="7" y="7" z="1" type="air"/>
                      <DrawBlock x="8" y="7" z="1" type="air"/>
                      <DrawBlock x="9" y="7" z="1" type="air"/>
                      <DrawBlock x="0" y="7" z="2" type="air"/>
                      <DrawBlock x="1" y="7" z="2" type="air"/>
                      <DrawBlock x="2" y="7" z="2" type="air"/>
                      <DrawBlock x="3" y="7" z="2" type="air"/>
                      <DrawBlock x="4" y="7" z="2" type="air"/>
                      <DrawBlock x="5" y="7" z="2" type="air"/>
                      <DrawBlock x="6" y="7" z="2" type="air"/>
                      <DrawBlock x="7" y="7" z="2" type="air"/>
                      <DrawBlock x="8" y="7" z="2" type="air"/>
                      <DrawBlock x="9" y="7" z="2" type="air"/> 
                      <DrawBlock x="0" y="7" z="3" type="air"/>
                      <DrawBlock x="1" y="7" z="3" type="air"/>
                      <DrawBlock x="2" y="7" z="3" type="air"/>
                      <DrawBlock x="3" y="7" z="3" type="air"/>
                      <DrawBlock x="4" y="7" z="3" type="air"/>
                      <DrawBlock x="5" y="7" z="3" type="air"/>
                      <DrawBlock x="6" y="7" z="3" type="air"/>
                      <DrawBlock x="7" y="7" z="3" type="air"/>
                      <DrawBlock x="8" y="7" z="3" type="air"/>
                      <DrawBlock x="9" y="7" z="3" type="air"/>
                      <DrawBlock x="0" y="7" z="4" type="air"/>
                      <DrawBlock x="1" y="7" z="4" type="air"/>
                      <DrawBlock x="2" y="7" z="4" type="air"/>
                      <DrawBlock x="3" y="7" z="4" type="air"/>
                      <DrawBlock x="4" y="7" z="4" type="air"/>
                      <DrawBlock x="5" y="7" z="4" type="air"/>
                      <DrawBlock x="6" y="7" z="4" type="air"/>
                      <DrawBlock x="7" y="7" z="4" type="air"/>
                      <DrawBlock x="8" y="7" z="4" type="air"/>
                      <DrawBlock x="9" y="7" z="4" type="air"/>
                      <DrawBlock x="0" y="7" z="5" type="air"/>
                      <DrawBlock x="1" y="7" z="5" type="air"/>
                      <DrawBlock x="2" y="7" z="5" type="air"/>
                      <DrawBlock x="3" y="7" z="5" type="air"/>
                      <DrawBlock x="4" y="7" z="5" type="air"/>
                      <DrawBlock x="5" y="7" z="5" type="air"/>
                      <DrawBlock x="6" y="7" z="5" type="air"/>
                      <DrawBlock x="7" y="7" z="5" type="air"/>
                      <DrawBlock x="8" y="7" z="5" type="air"/>
                      <DrawBlock x="9" y="7" z="5" type="air"/>
                      <DrawBlock x="0" y="7" z="6" type="air"/>
                      <DrawBlock x="1" y="7" z="6" type="air"/>
                      <DrawBlock x="2" y="7" z="6" type="air"/>
                      <DrawBlock x="3" y="7" z="6" type="air"/>
                      <DrawBlock x="4" y="7" z="6" type="air"/>
                      <DrawBlock x="5" y="7" z="6" type="air"/>
                      <DrawBlock x="6" y="7" z="6" type="air"/>
                      <DrawBlock x="7" y="7" z="6" type="air"/>
                      <DrawBlock x="8" y="7" z="6" type="air"/>
                      <DrawBlock x="9" y="7" z="6" type="air"/>
  
                      <DrawBlock x="0" y="7" z="7" type="air"/>
                      <DrawBlock x="1" y="7" z="7" type="air"/>
                      <DrawBlock x="2" y="7" z="7" type="air"/>
                      <DrawBlock x="3" y="7" z="7" type="air"/>
                      <DrawBlock x="4" y="7" z="7" type="air"/>
                      <DrawBlock x="5" y="7" z="7" type="air"/>
                      <DrawBlock x="6" y="7" z="7" type="air"/>
                      <DrawBlock x="7" y="7" z="7" type="air"/>
                      <DrawBlock x="8" y="7" z="7" type="air"/>
                      <DrawBlock x="9" y="7" z="7" type="air"/>
                      <DrawBlock x="0" y="7" z="8" type="air"/>
                      <DrawBlock x="1" y="7" z="8" type="air"/>
                      <DrawBlock x="2" y="7" z="8" type="air"/>
                      <DrawBlock x="3" y="7" z="8" type="air"/>
                      <DrawBlock x="4" y="7" z="8" type="air"/>
                      <DrawBlock x="5" y="7" z="8" type="air"/>
                      <DrawBlock x="6" y="7" z="8" type="air"/>
                      <DrawBlock x="7" y="7" z="8" type="air"/>
                      <DrawBlock x="8" y="7" z="8" type="air"/>
                      <DrawBlock x="9" y="7" z="8" type="air"/>
                      <DrawBlock x="0" y="7" z="9" type="air"/>
                      <DrawBlock x="1" y="7" z="9" type="air"/>
                      <DrawBlock x="2" y="7" z="9" type="air"/>
                      <DrawBlock x="3" y="7" z="9" type="air"/>
                      <DrawBlock x="4" y="7" z="9" type="air"/>
                      <DrawBlock x="5" y="7" z="9" type="air"/>
                      <DrawBlock x="6" y="7" z="9" type="air"/>
                      <DrawBlock x="7" y="7" z="9" type="air"/>
                      <DrawBlock x="8" y="7" z="9" type="air"/>
                      <DrawBlock x="9" y="7" z="9" type="air"/>
                      <DrawBlock x="0" y="7" z="10" type="air"/>
                      <DrawBlock x="1" y="7" z="10" type="air"/>
                      <DrawBlock x="2" y="7" z="10" type="air"/>
                      <DrawBlock x="3" y="7" z="10" type="air"/>
                      <DrawBlock x="4" y="7" z="10" type="air"/>
                      <DrawBlock x="5" y="7" z="10" type="air"/>
                      <DrawBlock x="6" y="7" z="10" type="air"/>
                      <DrawBlock x="7" y="7" z="10" type="air"/>
                      <DrawBlock x="8" y="7" z="10" type="air"/>
                      <DrawBlock x="9" y="7" z="10" type="air"/>
                      
                      <DrawBlock x="3" y="7" z="4" type="air"/>
                      <DrawBlock x="3" y="6" z="4" type="diamond_block"/>
                      <DrawEntity x="3.5"  y="9" z="4.5" type="Creeper" />
                      
                      <DrawBlock x="1" y="6" z="9" type="air"/>
                      <DrawBlock x="0" y="8" z="1" type="emerald_block"/>
                      <DrawBlock x="1" y="8" z="1" type="diamond_block"/>
                      <DrawBlock x="2" y="8" z="1" type="diamond_block"/>
                      <DrawBlock x="3" y="8" z="1" type="diamond_block"/>
                      <DrawBlock x="4" y="8" z="1" type="diamond_block"/>
                      <DrawBlock x="5" y="8" z="1" type="diamond_block"/>
                      <DrawBlock x="6" y="8" z="1" type="diamond_block"/>
                      <DrawBlock x="7" y="8" z="1" type="diamond_block"/>
                      <DrawBlock x="8" y="8" z="1" type="diamond_block"/>
                      <DrawBlock x="9" y="8" z="1" type="diamond_block"/>
                      <DrawBlock x="0" y="8" z="2" type="diamond_block"/>
                      <DrawBlock x="1" y="8" z="2" type="diamond_block"/>
                      <DrawBlock x="2" y="8" z="2" type="diamond_block"/>
                      <DrawBlock x="3" y="8" z="2" type="diamond_block"/>
                      <DrawBlock x="4" y="8" z="2" type="diamond_block"/>
                      <DrawBlock x="5" y="8" z="2" type="diamond_block"/>
                      <DrawBlock x="6" y="8" z="2" type="diamond_block"/>
                      <DrawBlock x="7" y="8" z="2" type="diamond_block"/>
                      <DrawBlock x="8" y="8" z="2" type="diamond_block"/>
                      <DrawBlock x="9" y="8" z="2" type="diamond_block"/> 
                      <DrawBlock x="0" y="8" z="3" type="diamond_block"/>
                      <DrawBlock x="1" y="8" z="3" type="diamond_block"/>
                      <DrawBlock x="2" y="8" z="3" type="diamond_block"/>
                      <DrawBlock x="3" y="8" z="3" type="diamond_block"/>
                      <DrawBlock x="4" y="8" z="3" type="diamond_block"/>
                      <DrawBlock x="5" y="8" z="3" type="diamond_block"/>
                      <DrawBlock x="6" y="8" z="3" type="diamond_block"/>
                      <DrawBlock x="7" y="8" z="3" type="diamond_block"/>
                      <DrawBlock x="8" y="8" z="3" type="diamond_block"/>
                      <DrawBlock x="9" y="8" z="3" type="diamond_block"/>
                      <DrawBlock x="0" y="8" z="4" type="diamond_block"/>
                      <DrawBlock x="1" y="8" z="4" type="diamond_block"/>
                      <DrawBlock x="2" y="8" z="4" type="diamond_block"/>
                      <DrawBlock x="4" y="8" z="4" type="diamond_block"/>
                      <DrawBlock x="5" y="8" z="4" type="diamond_block"/>
                      <DrawBlock x="6" y="8" z="4" type="diamond_block"/>
                      <DrawBlock x="7" y="8" z="4" type="diamond_block"/>
                      <DrawBlock x="8" y="8" z="4" type="diamond_block"/>
                      <DrawBlock x="9" y="8" z="4" type="diamond_block"/>
                      <DrawBlock x="0" y="8" z="5" type="diamond_block"/>
                      <DrawBlock x="1" y="8" z="5" type="diamond_block"/>
                      <DrawBlock x="2" y="8" z="5" type="diamond_block"/>
                      <DrawBlock x="3" y="8" z="5" type="diamond_block"/>
                      <DrawBlock x="4" y="8" z="5" type="diamond_block"/>
                      <DrawBlock x="5" y="8" z="5" type="diamond_block"/>
                      <DrawBlock x="6" y="8" z="5" type="diamond_block"/>
                      <DrawBlock x="7" y="8" z="5" type="diamond_block"/>
                      <DrawBlock x="8" y="8" z="5" type="diamond_block"/>
                      <DrawBlock x="9" y="8" z="5" type="diamond_block"/>
                      <DrawBlock x="0" y="8" z="6" type="diamond_block"/>
                      <DrawBlock x="1" y="8" z="6" type="diamond_block"/>
                      <DrawBlock x="2" y="8" z="6" type="diamond_block"/>
                      <DrawBlock x="3" y="8" z="6" type="diamond_block"/>
                      <DrawBlock x="4" y="8" z="6" type="diamond_block"/>
                      <DrawBlock x="5" y="8" z="6" type="diamond_block"/>
                      <DrawBlock x="6" y="8" z="6" type="diamond_block"/>
                      <DrawBlock x="7" y="8" z="6" type="diamond_block"/>
                      <DrawBlock x="8" y="8" z="6" type="diamond_block"/>
                      <DrawBlock x="9" y="8" z="6" type="diamond_block"/>
  
                      <DrawBlock x="0" y="8" z="7" type="diamond_block"/>
                      <DrawBlock x="1" y="8" z="7" type="diamond_block"/>
                      <DrawBlock x="2" y="8" z="7" type="diamond_block"/>
                      <DrawBlock x="3" y="8" z="7" type="air"/>
                      <DrawBlock x="4" y="8" z="7" type="diamond_block"/>
                      <DrawBlock x="5" y="8" z="7" type="diamond_block"/>
                      <DrawBlock x="6" y="8" z="7" type="diamond_block"/>
                      <DrawBlock x="7" y="8" z="7" type="diamond_block"/>
                      <DrawBlock x="8" y="8" z="7" type="diamond_block"/>
                      <DrawBlock x="9" y="8" z="7" type="diamond_block"/>
                      <DrawBlock x="0" y="8" z="8" type="diamond_block"/>
                      <DrawBlock x="1" y="8" z="8" type="diamond_block"/>
                      <DrawBlock x="2" y="8" z="8" type="diamond_block"/>
                      <DrawBlock x="3" y="8" z="8" type="diamond_block"/>
                      <DrawBlock x="4" y="8" z="8" type="gold_block"/>
                      <DrawItem x="4" y="9" z="8" type="gold_nugget"/>
                      <DrawBlock x="5" y="8" z="8" type="diamond_block"/>
                      <DrawBlock x="6" y="8" z="8" type="diamond_block"/>
                      <DrawBlock x="7" y="8" z="8" type="diamond_block"/>
                      <DrawBlock x="8" y="8" z="8" type="diamond_block"/>
                      <DrawBlock x="9" y="8" z="8" type="diamond_block"/>
                      <DrawBlock x="0" y="8" z="9" type="diamond_block"/>
                      <DrawBlock x="1" y="8" z="9" type="air"/>
                      <DrawBlock x="2" y="8" z="9" type="diamond_block"/>
                      <DrawBlock x="3" y="8" z="9" type="diamond_block"/>
                      <DrawBlock x="4" y="8" z="9" type="diamond_block"/>
                      <DrawBlock x="5" y="8" z="9" type="diamond_block"/>
                      <DrawBlock x="6" y="8" z="9" type="diamond_block"/>
                      <DrawBlock x="7" y="8" z="9" type="diamond_block"/>
                      <DrawBlock x="8" y="8" z="9" type="diamond_block"/>
                      <DrawBlock x="9" y="8" z="9" type="diamond_block"/>
                      <DrawBlock x="0" y="8" z="10" type="diamond_block"/>
                      <DrawBlock x="1" y="8" z="10" type="diamond_block"/>
                      <DrawBlock x="2" y="8" z="10" type="diamond_block"/>
                      <DrawBlock x="3" y="8" z="10" type="diamond_block"/>
                      <DrawBlock x="4" y="8" z="10" type="diamond_block"/>
                      <DrawBlock x="5" y="8" z="10" type="diamond_block"/>
                      <DrawBlock x="6" y="8" z="10" type="diamond_block"/>
                      <DrawBlock x="7" y="8" z="10" type="diamond_block"/>
                      <DrawBlock x="8" y="8" z="10" type="diamond_block"/>
                      <DrawBlock x="9" y="8" z="10" type="diamond_block"/>
                      
                  </DrawingDecorator>
                  <ServerQuitFromTimeUp timeLimitMs="300000"/>
                  <ServerQuitWhenAnyAgentFinishes/>
                </ServerHandlers>
              </ServerSection>
              
              <AgentSection mode="Creative">
                <Name>GolumGlobe</Name>
                <AgentStart>
                    <Placement x="0.5" y="9.0" z="1.5" yaw="0"/>
                    <Inventory>
                        <InventoryItem slot="0" type = "diamond_sword"/>
                    </Inventory>
                </AgentStart>
                <AgentHandlers>
                  <ObservationFromFullStats/>
                  
                  <ContinuousMovementCommands turnSpeedDegs="360"/>
                  <AbsoluteMovementCommands/>
                </AgentHandlers>
              </AgentSection>
            </Mission>'''


