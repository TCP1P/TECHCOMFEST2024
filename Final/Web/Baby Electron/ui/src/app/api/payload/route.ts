import { spawn } from "child_process";

export async function POST(req: Request) {
    try {
        const { payload } = await req.json();
        if (typeof payload === "string") {
            spawn("baby-electron", [payload], { timeout: 1 * 15 * 1000 });
            return Response.json({ message: "Payload received successfully." });
        } else {
            return Response.json({ message: "Payload must be a string" }, { status: 400 });
        }
    } catch (error) {
        return Response.json({ error: "Internal server error." }, { status: 500 });
    }
}
