# Networks — the diagnosis ladder

## Core models
Physical link → Ethernet switching/VLAN → IPv4/IPv6 addressing → ARP/ND → default gateway and routing → DNS resolution → TCP/UDP transport → TLS certificate/handshake → HTTP/app protocol → dependency service.

Important distinction: **successful ping does not prove an application works**, and failed ping does not prove a host is unreachable (ICMP may be filtered).

## Twelve core exercises
1. Inspect NIC, addresses, interfaces and routes (`ip link`, `ip addr`, `ip route` or Windows equivalents).
2. Identify connected subnet, subnet mask/prefix and default gateway.
3. Compare local routing table decisions for on-subnet vs remote addresses.
4. Reproduce DHCP lease assignment and explain DORA; observe DNS settings.
5. Compare DNS resolver cache, authoritative DNS and recursive resolution.
6. Resolve A vs AAAA/CNAME and observe TTL and failure modes.
7. Use Wireshark/tcpdump to show a TCP handshake and connection close.
8. Explain why TCP connect success and HTTP status success are different.
9. Diagnose server-listens-on-loopback vs listens-on-LAN.
10. Inspect TLS versions, trust chain, hostname checks and expired certificates.
11. Simulate incorrect route, DNS, firewall block and misconfigured service.
12. Build a diagnostic runbook that identifies root cause with minimal invasive tests.

## Technical command toolbox
Linux: `ip`, `ss`, `dig`, `getent`, `curl`, `openssl s_client`, `tcpdump`, `tracepath`. Windows: `Get-NetIPConfiguration`, `Get-NetRoute`, `Resolve-DnsName`, `Test-NetConnection`, `Get-NetTCPConnection`, `pktmon`, Wireshark.

## Networking employment angle
For IT Support/Endpoint roles, dependable DNS/VPN/TLS troubleshooting is more useful immediately than memorizing all routing protocols. For dedicated network/data-center roles, work through Cisco CCNA objectives and Packet Tracer VLAN/inter-VLAN routing/STP/OSPF/ACL labs.

## Proof project
P07 should include separate real-lab traces for DNS, routing, SYN timeout, TLS and application failure. Redact internal addresses and identifiers. Capture only traffic from isolated authorized endpoints.

References: [Cisco CCNA](https://www.cisco.com/web/go/ccna/) · [NetAcad](https://www.netacad.com/) · [Wireshark guide](https://www.wireshark.org/docs/wsug_html_chunked/).
