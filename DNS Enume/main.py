
import sys
import dns.resolver

print("DNS Enumeration Tool")
domain = sys.argv[1]
records_list = ["A", "AAAA", "CNAME", "MX", "NS", "PTR", "SOA", "SRV", "TXT", "rDNS"]
for record in records_list:
    try:
        answers = dns.resolver.resolve(domain, record)
        print(f"\n{record} record")    
        print("*-"*50) 
        for data in answers:          
            print(data.to_text())
        print("")
    except dns.resolver.NoAnswer:
        print(f"No {record} record found for {input}")
        pass