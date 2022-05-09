from Demonstrator import *
cfg = Demonstrator()
for dgtz in cfg.Digitizers:
        dgtz.IRQPolicy.use = False
        for iChannel, channel in enumerate(dgtz.channels):
        channel.enable = True
                channel.triggerEnable = False
cfg.Digitizers[1].TriggerType.type = software
cfg.Digitizers[1].GroupTriggerLogic.logic = logicOr
cfg.Digitizers[1].channels[1].triggerEnable = False
cfg.Digitizers[1].channels[1].triggerThreshold = 
cfg.Digitizers[1].TriggerType.type = software
cfg.Digitizers[1].GroupTriggerLogic.logic = logicOr
cfg.Digitizers[1].channels[1].triggerEnable = False
cfg.Digitizers[1].channels[1].triggerThreshold = 
