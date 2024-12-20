# optimizer
optimizer = dict(type='AdamW', lr=0.005, momentum=0.9, weight_decay=0.001)
optim_wrapper = dict(type='OptimWrapper', optimizer=optimizer, clip_grad=dict(max_norm=35, norm_type=2))
# learning policy

param_scheduler = [
    dict(
        type='LinearLR',  # Warm-up for the first 1000 iterations
        start_factor=0.001,
        begin=0,
        end=1000,
        by_epoch=False),
    dict(
        type='PolyLR',
        eta_min=1e-4,
        power=0.9,
        begin=1000,
        end=80000,
        by_epoch=False)
]

# training schedule for 80k
train_cfg = dict(type='IterBasedTrainLoop', max_iters=80000, val_interval=4000)
val_cfg = dict(type='ValLoop')
test_cfg = dict(type='TestLoop')
default_hooks = dict(
    timer=dict(type='IterTimerHook'),
    logger=dict(type='LoggerHook', interval=50, log_metric_by_epoch=False),
    param_scheduler=dict(type='ParamSchedulerHook'),
    checkpoint=dict(type='CheckpointHook', by_epoch=False, interval=8000),
    sampler_seed=dict(type='DistSamplerSeedHook'),
    visualization=dict(type='SegVisualizationHook'))
