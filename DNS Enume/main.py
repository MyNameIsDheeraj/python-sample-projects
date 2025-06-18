import sys
import dns.resolver
import dns.reversename

def dns_lookup(domain):
    records_list = ["A", "AAAA", "CNAME", "MX", "NS", "PTR", "SOA", "SRV", "TXT"]
    print(f"\n\n====== DNS Lookup for: {domain} ======\n")

    for record in records_list:
        try:
            answers = dns.resolver.resolve(domain, record)
            print(f"\n{record} Record")
            print("*-" * 30)
            for data in answers:
                print(data.to_text())
        except dns.resolver.NoAnswer:
            print(f"No {record} record found for {domain}")
        except dns.resolver.NXDOMAIN:
            print(f"Domain {domain} does not exist.")
            break
        except dns.rdatatype.UnknownRdatatype:
            print(f"Unknown record type: {record}")
        except Exception as e:
            print(f"Error fetching {record} record: {e}")

    # Reverse DNS (if input is IP)
    try:
        addr = dns.reversename.from_address(domain)
        reversed_dns = dns.resolver.resolve(addr, "PTR")
        print(f"\nReverse DNS (PTR) Lookup for {domain}")
        print("*-" * 30)
        for data in reversed_dns:
            print(data.to_text())
    except Exception as e:
        print(f"No reverse DNS found for {domain} or error occurred: {e}")

if __name__ == "__main__":
    print("DNS Enumeration Tool")
    user_input = input("Enter domains or IPs separated by comma (e.g. google.com, yahoo.com, 8.8.8.8):\n")

    domains = [d.strip() for d in user_input.split(",") if d.strip()]
    if not domains:
        print("No valid input detected. Exiting.")
        sys.exit(1)

    for domain in domains:
        dns_lookup(domain)

