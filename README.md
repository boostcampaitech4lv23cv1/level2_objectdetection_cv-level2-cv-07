# level2_objectdetection_cv-level2-cv-07

## 팀원 
<table>
    <th colspan=5>블랙박스</th>
    <tr height="160px">
        <td align="center" width="150px">
            <a href="https://github.com/kimk-ki"><img height="120px" width="120px" src="https://avatars.githubusercontent.com/u/110472164?v=4"/></a>
            <br />
            <a href="https://github.com/kimk-ki"><strong>🙈 김기용</strong></a>
            <br />
        </td>
        <td align="center" width="150px">
            <a href="https://github.com/SeongSuKim95"><img height="120px" width="120px" src="https://avatars.githubusercontent.com/u/62092317?v=4"/></a>
            <br/>
            <a href="https://github.com/SeongSuKim95"><strong>🐒 김성수</strong></a>
            <br />
        </td>
        <td align="center" width="150px">
            <a href="https://github.com/juye-ops"><img height="120px" width="120px" src="https://avatars.githubusercontent.com/u/103459155?v=4"/></a>
            <br/>
            <a href="https://github.com/juye-ops"><strong>🙉 김주엽</strong></a>
            <br />
        </td>
        <td align="center" width="150px">
            <a href="https://github.com/99sphere"><img height="120px" width="120px" src="https://avatars.githubusercontent.com/u/59161083?v=4"/></a>
            <br />
            <a href="https://github.com/99sphere"><strong>🙊 이  구</strong></a>
            <br />
        </td>
        <td align="center" width="150px">
            <a href="https://github.com/thlee00"><img height="120px" width="120px" src="https://avatars.githubusercontent.com/u/56151577?v=4"/></a>
            <br/>
            <a href="https://github.com/thlee00"><strong>🐵 이태희</strong></a>
            <br />
        </td>
    </tr>
</table>

- 김기용_T4020: Cascade-RCNN, Faster-RCNN 실험
- 김성수_T4039: 협업 리딩, Yolo v7 분석 및 실험, K-fold ensemble
- 김주엽_T4048: Faster-RCNN 및 YoloX, Yolov7 실험
- 이  구_T4145: 실험 초반 setting, Deformable DETR, ATSS FocalNet 실험 및 분석
- 이태희_T4172: UniverseNet, DiffusionDet 실험

