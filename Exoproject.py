import opensim as osim
import math


model = osim.Model()
model.setName('Exoarm')
model.setGravity(osim.Vec3(0, -9.81, 0))  # Gravity along Y-axis


upperarm = osim.Body('upperarm', 2.0, osim.Vec3(0),
    osim.Inertia(0.05, 0.05, 0.05, 0, 0, 0))
geom_upperarm = osim.Cylinder(0.04, 0.15)
geom_upperarm.upd_Appearance().set_color(osim.Vec3(0.2, 0.6, 1.0))
upperarm.attachGeometry(geom_upperarm)


shoulder_joint = osim.WeldJoint(
    'shoulder_joint',
    model.getGround(), osim.Vec3(0, 0.9, 0), osim.Vec3(0, 0, 0),
    upperarm, osim.Vec3(0, 0.15, 0), osim.Vec3(0, 0, 0)
)

model.addBody(upperarm)
model.addJoint(shoulder_joint)


forearm = osim.Body('forearm', 1.5, osim.Vec3(0),
    osim.Inertia(0.05, 0.05, 0.05, 0, 0, 0))
geom_forearm = osim.Cylinder(0.04, 0.15)
geom_forearm.upd_Appearance().set_color(osim.Vec3(0.2, 1.0, 0.2))
forearm.attachGeometry(geom_forearm)
ring = osim.Body('arm_ring', 0.1, osim.Vec3(0),
    osim.Inertia(0.001, 0.001, 0.001, 0, 0, 0))


geom_ring = osim.Cylinder(0.045, 0.02)  
geom_ring.upd_Appearance().set_color(osim.Vec3(0.8, 0.8, 0.8))  
ring.attachGeometry(geom_ring)


ring_joint = osim.WeldJoint(
    'arm_ring_joint',
    upperarm, osim.Vec3(0, 0.09, 0), osim.Vec3(0, 0, 0),
    ring, osim.Vec3(0, 0, 0), osim.Vec3(0, 0, 0)
)

model.addBody(ring)
model.addJoint(ring_joint)


elbow_joint = osim.PinJoint(
    'elbow_joint',
    upperarm, osim.Vec3(0, -0.15, 0), osim.Vec3(0, 0, 0),
    forearm, osim.Vec3(0, -0.15, 0), osim.Vec3(0, 0, 0)
)

elbow_coord = elbow_joint.upd_coordinates(0)
elbow_coord.setName('elbow_flex')
elbow_coord.setDefaultValue(math.radians(-150))
elbow_coord.setRangeMin(math.radians(-150))
elbow_coord.setRangeMax(math.radians(-30))
elbow_coord.set_locked(True)  

model.addBody(forearm)
model.addJoint(elbow_joint)
forearm_ring_start = osim.Body('forearm_ring_start', 0.05, osim.Vec3(0),
    osim.Inertia(0.0005, 0.0005, 0.0005, 0, 0, 0))
geom_start = osim.Cylinder(0.045, 0.01)  
geom_start.upd_Appearance().set_color(osim.Vec3(0.9, 0.6, 0.2))  
forearm_ring_start.attachGeometry(geom_start)

forearm_ring_start_joint = osim.WeldJoint(
    'forearm_ring_start_joint',
    forearm, osim.Vec3(0, -0.08, 0), osim.Vec3(0, 0, 0),   
    forearm_ring_start, osim.Vec3(0, 0, 0), osim.Vec3(0, 0, 0)
)

model.addBody(forearm_ring_start)
model.addJoint(forearm_ring_start_joint)


forearm_ring_end = osim.Body('forearm_ring_end', 0.05, osim.Vec3(0),
    osim.Inertia(0.0005, 0.0005, 0.0005, 0, 0, 0))
geom_end = osim.Cylinder(0.045, 0.01)
geom_end.upd_Appearance().set_color(osim.Vec3(0.3, 0.8, 1.0))  
forearm_ring_end.attachGeometry(geom_end)

forearm_ring_end_joint = osim.WeldJoint(
    'forearm_ring_end_joint',
    forearm, osim.Vec3(0, 0.15, 0), osim.Vec3(0, 0, 0),   
    forearm_ring_end, osim.Vec3(0, 0, 0), osim.Vec3(0, 0, 0)
)

model.addBody(forearm_ring_end)
model.addJoint(forearm_ring_end_joint)



thumb = osim.Body('thumb', 0.2, osim.Vec3(0),
    osim.Inertia(0.001, 0.001, 0.001, 0, 0, 0))
geom_thumb = osim.Cylinder(0.01, 0.03)  
geom_thumb.upd_Appearance().set_color(osim.Vec3(1.0, 0.8, 0.2))  
thumb.attachGeometry(geom_thumb)

thumb_joint = osim.PinJoint(
    'thumb_joint',
    forearm, osim.Vec3(-0.04, 0.18, 0), osim.Vec3(0, 0, 0),   
    thumb, osim.Vec3(0, 0, 0), osim.Vec3(0, math.radians(90), 0)             
)

thumb_coord = thumb_joint.upd_coordinates(0)
thumb_coord.setName('thumb_flex')
thumb_coord.setDefaultValue(math.radians(0))
thumb_coord.setRangeMin(math.radians(-90))
thumb_coord.setRangeMax(math.radians(30))
thumb_coord.set_locked(False)


model.addBody(thumb)
model.addJoint(thumb_joint)


