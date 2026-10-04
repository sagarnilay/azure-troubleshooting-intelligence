from app.main import TroubleshootingCase


def analyze_case(case: TroubleshootingCase) -> dict:
    diagnoses = []

    if case.category == "windows_update":
        diagnoses.extend(analyze_windows_update(case))

    elif case.category == "dns":
        diagnoses.extend(analyze_dns(case))

    elif case.category == "group_policy":
        diagnoses.extend(analyze_group_policy(case))

    else:
        diagnoses.append({
            "cause": "Unknown",
            "confidence": 0.0,
            "reason": "No diagnostic rules exist for this category yet."
        })

    return {
        "diagnoses": diagnoses
    }


def analyze_windows_update(case: TroubleshootingCase) -> list:
    diagnoses = []

    if case.error_code == "0x800f081f":
        diagnoses.append({
            "cause": "Component store corruption or missing repair source",
            "confidence": 0.85,
            "recommended_checks": [
                "Run DISM /Online /Cleanup-Image /CheckHealth",
                "Check CBS.log",
                "Verify the configured repair source"
            ]
        })

    elif case.error_code == "0x80070005":
        diagnoses.append({
            "cause": "Access denied",
            "confidence": 0.70,
            "recommended_checks": [
                "Check Windows Update service permissions",
                "Review relevant Event Viewer logs",
                "Check security software interference"
            ]
        })

    else:
        diagnoses.append({
            "cause": "Unknown Windows Update issue",
            "confidence": 0.20,
            "recommended_checks": [
                "Collect Windows Update logs",
                "Check Event Viewer",
                "Check Windows Update service status"
            ]
        })

    return diagnoses


def analyze_dns(case: TroubleshootingCase) -> list:
    return [{
        "cause": "DNS configuration or name resolution issue",
        "confidence": 0.50,
        "recommended_checks": [
            "Run nslookup",
            "Check configured DNS servers",
            "Check DNS client event logs"
        ]
    }]


def analyze_group_policy(case: TroubleshootingCase) -> list:
    return [{
        "cause": "Group Policy processing issue",
        "confidence": 0.50,
        "recommended_checks": [
            "Run gpresult /h report.html",
            "Check GroupPolicy operational logs",
            "Run gpupdate /force"
        ]
    }]