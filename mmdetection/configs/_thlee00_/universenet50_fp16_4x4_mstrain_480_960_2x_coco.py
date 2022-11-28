_base_ = [
    './_base_/datasets/coco_detection0.py',
    './_base_/models/universenet50.py',
    './_base_/schedules/schedule_2x.py',
    './_base_/default_runtime.py'
]

data = dict(samples_per_gpu=4)

optimizer = dict(type='SGD', lr=0.01, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(
    _delete_=True, grad_clip=dict(max_norm=35, norm_type=2))
lr_config = dict(policy='poly', power=0.9, min_lr=1e-4, by_epoch=False)
runner = dict(type='EpochBasedRunner', max_epochs=256)

fp16 = dict(loss_scale=512.)