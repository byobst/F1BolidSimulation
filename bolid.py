#-*- coding: utf-8 -*-

from extra.projectionViewer import ProjectionViewer
from construction.construction import body_nodes, body_edges, tire, road
from extra.wireframe import Wireframe

from extra.extra import Vector3d

if __name__ == "__main__":

    bolid = Wireframe()

    #Bolid building

    count = 0
    height = 80
    dist = 10

    bolid_nodes = body_nodes()
    bolid_edges = body_edges()

    bolid.addNodes(bolid_nodes)
    bolid.addEdges(bolid_edges)

    count += len(bolid_nodes)

    anchor1 = (230, 230, 70)
    anchor2 = (230, 230, -70)
    anchor3 = (570, 230, 50)
    anchor4 = (570, 230, -50)

    (tire_nodes1, tire_edges1) = tire(anchor1, 3, 10, 30, 30, "right", count-1)

    bolid.addNodes(tire_nodes1)
    bolid.addEdges(tire_edges1)
    bolid.addSpring(count, count+1)

    bolid.ancor1index = count
    bolid.frontTireIndexesRight = (count+1, count+len(tire_nodes1))
    count += len(tire_nodes1)

    (tire_nodes2, tire_edges2) = tire(anchor2, 9, 10, 30, 30, "left", count-1)

    bolid.addNodes(tire_nodes2)
    bolid.addEdges(tire_edges2)
    bolid.addSpring(count, count+1)

    bolid.ancor2index = count
    bolid.frontTireIndexesLeft = (count+1, count+len(tire_nodes2))
    count += len(tire_nodes2)

    (tire_nodes3, tire_edges3) = tire(anchor3, 21, 10, 30, 30, "right", count-1)

    bolid.addNodes(tire_nodes3)
    bolid.addEdges(tire_edges3)
    bolid.addSpring(count, count+1)

    bolid.ancor3index = count
    bolid.rearTireIndexesRight = (count+1, count+len(tire_nodes3))
    count += len(tire_nodes3)

    (tire_nodes4, tire_edges4) = tire(anchor4, 23, 10, 30, 30, "left", count-1)

    bolid.addNodes(tire_nodes4)
    bolid.addEdges(tire_edges4)
    bolid.addSpring(count, count+1)

    bolid.ancor4index = count
    bolid.rearTireIndexesLeft = (count+1, count+len(tire_nodes4))
    count += len(tire_nodes4)
    bolid.translate3d(Vector3d(500, 0, 0))

    road_wf = Wireframe()

    (road_nodes, road_edges) = road(360)
    road_wf.addNodes(road_nodes)
    road_wf.addEdges(road_edges)


    #Bolid done

    # bolid.translate('x', 200)

    pv = ProjectionViewer(800,600)
    pv.addWireframe('bolid', bolid)
    pv.addWireframe('road', road_wf)
    pv.run()

