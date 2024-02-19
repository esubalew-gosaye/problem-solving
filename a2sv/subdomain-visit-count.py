class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_visit = {}

        for cpdomain in cpdomains:
            rep, domains = cpdomain.split()
            domain = domains.split(".")
            for j in range(len(domain)):
                domain_visit[".".join(domain[j:])] = domain_visit.get(".".join(domain[j:]), 0) + int(rep)
        
        return [f"{value} {key}" for key, value in domain_visit.items()]
