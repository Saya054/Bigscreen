import configparser

class mainConfig(object):
    def __init__(self,path):
        self.path = path
        self.config= configparser.RawConfigParser()
        self.config.read(self.path,encoding='utf-8')
    def Getconfig(self,sect,opt):
        keyvalue =  self.config[f'{sect}'][f'{opt}']
        return keyvalue
    def Addconig(self,sect,opt,value):
        if sect not in self.config.sections():
            try:
                self.config.add_section(sect)
                self.config.set(sect,opt,value)
                return True
            except Exception as e:
                return False
        else:
            try:
                self.config.set(sect,opt, value)
                return True
            except Exception as e:
                return False
    def Updateconfig(self,sect,opt,value):
        if sect not in self.config.sections():
            try:
                self.config.add_section(sect)
                self.config.set(sect,opt,value)
                return True
            except Exception as e:
                return False
        else:
            try:
                self.config.set(sect,opt, value)
                return True
            except Exception as e:
                return False
    def Deleteconfig(self,sect,opt):
        if sect in self.config.sections():
            self.config.remove_option(sect,opt)
    def InitConfig(self,sects,opts,values):
        pass