finger = osim.Body('finger', 0.2, osim.Vec3(0),
    osim.Inertia(0.001, 0.001, 0.001, 0, 0, 0))
geom_finger = osim.Cylinder(0.01, 0.045)
geom_finger.upd_Appearance().set_color(osim.Vec3(0.8, 0.2, 1.0))  
finger.attachGeometry(geom_finger)

finger_joint = osim.PinJoint(
    'finger_joint',
    forearm, osim.Vec3(0, 0.19, 0.04), osim.Vec3(0, math.radians(90), 0),   
    finger, osim.Vec3(0, 0, 0), osim.Vec3(0, 0, 0)          
)
         

finger_coord = finger_joint.upd_coordinates(0)
finger_coord.setName('finger_flex')
finger_coord.setDefaultValue(math.radians(0))
finger_coord.setRangeMin(math.radians(-90))
finger_coord.setRangeMax(math.radians(30))
finger_coord.set_locked(False)

model.addBody(finger)
model.addJoint(finger_joint)
thumb_ring = osim.Body('thumb_ring', 0.02, osim.Vec3(0),
    osim.Inertia(0.0002, 0.0002, 0.0002, 0, 0, 0))
geom_thumb_ring = osim.Cylinder(0.015, 0.005)  
geom_thumb_ring.upd_Appearance().set_color(osim.Vec3(1.0, 0.4, 0.4))  
thumb_ring.attachGeometry(geom_thumb_ring)

thumb_ring_joint = osim.WeldJoint(
    'thumb_ring_joint',
    thumb, osim.Vec3(0, 0.029, 0), osim.Vec3(0, 0, 0),  
    thumb_ring, osim.Vec3(0, 0, 0), osim.Vec3(0, 0, 0)
)

model.addBody(thumb_ring)
model.addJoint(thumb_ring_joint)
finger_ring = osim.Body('finger_ring', 0.02, osim.Vec3(0),
    osim.Inertia(0.0002, 0.0002, 0.0002, 0, 0, 0))
geom_finger_ring = osim.Cylinder(0.015, 0.005)
geom_finger_ring.upd_Appearance().set_color(osim.Vec3(0.4, 0.8, 1.0)) 
finger_ring.attachGeometry(geom_finger_ring)

finger_ring_joint = osim.WeldJoint(
    'finger_ring_joint',
    finger, osim.Vec3(0, 0.044, 0), osim.Vec3(0, 0, 0),  
    finger_ring, osim.Vec3(0, 0, 0), osim.Vec3(0, 0, 0)
)

model.addBody(finger_ring)
model.addJoint(finger_ring_joint)


cable = osim.PathActuator()
cable.setName('upper_to_forearm_cable')
cable.setOptimalForce(48.0)
cable.setMinControl(0.0)
cable.setMaxControl(1.0)


cable.addNewPathPoint("origin", ring, osim.Vec3(0.045, 0.0, 0.0))  


cable.addNewPathPoint("insertion", forearm_ring_start, osim.Vec3(-0.045, 0.0, 0.0))

model.addForce(cable)


controller = osim.PrescribedController()
controller.setName('cable_controller')
controller.addActuator(cable)


controller.prescribeControlForActuator("upper_to_forearm_cable", osim.Constant(1.0))

model.addController(controller)

elbow_damper = osim.CoordinateActuator('elbow_flex')
elbow_damper.setName('elbow_damper')
elbow_damper.setOptimalForce(1.0)   
elbow_damper.setMinControl(-50)     
elbow_damper.setMaxControl(50)
model.addForce(elbow_damper)


damping_controller = osim.PrescribedController()
damping_controller.setName('elbow_damping_controller')
damping_controller.addActuator(elbow_damper)


damping_controller.prescribeControlForActuator('elbow_damper', osim.Constant(-0.5))

model.addController(damping_controller)
thumb_cable = osim.PathActuator()
thumb_cable.setName('thumb_cable')
thumb_cable.setOptimalForce(0.1)
thumb_cable.setMinControl(0.0)
thumb_cable.setMaxControl(1.0)
thumb_cable.addNewPathPoint("thumb_start", thumb, osim.Vec3(0, 0.03, 0))
thumb_cable.addNewPathPoint("thumb_end", forearm_ring_end, osim.Vec3(0, 0, 0))
model.addForce(thumb_cable)


finger_cable = osim.PathActuator()
finger_cable.setName('finger_cable')
finger_cable.setOptimalForce(0.1)
finger_cable.setMinControl(0.0)
finger_cable.setMaxControl(1.0)
finger_cable.addNewPathPoint("finger_start", finger, osim.Vec3(0, 0.045, 0))
finger_cable.addNewPathPoint("finger_end", forearm_ring_end, osim.Vec3(0, 0.01, 0))
model.addForce(finger_cable)
finger_cable_controller = osim.PrescribedController()
finger_cable_controller.setName('finger_cable_controller')
finger_cable_controller.addActuator(thumb_cable)
finger_cable_controller.addActuator(finger_cable)

# Constant pull (can change later)
finger_cable_controller.prescribeControlForActuator("thumb_cable", osim.Constant(1.0))
finger_cable_controller.prescribeControlForActuator("finger_cable", osim.Constant(1.0))

model.addController(finger_cable_controller)
model.finalizeConnections()
model.printToXML('Exoarm.osim')

print("Saved")  