## 프로젝트 개요
![image](https://user-images.githubusercontent.com/59161083/206113041-ba64f643-4321-4eb9-9a3f-a3bc83b84bbf.png)

바야흐로 대량 생산, 대량 소비의 시대. 우리는 많은 물건이 대량으로 생산되고, 소비되는 시대를 살고 있다. 하지만 이러한 문화는 '쓰레기 대란', '매립지 부족'과 같은 여러 사회 문제를 낳고 있다. 

분리수거는 이러한 환경 부담을 줄일 수 있는 방법 중 하나이다. 잘 분리배출 된 쓰레기는 자원으로서 가치를 인정받아 재활용되지만, 잘못 분리배출 되면 그대로 폐기물로 분류되어 매립 또는 소각되기 때문이다.

따라서 우리는 사진에서 쓰레기를 Detection 하는 모델을 만들어 이러한 문제점을 해결해보고자 한다. 문제 해결을 위한 데이터셋으로는 일반 쓰레기, 플라스틱, 종이, 유리 등 10 종류의 쓰레기가 찍힌 사진 데이터셋을 사용한다.

이를 이용하여 학습 시킨 모델은 쓰레기장에 설치되어 정확한 분리수거를 돕거나, 어린아이들의 분리수거 교육 등에 사용될 수 있을 것이다.

## Dataset
![image](https://user-images.githubusercontent.com/56151577/206118118-731b44e0-722d-4218-8e39-6b009c468533.png)

>우리는 수많은 쓰레기를 배출하면서 지구의 환경파괴, 야생동물의 생계 위협 등 여러 문제를 겪고 있습니다. 이러한 문제는 쓰레기를 줍는 드론, 쓰레기 배출 방지 비디오 감시, 인간의 쓰레기 분류를 돕는 AR 기술과 같은 여러 기술을 통해서 조금이나마 개선이 가능합니다.
>제공되는 이 데이터셋은 위의 기술을 뒷받침하는 쓰레기를 판별하는 모델을 학습할 수 있게 해줍니다.
- 전체 이미지 개수 : 9754장 (train: 4883장 / test: 4871장)
- Class : General trash, Paper, Paper pack, Metal, Glass, Plastic, Styrofoam, Plastic bag, Battery, Clothing
- Image size : (1024, 1024)

## 프로젝트 환경
모든 실험은 아래의 환경에서 진행되었다.

- Ubuntu 18.04.5 LTS   
- Intel(R) Xeon(R) Gold 5120 CPU @ 2.20GHz   
- NVIDIA Tesla V100-SXM2-32GB   

## 프로젝트 수행 일정
![image](https://user-images.githubusercontent.com/56151577/206137370-8eb69b24-66d4-44c9-9689-11355dda7871.png)

- Course & Mission (11.14 ~ 11.18)
    - 강의 수강 및 Special mission 진행
- EDA (11.17 ~ 11.18)
    - Train Dataset에 대한 분석 진행
- Baseline Code Analysis (11.21 ~ 11.25)
    - mmdetection, detectron2, yolo v7에 대한 baseline코드 분석
- Model Selecting (11.21 ~ 11.25)
    - 다양한 모델들 중, 최종적으로 사용할 모델 선정
- Model Training & Development (11.24 ~ 11.30)
    - 선정한 모델들의 성능 개선을 위한 다양한 방법 적용
- Ensemble (12.01)
    - 다양한 방법으로 성능을 향상시킨 모델들 간의 ensemble 진행

## Model 
![슬라이드3](https://user-images.githubusercontent.com/56151577/206129611-9de6a466-5fc3-4949-b3b8-fc39fc7eb8e0.JPG)

| idx | Ensembled Models (used fold)                                                                                                                                            | Public LB Score | Private LB Score |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|------------------|
| 1   | Faster R-CNN + Cascade R-CNN + Cascade R-CNN&weighted CE (fold 1,2,3,4) + YOLOv7 e6e + YOLO v7 + YOLO v7&cls loss (iou_threshold 0.4)                                   | 65.64           | 64.4             |
| 2   | Faster R-CNN + Cascade R-CNN + Cascade R-CNN&weighted CE (fold 1,2,3,4) + YOLOv7 e6e (iou_threshold 0.4)                                                                | 66.21           | 64.85            |
| 3   | Faster R-CNN + Cascade R-CNN + Cascade R-CNN&weighted CE (fold 1,2,3,4) + YOLOv7 e6e (iou_threshold 0.05)                                                               | 52.31           | 50.67            |
| 4   | Faster R-CNN + Cascade R-CNN&weighted CE (fold 1,2,3,4) + YOLOv7 e6e (iou_threshold 0.4)                                                                                | 66.09           | 64.64            |
| 5   | YOLOv7 e6e (fold 1,3,4,5) + Cascade R-CNN (fold 1) + Cascade R-CNN&weighted CE (fold 1,2) + Faster R-CNN (fold 2) / (iou_threshold 0.4)                                 | 66.65           | 65.01            |
| 6   | YOLOv7 e6e (fold 1,3,4,5) + Cascade R-CNN (fold 1) + Cascade R-CNN&weighted CE (fold 1,2) + Faster R-CNN (fold 2) / (iou_threshold 0.55)                                | 67.75           | 66.25            |
| 7   | YOLOv7 e6e (fold 1,3,4,5) + Cascade R-CNN (fold 1) + Cascade R-CNN&weighted CE (fold 1,2) + Faster R-CNN (fold 2) / (iou_threshold 0.3)                                 | 64.53           | 62.95            |
| 8   | Cascade R-CNN&weighted CE (iou_threshold 0.4) + YOLOv7 e6e (iou_threshold 0.4) / (total iou_threshold 0.55)                                                             | 67.29           | 65.72            |
| 9   | Cascade R-CNN&weighted CE (iou_threshold 0.3) + YOLOv7 e6e (iou_threshold 0.5) / (total iou_threshold 0.55)                                                             | 67.63           | 66.09            |
| 10  | Cascade R-CNN (fold 1), Cascade R-CNN(fold 1,2), Faster R-CNN (fold 2) (iou_threshold 0.3) / YOLOv7 e6e (fold 1,3,4,5) (iou_threshold 0.5) / (total iou_threshold 0.55) | 67.77           | 66.24            |

## Wrap-Up Report
[![image](https://user-images.githubusercontent.com/62556539/200262300-3765b3e4-0050-4760-b008-f218d079a770.png)](https://hallowed-eris-113.notion.site/Wrap-up-report-7b68cdc10c904e6c9139bc98f57752a5)

## Result
- Public LB mAP: **67.77**
- Private LB mAP : **66.25**
- Rank : **9**/19
