class Target:
    """O Target define a interface específica do domínio usada pelo código do cliente"""
    
    def request(self) -> str:
        return "Target: comportamento padrão do Target."
