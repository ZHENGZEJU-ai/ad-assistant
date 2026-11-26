"""电粘附学习路径：固定知识骨架，动态挂接检索论文。"""
from __future__ import annotations

from typing import Iterator, Optional

EA = "electroadhesion"

TREE = {
    "id": "ea_root", "label": "静电吸附与电粘附", "en": "Electroadhesion",
    "desc": "通过电场在界面产生可控吸附、剪切或剥离阻力。",
    "children": [
        {"id": "ea_fund", "label": "一、物理基础", "en": "Fundamentals", "level": 1,
         "desc": "从电场、介电响应与界面接触理解吸附力的来源。", "children": [
            {"id": "ea_coulomb", "label": "静电场与吸附力", "en": "Electrostatic force", "level": 1,
             "q": "electroadhesion electrostatic force Coulomb Maxwell stress electric field"},
            {"id": "ea_jr", "label": "Johnsen–Rahbek 与库仑机制", "en": "Johnsen-Rahbek and Coulomb mechanisms", "level": 1,
             "q": "Johnsen Rahbek Coulomb electroadhesion contact resistance"},
            {"id": "ea_interface", "label": "介电材料与界面接触", "en": "Dielectrics and contact mechanics", "level": 1,
             "q": "dielectric permittivity surface roughness contact mechanics electroadhesion"},
            {"id": "ea_charge", "label": "驻极体与残余电荷", "en": "Electrets and residual charge", "level": 2,
             "q": "electret residual charge charge retention electrostatic adhesion"},
         ]},
        {"id": "ea_design", "label": "二、器件设计", "en": "Device design", "level": 2,
         "desc": "比较电极、介质、柔顺结构和驱动波形的设计取舍。", "children": [
            {"id": "ea_electrode", "label": "电极图案与几何参数", "en": "Electrode patterns", "level": 2,
             "q": "electrode pattern width pitch gap geometry electroadhesive force"},
            {"id": "ea_material", "label": "介电层与柔性基底", "en": "Dielectric and backing materials", "level": 2,
             "q": "dielectric layer thickness elastomer flexible substrate electroadhesion"},
            {"id": "ea_drive", "label": "电压、波形与释放", "en": "Voltage, waveform and release", "level": 2,
             "q": "voltage waveform frequency residual charge release electroadhesion"},
         ]},
        {"id": "ea_measure", "label": "三、性能表征", "en": "Characterization", "level": 2,
         "desc": "区分法向吸附、剪切、剥离与响应时间，并保留测试条件。", "children": [
            {"id": "ea_normal", "label": "法向吸附力", "en": "Normal adhesion force", "level": 2,
             "q": "normal adhesion force electroadhesion pull-off force"},
            {"id": "ea_shear", "label": "剪切力与承载", "en": "Shear force and load", "level": 2,
             "q": "shear force holding force load electroadhesive gripper"},
            {"id": "ea_peel", "label": "剥离与释放特性", "en": "Peeling and release", "level": 2,
             "q": "peel force peeling release electroadhesion soft gripper"},
         ]},
        {"id": "ea_apps", "label": "四、应用", "en": "Applications", "level": 2,
         "desc": "从机器人抓取、可穿戴触觉到可变刚度与爬壁应用。", "children": [
            {"id": "ea_gripper", "label": "软体夹持与材料搬运", "en": "Soft grippers", "level": 2,
             "q": "electroadhesive gripper robotic material handling soft robotics"},
            {"id": "ea_robot", "label": "机器人附着与爬壁", "en": "Robotic adhesion", "level": 2,
             "q": "electroadhesion climbing robot wall climbing aerial robot"},
            {"id": "ea_haptics", "label": "触觉显示与可穿戴离合器", "en": "Haptics and wearable clutches", "level": 2,
             "q": "electrostatic haptics wearable clutch tactile display electroadhesion"},
         ]},
    ],
}

TREES = {EA: TREE}


def get_tree(domain: Optional[str] = None) -> dict:
    if domain not in (None, EA):
        raise ValueError("只支持 electroadhesion")
    return TREE


def walk(node: Optional[dict] = None) -> Iterator[dict]:
    node = node if node is not None else TREE
    yield node
    for child in node.get("children", []):
        yield from walk(child)


def leaves(domain: Optional[str] = None) -> list:
    return [n for n in walk(get_tree(domain)) if not n.get("children")]


def find(node_id: str, domain: Optional[str] = None) -> Optional[dict]:
    return next((n for n in walk(get_tree(domain)) if n["id"] == node_id), None)


def domain_of(node_id: str) -> Optional[str]:
    return EA if any(n["id"] == node_id for n in walk(TREE)) else None
