_base_ = [
    './_base_/models/atss_focalnet_fpn.py',
    './_base_/datasets/coco_detection.py',
    './_base_/schedules/AdamW_schedule_1x.py',
     './_base_/focal_runtime.py'
]

pretrained = 'https://projects4jw.blob.core.windows.net/focalnet/release/classification/focalnet_tiny_lrf.pth'  # noqa
model = dict(
    backbone=dict(
        type='FocalNet',
        embed_dim=96,
        depths=[2, 2, 6, 2],
        drop_path_rate=0.3,
        patch_norm=True,
        use_checkpoint=False,
        focal_windows=[11, 9, 9, 7],
        focal_levels=[3, 3, 3, 3],
        use_conv_embed=False,
        pretrained=pretrained),
    neck=dict(in_channels=[192, 384, 768]))

optimizer = dict(
    _delete_=True,
    type='AdamW',
    lr=0.0001,
    betas=(0.9, 0.999),
    weight_decay=0.05,
    paramwise_cfg=dict(
        custom_keys={
            'absolute_pos_embed': dict(decay_mult=0.),
            'relative_position_bias_table': dict(decay_mult=0.),
            'norm': dict(decay_mult=0.)
        }))


# lr_config = dict(step=[27, 33])
# runner = dict(type='EpochBasedRunner', max_epochs=36)

lr_config = dict(step=[50, 70])
runner = dict(type='EpochBasedRunner', max_epochs=100)

fp16 = dict(loss_scale=dict(init_scale=512))
